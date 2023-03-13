from http import HTTPStatus
from shared.helpers.handler_base import Handler, Result
from shared.helpers.hw_helper import helper_fn
from shared.repository.klavi_report import KlaviReportRepository
from shared.repository.event_logger import EventLoggerRepository
from shared.factory.klavi_report import build_report_from_klavi_payload
from shared.factory.event_logger import build_event_logger_from_klavi_payload
from shared.exports.klavi_report import export_klavi_report_to_excel, export_klavi_report_to_pipefy_database
from shared.parsers.event_logger import parse_payload_into_logger_object
from shared.helpers.email import send_simple_mail

import json
import io
import boto3
import os

from src.klavi_webhook.email.payload_event import event
from src.klavi_webhook.email.validate_payload import validate_payload

s3client = boto3.client('s3')


class MidKlavi(Handler):
    body: str

    def pre_process(self):
        if self.event.get('body', None):
            self.body = json.loads(self.event['body'])
        else:
            self.body = None
    def validate(self) -> Result:
        error = validate_payload(self.body)
        if error:
            return Result(HTTPStatus.BAD_REQUEST, error)

    def save_payload_into_database(self):
        report = build_report_from_klavi_payload(self.body)
        report_repository = KlaviReportRepository()
        report_repository.save(report)

        return report

    def get_report_from_database(self, report_id, enquiry_cpf):
        report_repository = KlaviReportRepository()
        report_from_database = report_repository.getByReportId(report_id, enquiry_cpf)

        return report_from_database


    def generate_xlsx_stream_from_report(self, report):
        excel_file_buffer = io.BytesIO()
        export_klavi_report_to_excel(report, excel_file_buffer)

        return excel_file_buffer

    def upload_excel_stream_to_s3(self, excel_stream, report_id, report_type):
        name = "{report_id}/{report_type}.xlsx".format(report_id=report_id, report_type=report_type)
        bucket_name = os.getenv("KLAVI_REPORTS_BUCKET_NAME")

        s3client.put_object(Body=excel_stream.getvalue(), ContentType='application/excel', Bucket=bucket_name,
                            Key=name)

    def save_payload_as_json(self, report_id, report_type):
        self.upload_json_object_to_s3(self.body, report_id, report_type)

    def upload_json_object_to_s3(self, json_object, report_id, report_type):
        name = "{report_id}/{report_type}.json".format(report_id=report_id, report_type=report_type)
        bucket_name = os.getenv("KLAVI_REPORTS_BUCKET_NAME")
        s3client.put_object(Body=json.dumps(json_object), ContentType='application/json', Bucket=bucket_name,
                            Key=name)

    def log_request(self):
        event_logger = build_event_logger_from_klavi_payload(self.body)
        event_logger_repository = EventLoggerRepository()
        event_logger_repository.save(event_logger)

        return event_logger

    def handler(self):
        if self.body is None:
            return Result(HTTPStatus.OK, {"message": "no body sent"})
        print("Received Event")
        print(self.event)
        print("Received Context")
        print(self._context)
#        try:
        self.log_request()
        report = self.save_payload_into_database()
        export_klavi_report_to_pipefy_database(report)
        self.save_payload_as_json(str(report.report_id), str(report.report_type))
        xls_stream = self.generate_xlsx_stream_from_report(report)
        self.upload_excel_stream_to_s3(xls_stream, str(report.report_id), str(report.report_type))
        xls_stream.close()
        return Result(HTTPStatus.OK, {"id": str(report.id)})
#        except:
#            send_simple_mail("Klavi Unexpected Error", "Unexpected Error occurred", "ujinrowatany@gmail.com")
#            return Result(HTTPStatus.BAD_REQUEST, {"error": "unexpect error occurred."})



def lambda_handler(event, context):
    helper_fn()

    return MidKlavi(event, context).run()

if __name__ == '__main__':
    result = lambda_handler(event, {})
    print(result)
