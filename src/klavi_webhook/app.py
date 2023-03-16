import io
import json
import os
from http import HTTPStatus

import boto3

from shared.exports.klavi_report import export_klavi_report_to_excel, export_klavi_report_to_pipefy_database
from shared.factory.event_logger import build_event_logger_from_klavi_payload
from shared.factory.klavi_report import build_report_from_klavi_payload
from shared.helpers.handler_base import Handler, Result
from shared.helpers.hw_helper import helper_fn
from shared.repository.event_logger import EventLoggerRepository
from shared.repository.klavi_report import KlaviReportRepository
#from email_helper.payload_event import event
from email_helper.validate_payload import validate_payload
from shared.data_access_objects.base_dao import DynamoDbORM
from shared.helpers.pipefy.client import PipefyClient

s3client = boto3.client('s3')

import time
import random

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

    def _initialize_pipefy_card(self):
        pipefy_client = PipefyClient()
        env = os.getenv("ENV")
        integration_table_dao = DynamoDbORM(env, "Klavi-IntegrationTable-{}".format(env))
        pipe_id = os.getenv("PIPEFY_KLAVI_PIPE_ID")
        tentativas = 5
        enquiry_cpf = self.body.get("data").get("enquiry_cpf")
        item = integration_table_dao.get({"enquiry_cpf": enquiry_cpf})
        print("LE Item")
        print(item)

        if item is None:
            integration_table_dao.put({"enquiry_cpf": enquiry_cpf, "status": "creating"})
            response = pipefy_client.create_card_into_pipe(card_data = [
                {"field_id": 'cpf_cnpj', "field_value": enquiry_cpf}
            ], pipe_id=pipe_id)
            print("response")
            print(response)


            print(response.text)

            data = json.loads(response.text)
            card_id = data.get("data").get("createCard").get("card").get("id")
            print("Card ID")
            print(card_id)

            integration_table_dao.put({"enquiry_cpf": enquiry_cpf, "status": "created", "card_id": card_id})

        if item is not None:
            while item.get('status') != "created" and tentativas > 0:
                print("tentativa {}".format(tentativas))
                time.sleep(random.randint(300, 700) / 1000)
                tentativas -= 1
                item = integration_table_dao.get({"enquiry_cpf": enquiry_cpf})

        if tentativas == 0:
            print("Tentativas acabaram")

        item = integration_table_dao.get({"enquiry_cpf": enquiry_cpf})

        return item.get("card_id")




    def is_a_enabled_report(self):
        return self.body.get("data").get("report_type") == "category_checking" or self.body.get("data").get("report_type") == "income"
    def handler(self):
        if self.is_a_enabled_report():
            card_id = self._initialize_pipefy_card()
            print("LE CARD ID")
            print(card_id)
            if self.body is None:
                return Result(HTTPStatus.OK, {"message": "no body sent"})
            self.log_request()
            print("Processing report {} from CPF {}".format( self.body.get("data").get("report_type"), self.body.get("data").get("enquiry_cpf")) )
            report = self.save_payload_into_database()
            self.save_payload_as_json(str(report.report_id), str(report.report_type))
            xls_stream = self.generate_xlsx_stream_from_report(report)
            self.upload_excel_stream_to_s3(xls_stream, str(report.report_id), str(report.report_type))
            xls_stream.close()
            export_klavi_report_to_pipefy_database(report, card_id)
            return Result(HTTPStatus.OK, {"id": str(report.id)})
        else:
            return Result(HTTPStatus.BAD_REQUEST, {"message": "report type not supported."})



def lambda_handler(event, context):
    helper_fn()

    return MidKlavi(event, context).run()


#if __name__ == '__main__':
#    result = lambda_handler(event, {})
#    print(result)
