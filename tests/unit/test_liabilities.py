import pytest
from moto import mock_dynamodb
import io
import os
import boto3
import sys
import pandas
os.environ["ENV"] = "dev"


sys.path.append("/home/silvio/Workspacecs/Pontte/codebase/mid-klavi/src/klavi_webhook")

from src.klavi_webhook.shared.models.liabilities import Liabilities, LiabilityStream, LiabilityTransaction
from src.klavi_webhook.shared.parsers.liabilities import parse_liabilities_payload_body
from src.klavi_webhook.shared.factory.liabilities import build_liability_from_kavli_payload
from src.klavi_webhook.shared.repository.liability import LiabilityRepository
from src.klavi_webhook.shared.exports.liabilities import export_liabilities_to_excel

from src.klavi_webhook.shared.models.financial_insight import FinancialInsight
from src.klavi_webhook.shared.parsers.financial_insight import parse_financial_insight_payload_body, parse_financial_insight_payload_cashflow_analysis, parse_financial_insight_payload_credit_analysis, parse_financial_insight_payload_credit_card_spending, parse_financial_insight_payload_financial_profile
from src.klavi_webhook.shared.factory.financial_insight import build_financial_insight_from_kavli_payload
from src.klavi_webhook.shared.repository.financial_insight import FinancialInsightRepository
from src.klavi_webhook.shared.factory.klavi_report import build_report_from_klavi_payload
from src.klavi_webhook.shared.exports.financial_insight import export_financial_insight_to_excel



liabilities_payload = {
    "code": 200,
    "msg": "ok",
    "action": "save",
    "report_time": "2022-03-03 12:52:13",
    "data": {
        "enquiry_cpf":"12345678901",
        "user_consent":"Yes",
        "allow_autoupdate":"Yes",
        "connection_key":"gPuKXrCJU0kUDQO65J4k",
        "connection_id":"f45c899f-11eb-231f-97c4-4b2c16484587",
        "institution_id":"033",
        "report_type":"liabilities",
        "report_id":"4b2c1648-231f-11eb-97c4-f45c899f4592",
        "report_version":"V1.1",
        "Liabilities": [
            {
                "account_holder": "JOHN DOE",
                "account_number": "01.12345.4",
                "agency_number": "1076",
                "bacen_id": "033",
                "bacen_name": "BANCO SANTANDER (BRASIL) S.A.",
                "bank_name": "Santander",
                "cpf_verified": "01234567890",
                "days_covered": 180,
                "number_of_liability_streams": 1,
                "total_liabilities_last_180_days": 17.25,
                "total_liabilities_last_30_days": 0,
                "total_liabilities_last_60_days": 0,
                "total_liabilities_last_90_days": 0,
                "liabilityStream": [
                    {
                        "liability_stream_type": "Credit card",
                        "liabilityTransactions": [
                            {
                                "trans_date": "2021-11-22",
                                "trans_amount": -17.25,
                                "trans_description": "CARTAO CX"
                            }
                        ]
                    }
                ]
            },
            {
                "account_holder": "JOHN DOE",
                "account_number": "01.23456.2",
                "agency_number": "1076",
                "bacen_id": "033",
                "bacen_name": "BANCO SANTANDER (BRASIL) S.A.",
                "bank_name": "Santander",
                "cpf_verified": "01234567890",
                "days_covered": 180,
                "number_of_liability_streams": 1,
                "total_liabilities_last_180_days": 37.25,
                "total_liabilities_last_30_days": 0,
                "total_liabilities_last_60_days": 0,
                "total_liabilities_last_90_days": 37.25,
                "liabilityStream": [
                    {
                        "liability_stream_type": "Credit card",
                        "liabilityTransactions": [
                            {
                                "trans_date": "2021-12-22",
                                "trans_amount": -37.25,
                                "trans_description": "CARTAO CX"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}

class TestCategoryChecking:

    def test_parser_liabilities_body(self):
        body_payload = liabilities_payload["data"]["Liabilities"]
        objects_to_test = []
        for liability in body_payload:
            parsed_data = parse_liabilities_payload_body(liability)
            objects_to_test.append(Liabilities(**parsed_data))

        assert len(objects_to_test) == len(body_payload)
        assert objects_to_test[0].total_liabilities_last_180_days == body_payload[0]["total_liabilities_last_180_days"]


    def test_create_a_full_liability_instance_from_payload(self):
        body_payload = liabilities_payload["data"]["Liabilities"]
        objects_to_test = []

        for liability in body_payload:
            liability_instance = build_liability_from_kavli_payload(liability)
            objects_to_test.append(liability_instance)

        assert len(objects_to_test) == len(liabilities_payload["data"]["Liabilities"])
        assert objects_to_test[0].days_covered == body_payload[0]["days_covered"]

    @mock_dynamodb
    def test_save_liability_into_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        table_args = {
            "TableName": "Klavi-Liabilities-dev",
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
            "TableName": "Klavi-LiabilityStream-dev",
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
        table_args_3 = {
            "TableName": "Klavi-LiabilityTransaction-dev",
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
        conn.create_table(**table_args_3)

        body_payload = liabilities_payload["data"]["Liabilities"]
        liability_repository = LiabilityRepository()
        objects_to_test = []

        for liability in body_payload:
            liability_instance = build_liability_from_kavli_payload(liability)
            liability_instance.report_id = "some id"
            objects_to_test.append(liability_instance)

        liability_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-Liabilities-dev"
        )


        assert len(objects_to_test) == len(liabilities_payload["data"]["Liabilities"])
        assert objects_to_test[0].cpf_verified == \
               liabilities_payload["data"]["Liabilities"][0]["cpf_verified"]
        assert len(saved_objects["Items"]) == 1

    @mock_dynamodb
    def test_get_liability_from_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")

        table_args = {
            "TableName": "Klavi-Liabilities-dev",
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
            "TableName": "Klavi-LiabilityStream-dev",
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
        table_args_3 = {
            "TableName": "Klavi-LiabilityTransaction-dev",
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
        conn.create_table(**table_args_3)

        body_payload = liabilities_payload["data"]["Liabilities"]
        liability_repository = LiabilityRepository()
        objects_to_test = []

        for liability in body_payload:
            liability_instance = build_liability_from_kavli_payload(liability)
            liability_instance.report_id = "some id"
            objects_to_test.append(liability_instance)

        liability_repository.save(objects_to_test[0])

        retrieved_liabilities = liability_repository.getByReportId({'id': str(objects_to_test[0].id), 'report_id': objects_to_test[0].report_id})

        assert len(objects_to_test) == len(liabilities_payload["data"]["Liabilities"])
        assert objects_to_test[0].cpf_verified == \
               liabilities_payload["data"]["Liabilities"][0]["cpf_verified"]
        assert retrieved_liabilities.cpf_verified == objects_to_test[0].cpf_verified

    def test_export_liability_to_excel(self):
        body_payload = liabilities_payload["data"]
        klavi_report = build_report_from_klavi_payload(liabilities_payload)
        excel_file_buffer = io.BytesIO()
        pandas_excel_writter = pandas.ExcelWriter(excel_file_buffer)
        liability_xlsx = export_liabilities_to_excel(klavi_report, pandas_excel_writter)

        workbook = pandas_excel_writter.book

        assert "Liabilities Streams" in workbook.sheetnames

