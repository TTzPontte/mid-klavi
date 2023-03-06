import pytest
from moto import mock_dynamodb
import io
import os
import boto3
import sys
import pandas
os.environ["ENV"] = "dev"


sys.path.append("/home/silvio/Workspacecs/Pontte/codebase/mid-klavi/src/klavi_webhook")

from src.klavi_webhook.shared.models.balance import Balance
from src.klavi_webhook.shared.parsers.balance import parse_balance_payload_body
from src.klavi_webhook.shared.factory.balance import build_balance_from_kavli_payload
from src.klavi_webhook.shared.repository.balance import BalanceRepository
from src.klavi_webhook.shared.exports.balance import export_balance_to_excel

from src.klavi_webhook.shared.factory.klavi_report import build_report_from_klavi_payload
from ..helpers.mocked_payloads import balance_payload
from ..helpers.dynamodb import create_balance_tables



class TestBalance:

    def test_parser_balance_body(self):
        body_payload = balance_payload["data"]["accountBalance"]
        objects_to_test = []
        for balance in body_payload:
            parsed_data = parse_balance_payload_body(balance)
            objects_to_test.append(Balance(**parsed_data))

        assert len(objects_to_test) == len(body_payload)
        assert objects_to_test[0].current_balance == body_payload[0]["current_balance"]


    def test_create_a_full_balance_instance_from_payload(self):
        body_payload = balance_payload["data"]["accountBalance"]
        objects_to_test = []

        for balance in body_payload:
            balance_instance = build_balance_from_kavli_payload(balance)
            objects_to_test.append(balance_instance)

        assert len(objects_to_test) == len(balance_payload["data"]["accountBalance"])
        assert objects_to_test[0].current_balance == body_payload[0]["current_balance"]

    @mock_dynamodb
    def test_save_balance_into_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        create_balance_tables()
        body_payload = balance_payload["data"]["accountBalance"]
        balance_repository = BalanceRepository()
        objects_to_test = []

        for balance in body_payload:
            balance_instance = build_balance_from_kavli_payload(balance)
            balance_instance.report_id = "some id"
            objects_to_test.append(balance_instance)

        balance_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-Balance-dev"
        )


        assert len(objects_to_test) == len(balance_payload["data"]["accountBalance"])
        assert objects_to_test[0].current_balance == body_payload[0]["current_balance"]
        assert len(saved_objects["Items"]) == 1

    @mock_dynamodb
    def test_get_balance_from_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")

        create_balance_tables()
        body_payload = balance_payload["data"]["accountBalance"]
        balance_repository = BalanceRepository()
        objects_to_test = []

        for balance in body_payload:
            balance_instance = build_balance_from_kavli_payload(balance)
            balance_instance.report_id = "some id"
            objects_to_test.append(balance_instance)

        balance_repository.save(objects_to_test[0])

        retrieved_balance = balance_repository.getByReportId({'id': str(objects_to_test[0].id), 'report_id': objects_to_test[0].report_id})

        assert len(objects_to_test) == len(balance_payload["data"]["accountBalance"])
        assert objects_to_test[0].current_balance == body_payload[0]["current_balance"]
        assert retrieved_balance.current_balance == objects_to_test[0].current_balance

    def test_export_balance_to_excel(self):
        body_payload = balance_payload["data"]
        klavi_report = build_report_from_klavi_payload(balance_payload)
        excel_file_buffer = io.BytesIO()
        pandas_excel_writter = pandas.ExcelWriter(excel_file_buffer)
        balance_xlsx = export_balance_to_excel(klavi_report, pandas_excel_writter)

        workbook = pandas_excel_writter.book

        assert "Balance" in workbook.sheetnames

