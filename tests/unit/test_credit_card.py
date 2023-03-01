import pytest
from moto import mock_dynamodb
import io
import os
import boto3
import sys
import pandas
os.environ["ENV"] = "dev"

sys.path.append("/home/silvio/Workspacecs/Pontte/codebase/mid-klavi/src/klavi_webhook")

from src.klavi_webhook.shared.factory.category_creditcard import build_category_creditcard_from_kavli_payload
from src.klavi_webhook.shared.repository.category_creditcard import CategoryCreditCardRepository
from src.klavi_webhook.shared.parsers.category_creditcard import parse_credit_card_payload_body, parse_credit_card_payload_open_statement, parse_credit_card_payload_closed_statement
from src.klavi_webhook.shared.models.category_creditcard import CategoryCreditCard, OpenStatement, ClosedStatement
from src.klavi_webhook.shared.exports.category_creditcard import export_category_creditcard_to_excel
from src.klavi_webhook.shared.factory.klavi_report import build_report_from_klavi_payload
from ..helpers.mocked_payloads import credit_card_payload
from ..helpers.dynamodb import create_category_credit_card_tables, create_transaction_detail_table

class TestCreditCard:

    def test_parser_credit_card_body(self):
        body_payload = credit_card_payload["data"]["Category_creditcard"]
        objects_to_test = []
        for category_creditcard in body_payload:
            parsed_data = parse_credit_card_payload_body(category_creditcard)
            objects_to_test.append(CategoryCreditCard(**parsed_data))

        assert len(objects_to_test) == len(body_payload)
        assert objects_to_test[0].agency_number == body_payload[0]["agency_number"]

    def test_parser_open_statement_body(self):
        body_payload = credit_card_payload["data"]["Category_creditcard"]
        objects_to_test = []
        total_open_statements = 0

        for category_creditcard in body_payload:
            open_statememt = category_creditcard["OpenStatement"]
            total_open_statements += 1
            parsed_data = parse_credit_card_payload_open_statement(open_statememt)
            objects_to_test.append(OpenStatement(category_id="some_id", **parsed_data))

        assert len(objects_to_test) == total_open_statements
        assert objects_to_test[0].billing_date == body_payload[0]["OpenStatement"]["billing_date"]

    def test_parser_closed_statement_body(self):
        body_payload = credit_card_payload["data"]["Category_creditcard"]
        objects_to_test = []
        total_closed_statements = 0

        for category_creditcard in body_payload:
            for closed_statement in category_creditcard["ClosedStatement"]:
                total_closed_statements += 1
                parsed_data = parse_credit_card_payload_closed_statement(closed_statement)
                objects_to_test.append(ClosedStatement(category_id="some_id", **parsed_data))

        assert len(objects_to_test) == total_closed_statements
        assert objects_to_test[0].billing_date == body_payload[0]["ClosedStatement"][0]["billing_date"]

    def test_create_a_full_credit_card_instance_from_payload(self):
        body_payload = credit_card_payload["data"]["Category_creditcard"]
        objects_to_test = []

        for category_creditcard in body_payload:
            credit_card_instance = build_category_creditcard_from_kavli_payload(category_creditcard)
            objects_to_test.append(credit_card_instance)

        assert len(objects_to_test) == len(credit_card_payload["data"]["Category_creditcard"])
        assert objects_to_test[0].open_statement.billing_date == credit_card_payload["data"]["Category_creditcard"][0]["OpenStatement"]["billing_date"]

    @mock_dynamodb
    def test_save_credit_card_into_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        create_category_credit_card_tables()
        create_transaction_detail_table()

        body_payload = credit_card_payload["data"]["Category_creditcard"]
        credit_card_repository = CategoryCreditCardRepository()
        objects_to_test = []

        for category_creditcard in body_payload:
            credit_card_instance = build_category_creditcard_from_kavli_payload(category_creditcard)
            credit_card_instance.report_id = "some id"
            objects_to_test.append(credit_card_instance)

        credit_card_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-CategoryCreditCard-dev"
        )


        assert len(objects_to_test) == len(credit_card_payload["data"]["Category_creditcard"])
        assert objects_to_test[0].open_statement.billing_date == \
               credit_card_payload["data"]["Category_creditcard"][0]["OpenStatement"]["billing_date"]
        assert len(saved_objects["Items"]) == 1

    @mock_dynamodb
    def test_get_liability_from_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")

        create_category_credit_card_tables()
        create_transaction_detail_table()

        body_payload = credit_card_payload["data"]["Category_creditcard"]
        credit_card_repository = CategoryCreditCardRepository()
        objects_to_test = []

        for credit_card in body_payload:
            credit_card_instance = build_category_creditcard_from_kavli_payload(credit_card)
            credit_card_instance.report_id = "some id"
            objects_to_test.append(credit_card_instance)

        credit_card_repository.save(objects_to_test[0])

        retrieved_credit_card = credit_card_repository.getByReportId(
            {'id': str(objects_to_test[0].id), 'report_id': objects_to_test[0].report_id})

        assert len(objects_to_test) == len(credit_card_payload["data"]["Category_creditcard"])
        assert objects_to_test[0].available_limit == \
               credit_card_payload["data"]["Category_creditcard"][0]["available_limit"]
        assert retrieved_credit_card.available_limit == str(objects_to_test[0].available_limit)

    def test_export_credit_card_to_excel(self):
        body_payload = credit_card_payload
        klavi_report = build_report_from_klavi_payload(body_payload)
        excel_file_buffer = io.BytesIO()
        pandas_excel_writter = pandas.ExcelWriter(excel_file_buffer)
        credit_card_xlsx = export_category_creditcard_to_excel(klavi_report, pandas_excel_writter)

        workbook = pandas_excel_writter.book

        assert "Category Creditcard" in workbook.sheetnames
