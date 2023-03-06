import pytest
from moto import mock_dynamodb
import io
import os
import boto3
import sys
import pandas
os.environ["ENV"] = "dev"


sys.path.append("/home/silvio/Workspacecs/Pontte/codebase/mid-klavi/src/klavi_webhook")

from src.klavi_webhook.shared.models.category_checking import CategoryChecking
from src.klavi_webhook.shared.parsers.category_checking import parse_category_checking_payload_body
from src.klavi_webhook.shared.factory.category_checking import build_category_checking_from_kavli_payload
from src.klavi_webhook.shared.repository.category_checking import CategoryCheckingRepository
from src.klavi_webhook.shared.factory.klavi_report import build_report_from_klavi_payload
from src.klavi_webhook.shared.exports.category_checking import export_category_checkings_to_excel
from ..helpers.mocked_payloads import category_checking_payload


class TestCategoryChecking:

    def test_parser_category_checking_body(self):
        body_payload = category_checking_payload["data"]["Category_checking"]
        objects_to_test = []
        for category_checking in body_payload:
            parsed_data = parse_category_checking_payload_body(category_checking)
            objects_to_test.append(CategoryChecking(**parsed_data))

        assert len(objects_to_test) == len(body_payload)
        assert objects_to_test[0].holder_name == body_payload[0]["holder_name"]


    def test_create_a_full_category_checking_instance_from_payload(self):
        body_payload = category_checking_payload["data"]["Category_checking"]
        objects_to_test = []

        for category_checking in body_payload:
            category_checking_instance = build_category_checking_from_kavli_payload(category_checking)
            objects_to_test.append(category_checking_instance)

        assert len(objects_to_test) == len(category_checking_payload["data"]["Category_checking"])
        assert len(objects_to_test[0].transaction_details) == len(body_payload[0]["TransactionDetail"])

    @mock_dynamodb
    def test_save_category_checking_into_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        table_args = {
            "TableName": "Klavi-CategoryChecking-dev",
            'KeySchema': [
                {'AttributeName': 'report_id', 'KeyType': 'HASH'},
            ],
            'AttributeDefinitions': [
                {'AttributeName': 'report_id', 'AttributeType': 'S'}
            ],
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        }
        table_args_2 = {
            "TableName": "Klavi-TransactionDetail-dev",
            'KeySchema': [
                {'AttributeName': 'category_id', 'KeyType': 'HASH'},
            ],
            'AttributeDefinitions': [
                {'AttributeName': 'category_id', 'AttributeType': 'S'}
            ],
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        }
        conn.create_table(**table_args)
        conn.create_table(**table_args_2)

        body_payload = category_checking_payload["data"]["Category_checking"]
        category_checking_repository = CategoryCheckingRepository()
        objects_to_test = []

        for category_checking in body_payload:
            credit_checking_instance = build_category_checking_from_kavli_payload(category_checking)
            credit_checking_instance.report_id = "some id"
            objects_to_test.append(credit_checking_instance)

        category_checking_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-CategoryChecking-dev"
        )


        assert len(objects_to_test) == len(category_checking_payload["data"]["Category_checking"])
        assert objects_to_test[0].cpf_verified == \
               category_checking_payload["data"]["Category_checking"][0]["cpf_verified"]
        assert len(saved_objects["Items"]) == 1

    @mock_dynamodb
    def test_get_category_checking_from_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        table_args = {
            "TableName": "Klavi-CategoryChecking-dev",
            'KeySchema': [
                {'AttributeName': 'report_id', 'KeyType': 'HASH'},
            ],
            'AttributeDefinitions': [
                {'AttributeName': 'report_id', 'AttributeType': 'S'}
            ],
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        }
        table_args_2 = {
            "TableName": "Klavi-TransactionDetail-dev",
            'KeySchema': [
                {'AttributeName': 'category_id', 'KeyType': 'HASH'},
            ],
            'AttributeDefinitions': [
                {'AttributeName': 'category_id', 'AttributeType': 'S'}
            ],
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        }
        conn.create_table(**table_args)
        conn.create_table(**table_args_2)

        body_payload = category_checking_payload["data"]["Category_checking"]
        category_checking_repository = CategoryCheckingRepository()
        objects_to_test = []

        for category_checking in body_payload:
            credit_checking_instance = build_category_checking_from_kavli_payload(category_checking)
            credit_checking_instance.report_id = "some-id"
            objects_to_test.append(credit_checking_instance)

        category_checking_repository.save(objects_to_test[0])

        retrieved_category_checking = category_checking_repository.getByReportId({'id': str(objects_to_test[0].id), 'report_id': objects_to_test[0].report_id})

        assert len(objects_to_test) == len(category_checking_payload["data"]["Category_checking"])
        assert objects_to_test[0].cpf_verified == \
               category_checking_payload["data"]["Category_checking"][0]["cpf_verified"]
        assert retrieved_category_checking.bacen_id == objects_to_test[0].bacen_id

    def test_export_category_checking_to_excel(self):
        body_payload = category_checking_payload["data"]
        klavi_report = build_report_from_klavi_payload(category_checking_payload)
        excel_file_buffer = io.BytesIO()
        pandas_excel_writter = pandas.ExcelWriter(excel_file_buffer)
        category_checking_xlsx = export_category_checkings_to_excel(klavi_report, pandas_excel_writter)

        workbook = pandas_excel_writter.book

        assert "Category Checking" in workbook.sheetnames





