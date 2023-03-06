import pytest
from moto import mock_dynamodb
import io
import os
import boto3
import sys
import pandas
os.environ["ENV"] = "dev"


sys.path.append("/home/silvio/Workspacecs/Pontte/codebase/mid-klavi/src/klavi_webhook")

from src.klavi_webhook.shared.models.financial_insight import FinancialInsight
from src.klavi_webhook.shared.parsers.financial_insight import parse_financial_insight_payload_body, parse_financial_insight_payload_cashflow_analysis, parse_financial_insight_payload_credit_analysis, parse_financial_insight_payload_credit_card_spending, parse_financial_insight_payload_financial_profile
from src.klavi_webhook.shared.factory.financial_insight import build_financial_insight_from_kavli_payload
from src.klavi_webhook.shared.repository.financial_insight import FinancialInsightRepository
from src.klavi_webhook.shared.factory.klavi_report import build_report_from_klavi_payload
from src.klavi_webhook.shared.exports.financial_insight import export_financial_insight_to_excel



financial_insight_payload = {
    "code": 200,
    "msg": "ok",
    "action": "save",
    "report_time": "2022-03-03 09:45:54",
    "data": {
        "enquiry_cpf":"12345678901",
        "user_consent":"Yes",
        "allow_autoupdate":"No",
        "connection_key":"gPuKXrCJU0kUDQO65J4k",
        "connection_id":"f45c899f-11eb-231f-97c4-4b2c16484587",
        "institution_id":"341",
        "report_type":"financial_insight",
        "report_id":"4b2c1648-231f-11eb-97c4-f45c899f4593",
        "report_version": "V1.1",
        "financial_insight": [
            {
                "bacen_id": "033",
                "bacen_name": "BANCO SANTANDER (BRASIL) S.A.",
                "bank_name": "Santander",
                "agency_number": "1076",
                "account_number": "01.01234.4",
                "cpf_verified": "01234567890",
                "account_holder": "JOHN DOE",
                "days_covered": 0,
                "cashflowAnalysis": [
                    {
                        "checking_account_balance": 0,
                        "avg_daily_balance_last_180_days": -1,
                        "avg_daily_balance_last_30_days": -1,
                        "avg_daily_balance_last_60_days": -1,
                        "avg_daily_balance_last_90_days": -1,
                        "inflow_last_180_days": -1,
                        "inflow_last_30_days": -1,
                        "inflow_last_60_days": -1,
                        "inflow_last_90_days": -1,
                        "outflow_last_180_days": -1,
                        "outflow_last_30_days": -1,
                        "outflow_last_60_days": -1,
                        "outflow_last_90_days": -1,
                        "saving_account_balance": -1
                    }
                ],
                "creditAnalysis": [
                    {
                        "overdraft_limit": 0,
                        "preapproved_loan": 0
                    }
                ],
                "creditcardSpending": [
                    {
                        "card_holder": "JOHN DOE",
                        "card_last_4_digit": "1096",
                        "card_type": "SANTANDER SX MASTER",
                        "credit_limit": 0.01,
                        "closed_bills_covered": 6,
                        "open_bill_balance": 0,
                        "last_closed_bill": -205.48,
                        "avg_last_3_closed_bills": -205.48,
                        "days_covered": 180,
                        "has_late_payment": "No",
                        "pay_bills_in_installment": "No"
                    }
                ],
                "financialProfile": [
                    {
                        "additional_overdraft_interest": 0,
                        "atm_withdrawal": 0,
                        "has_inss": "No",
                        "has_iptu_payment": "No",
                        "has_ipva_payment": "No",
                        "has_returned_cheque": "No",
                        "has_severance": "No",
                        "iof": 0,
                        "overdraft_interest": 0
                    }
                ]
            },
            {
                "bacen_id": "033",
                "bacen_name": "BANCO SANTANDER (BRASIL) S.A.",
                "bank_name": "Santander",
                "agency_number": "1076",
                "account_number": "01.12345.2",
                "cpf_verified": "01234567890",
                "account_holder": "JOHN DOE",
                "days_covered": 0,
                "cashflowAnalysis": [
                    {
                        "checking_account_balance": 0,
                        "avg_daily_balance_last_180_days": -1,
                        "avg_daily_balance_last_30_days": -1,
                        "avg_daily_balance_last_60_days": -1,
                        "avg_daily_balance_last_90_days": -1,
                        "inflow_last_180_days": -1,
                        "inflow_last_30_days": -1,
                        "inflow_last_60_days": -1,
                        "inflow_last_90_days": -1,
                        "outflow_last_180_days": -1,
                        "outflow_last_30_days": -1,
                        "outflow_last_60_days": -1,
                        "outflow_last_90_days": -1,
                        "saving_account_balance": -1
                    }
                ],
                "creditAnalysis": [
                    {
                        "overdraft_limit": 0,
                        "preapproved_loan": 0
                    }
                ],
                "creditcardSpending": None,
                "financialProfile": [
                    {
                        "additional_overdraft_interest": 0,
                        "atm_withdrawal": 0,
                        "has_inss": "No",
                        "has_iptu_payment": "No",
                        "has_ipva_payment": "No",
                        "has_returned_cheque": "No",
                        "has_severance": "No",
                        "iof": 0,
                        "overdraft_interest": 0
                    }
                ]
            }
        ]
    }
}

class TestCategoryChecking:

    def test_parser_financial_insight_body(self):
        body_payload = financial_insight_payload["data"]["financial_insight"]
        objects_to_test = []
        for financial_insight in body_payload:
            parsed_data = parse_financial_insight_payload_body(financial_insight)
            objects_to_test.append(FinancialInsight(**parsed_data))

        assert len(objects_to_test) == len(body_payload)
        assert objects_to_test[0].days_covered == body_payload[0]["days_covered"]


    def test_create_a_full_financial_insight_instance_from_payload(self):
        body_payload = financial_insight_payload["data"]["financial_insight"]
        objects_to_test = []

        for financial_insight in body_payload:
            financial_insight_instance = build_financial_insight_from_kavli_payload(financial_insight)
            objects_to_test.append(financial_insight_instance)

        assert len(objects_to_test) == len(financial_insight_payload["data"]["financial_insight"])
        assert objects_to_test[0].cpf_verified == body_payload[0]["cpf_verified"]

    @mock_dynamodb
    def test_save_financial_insight_into_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        table_args = {
            "TableName": "Klavi-FinancialInsight-dev",
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
        table_args_3 = {
            "TableName": "Klavi-CashflowAnalysis-dev",
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
        table_args_4 = {
            "TableName": "Klavi-CreditAnalysis-dev",
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
        table_args_5 = {
            "TableName": "Klavi-CreditcardSpending-dev",
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
        table_args_6 = {
            "TableName": "Klavi-FinancialProfile-dev",
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
        conn.create_table(**table_args_4)
        conn.create_table(**table_args_5)
        conn.create_table(**table_args_6)

        body_payload = financial_insight_payload["data"]["financial_insight"]
        financial_insight_repository = FinancialInsightRepository()
        objects_to_test = []

        for financial_insight in body_payload:
            financial_insight_instance = build_financial_insight_from_kavli_payload(financial_insight)
            financial_insight_instance.report_id = "some id"
            objects_to_test.append(financial_insight_instance)

        financial_insight_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-FinancialInsight-dev"
        )


        assert len(objects_to_test) == len(financial_insight_payload["data"]["financial_insight"])
        assert objects_to_test[0].cpf_verified == \
               financial_insight_payload["data"]["financial_insight"][0]["cpf_verified"]
        assert len(saved_objects["Items"]) == 1

    @mock_dynamodb
    def test_get_category_checking_from_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        table_args = {
            "TableName": "Klavi-FinancialInsight-dev",
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
        table_args_3 = {
            "TableName": "Klavi-CashflowAnalysis-dev",
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
        table_args_4 = {
            "TableName": "Klavi-CreditAnalysis-dev",
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
        table_args_5 = {
            "TableName": "Klavi-CreditcardSpending-dev",
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
        table_args_6 = {
            "TableName": "Klavi-FinancialProfile-dev",
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
        conn.create_table(**table_args_4)
        conn.create_table(**table_args_5)
        conn.create_table(**table_args_6)

        body_payload = financial_insight_payload["data"]["financial_insight"]
        financial_insight_repository = FinancialInsightRepository()
        objects_to_test = []

        for financial_insight in body_payload:
            financial_insight_instance = build_financial_insight_from_kavli_payload(financial_insight)
            financial_insight_instance.report_id = "some id"
            objects_to_test.append(financial_insight_instance)

        financial_insight_repository.save(objects_to_test[0])

        retrieved_financial_insight = financial_insight_repository.getByReportId({'id': str(objects_to_test[0].id), 'report_id': objects_to_test[0].report_id})

        assert len(objects_to_test) == len(financial_insight_payload["data"]["financial_insight"])
        assert objects_to_test[0].cpf_verified == \
               financial_insight_payload["data"]["financial_insight"][0]["cpf_verified"]
        assert retrieved_financial_insight.cpf_verified == objects_to_test[0].cpf_verified

    def test_export_financial_insight_to_excel(self):
        body_payload = financial_insight_payload["data"]
        klavi_report = build_report_from_klavi_payload(financial_insight_payload)
        excel_file_buffer = io.BytesIO()
        pandas_excel_writter = pandas.ExcelWriter(excel_file_buffer)
        financial_insight_xlsx = export_financial_insight_to_excel(klavi_report, pandas_excel_writter)

        workbook = pandas_excel_writter.book

        assert "Cashflow Analysis" in workbook.sheetnames

