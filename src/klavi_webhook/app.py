from http import HTTPStatus
from shared.helpers.handler_base import Handler, Result
from shared.helpers.hw_helper import helper_fn
from shared.repository.klavi_report import KlaviReportRepository
from shared.repository.event_logger import EventLoggerRepository
from shared.factory.klavi_report import build_report_from_klavi_payload
from shared.factory.event_logger import build_event_logger_from_klavi_payload
from shared.exports.klavi_report import export_klavi_report_to_excel
from shared.parsers.event_logger import parse_payload_into_logger_object
import json
import io
import boto3
import os
s3client = boto3.client('s3')


class MidKlavi(Handler):
    body: str

    def pre_process(self):
        if self.event['body']:
            self.body = json.loads(self.event['body'])

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

    def upload_excel_stream_to_s3(self, excel_stream, report_id):
        name = "{report_id}.xlsx".format(report_id=report_id)
        s3client.put_object(Body=excel_stream.getvalue(), ContentType='application/excel', Bucket="silvio-dev",
                            Key=name)

    def save_payload_as_json(self, report_id):
        self.upload_json_object_to_s3(self.body, report_id)

    def upload_json_object_to_s3(self, json_object, report_id):
        name = "{report_id}_payload.json".format(report_id=report_id)
        s3client.put_object(Body=json.dumps(json_object), ContentType='application/json', Bucket="silvio-dev",
                            Key=name)

    def log_request(self):
        event_logger = build_event_logger_from_klavi_payload(self.body)
        event_logger_repository = EventLoggerRepository()
        event_logger_repository.save(event_logger)

        return event_logger

    def handler(self):
        self.log_request()
        report = self.save_payload_into_database()
        self.save_payload_as_json(str(report.id))
        xls_stream = self.generate_xlsx_stream_from_report(report)
        self.upload_excel_stream_to_s3(xls_stream, str(report.id))
        xls_stream.close()
        return Result(HTTPStatus.OK, {"id": str(report.id)})
        #enviroment = os.getenv('ENV')
        #print("Envroment")
        #print(enviroment)
        #print("________________")
        #return Result(HTTPStatus.OK, {"id": "OK"})


def lambda_handler(event, context):
    helper_fn()
    return MidKlavi(event, context).run()
