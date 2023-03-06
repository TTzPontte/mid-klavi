import pytest
from moto import mock_dynamodb
import io
import os
import boto3
import sys
import pandas
os.environ["ENV"] = "dev"


sys.path.append("/home/silvio/Workspacecs/Pontte/codebase/mid-klavi/src/klavi_webhook")

from src.klavi_webhook.shared.models.income import Income, IncomeStream, IncomeTransaction
from src.klavi_webhook.shared.parsers.income import parse_income_payload_body
from src.klavi_webhook.shared.factory.income import build_income_from_kavli_payload
from src.klavi_webhook.shared.repository.income import IncomeRepository
from src.klavi_webhook.shared.exports.income import export_income_to_excel

from src.klavi_webhook.shared.models.financial_insight import FinancialInsight
from src.klavi_webhook.shared.parsers.financial_insight import parse_financial_insight_payload_body, parse_financial_insight_payload_cashflow_analysis, parse_financial_insight_payload_credit_analysis, parse_financial_insight_payload_credit_card_spending, parse_financial_insight_payload_financial_profile
from src.klavi_webhook.shared.factory.financial_insight import build_financial_insight_from_kavli_payload
from src.klavi_webhook.shared.repository.financial_insight import FinancialInsightRepository
from src.klavi_webhook.shared.factory.klavi_report import build_report_from_klavi_payload
from src.klavi_webhook.shared.exports.financial_insight import export_financial_insight_to_excel
from ..helpers.mocked_payloads import income_payload
from ..helpers.dynamodb import create_income_tables



class TestIncome:

    def test_parser_income_body(self):
        body_payload = income_payload["data"]["Income"]
        objects_to_test = []
        for income in body_payload:
            parsed_data = parse_income_payload_body(income)
            objects_to_test.append(Income(**parsed_data))

        assert len(objects_to_test) == len(body_payload)
        assert objects_to_test[0].total_income_last_180_days == body_payload[0]["total_income_last_180_days"]


    def test_create_a_full_income_instance_from_payload(self):
        body_payload = income_payload["data"]["Income"]
        objects_to_test = []

        for income in body_payload:
            income_instance = build_income_from_kavli_payload(income)
            objects_to_test.append(income_instance)

        assert len(objects_to_test) == len(income_payload["data"]["Income"])
        assert objects_to_test[0].days_covered == body_payload[0]["days_covered"]

    @mock_dynamodb
    def test_save_income_into_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        create_income_tables()
        body_payload = income_payload["data"]["Income"]
        income_repository = IncomeRepository()
        objects_to_test = []

        for income in body_payload:
            income_instance = build_income_from_kavli_payload(income)
            income_instance.report_id = "some id"
            objects_to_test.append(income_instance)

        income_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-Income-dev"
        )


        assert len(objects_to_test) == len(income_payload["data"]["Income"])
        assert objects_to_test[0].cpf_verified == \
               income_payload["data"]["Income"][0]["cpf_verified"]
        assert len(saved_objects["Items"]) == 1

    @mock_dynamodb
    def test_get_income_from_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")

        create_income_tables()
        body_payload = income_payload["data"]["Income"]
        income_repository = IncomeRepository()
        objects_to_test = []

        for income in body_payload:
            income_instance = build_income_from_kavli_payload(income)
            income_instance.report_id = "some id"
            objects_to_test.append(income_instance)

        income_repository.save(objects_to_test[0])

        retrieved_income = income_repository.getByReportId({'id': str(objects_to_test[0].id), 'report_id': objects_to_test[0].report_id})

        assert len(objects_to_test) == len(income_payload["data"]["Income"])
        assert objects_to_test[0].cpf_verified == \
               income_payload["data"]["Income"][0]["cpf_verified"]
        assert retrieved_income.cpf_verified == objects_to_test[0].cpf_verified

    def test_export_income_to_excel(self):
        body_payload = income_payload["data"]
        klavi_report = build_report_from_klavi_payload(income_payload)
        excel_file_buffer = io.BytesIO()
        pandas_excel_writter = pandas.ExcelWriter(excel_file_buffer)
        income_xlsx = export_income_to_excel(klavi_report, pandas_excel_writter)

        workbook = pandas_excel_writter.book

        assert "Income Streams" in workbook.sheetnames

