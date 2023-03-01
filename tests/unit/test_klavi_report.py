import pytest
from moto import mock_dynamodb
import io
import os
import boto3
import sys
import pandas
os.environ["ENV"] = "dev"


sys.path.append("/home/silvio/Workspacecs/Pontte/codebase/mid-klavi/src/klavi_webhook")

from src.klavi_webhook.shared.models.klavi_report import KlaviReport
from src.klavi_webhook.shared.parsers.klavi_report import parse_klavi_report_payload_body
from src.klavi_webhook.shared.factory.klavi_report import build_report_from_klavi_payload
from src.klavi_webhook.shared.repository.klavi_report import KlaviReportRepository
from src.klavi_webhook.shared.exports.klavi_report import export_klavi_report_to_excel
from ..helpers.dynamodb import create_all_klavi_tables, create_table
from ..helpers.mocked_payloads import category_checking_payload, credit_card_payload, identity_payload, income_payload, balance_payload, score_k1_payload, risk_label_payload


klavi_report_payload = {
    "code":200,
    "msg":"ok",
    "action": "save",
    "report_time":"2019-12-23 06:10:43",
    "data":{
        "enquiry_cpf":"12345678901",
        "user_consent":"Yes",
        "allow_autoupdate":"Yes",
        "connection_key":"gPuKXrCJU0kUDQO65J4k",
        "connection_id":"f45c899f-11eb-231f-97c4-4b2c16484587",
        "institution_id":"033",
        "report_type":"category_checking",
        "report_id":"4b2c1648-231f-11eb-97c4-f45c899f4587",
        "report_version":"V1",
        "Category_checking":[
            {
                "bank_name":"Santander",
                "bacen_name":"BANCO SANTANDER (BRASIL) S.A.",
                "bacen_id":"033",
                "bank_branch":"1234",
                "account":"12.345678.9",
                "operation_code":"001",
                "cpf_verified":"12345678901",
                "holder_name":"Usuaro anonimo",
                "balance":18.75,
                "TransactionDetail":[
                    {
                        "trans_date":"2019-12-23",
                        "trans_amount":-150.05,
                        "trans_description":"PREST EMPRESTIMOS/FINANCIAMENTOS AYMORE",
                        "balance":18.75,
                        "category":"Empréstimo"
                    },
                    {
                        "trans_date":"2019-12-20",
                        "trans_amount":150,
                        "trans_description":"TED MESMA TITULARIDADE CIP 237-3750-0000001234567",
                        "balance":168.8,
                        "category":"Transferência"
                    }
                ]
            }
        ]
    }
}

class TestKlaviReport:

    def test_parser_klavi_body(self):
        body_payload = klavi_report_payload
        objects_to_test = []
        parsed_data = parse_klavi_report_payload_body(body_payload)
        objects_to_test.append(KlaviReport(**parsed_data))

        assert len(objects_to_test) == 1
        assert objects_to_test[0].enquiry_cpf == body_payload["data"]["enquiry_cpf"]


    def test_create_a_full_klavi_report_instance_from_payload(self):
        body_payload = klavi_report_payload
        objects_to_test = []

        klavi_report_instance = build_report_from_klavi_payload(body_payload)
        objects_to_test.append(klavi_report_instance)

        assert len(objects_to_test) == 1
        assert objects_to_test[0].enquiry_cpf == body_payload["data"]["enquiry_cpf"]

    @mock_dynamodb
    def test_save_klavi_report_into_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        create_table("Klavi-KlaviReport-dev", "id")
        create_table("Klavi-CategoryChecking-dev", "report_id")
        create_table("Klavi-TransactionDetail-dev", "category_id")


        body_payload = klavi_report_payload
        klavi_report_repository = KlaviReportRepository()
        objects_to_test = []

        credit_checking_instance = build_report_from_klavi_payload(body_payload)
        credit_checking_instance.report_id = "some id"
        objects_to_test.append(credit_checking_instance)

        klavi_report_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-KlaviReport-dev"
        )


        assert len(objects_to_test) == 1
        assert objects_to_test[0].enquiry_cpf == klavi_report_payload["data"]["enquiry_cpf"]
        assert len(saved_objects["Items"]) == 1

    @mock_dynamodb
    def test_save_klavi_report_category_checking(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        create_all_klavi_tables()

        body_payload = category_checking_payload
        klavi_report_repository = KlaviReportRepository()
        objects_to_test = []

        report_instance = build_report_from_klavi_payload(body_payload)
        objects_to_test.append(report_instance)

        klavi_report_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-KlaviReport-dev"
        )


        assert len(objects_to_test) == 1
        assert objects_to_test[0].enquiry_cpf == klavi_report_payload["data"]["enquiry_cpf"]
        assert len(saved_objects["Items"]) == 1

    @mock_dynamodb
    def test_save_klavi_report_category_credit_card(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        create_all_klavi_tables()

        body_payload = credit_card_payload
        klavi_report_repository = KlaviReportRepository()
        objects_to_test = []

        report_instance = build_report_from_klavi_payload(body_payload)
        objects_to_test.append(report_instance)

        klavi_report_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-KlaviReport-dev"
        )

        assert len(objects_to_test) == 1
        assert objects_to_test[0].enquiry_cpf == klavi_report_payload["data"]["enquiry_cpf"]
        assert len(saved_objects["Items"]) == 1

    @mock_dynamodb
    def test_save_klavi_report_identity(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        create_all_klavi_tables()

        body_payload = identity_payload
        klavi_report_repository = KlaviReportRepository()
        objects_to_test = []

        report_instance = build_report_from_klavi_payload(body_payload)
        objects_to_test.append(report_instance)

        klavi_report_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-KlaviReport-dev"
        )

        assert len(objects_to_test) == 1
        assert objects_to_test[0].enquiry_cpf == body_payload["data"]["enquiry_cpf"]
        assert len(saved_objects["Items"]) == 1

    @mock_dynamodb
    def test_save_klavi_report_income(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        create_all_klavi_tables()

        body_payload = income_payload
        klavi_report_repository = KlaviReportRepository()
        objects_to_test = []

        report_instance = build_report_from_klavi_payload(body_payload)
        objects_to_test.append(report_instance)

        klavi_report_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-KlaviReport-dev"
        )

        assert len(objects_to_test) == 1
        assert objects_to_test[0].enquiry_cpf == body_payload["data"]["enquiry_cpf"]
        assert len(saved_objects["Items"]) == 1

    @mock_dynamodb
    def test_save_klavi_report_balance(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        create_all_klavi_tables()

        body_payload = balance_payload
        klavi_report_repository = KlaviReportRepository()
        objects_to_test = []

        report_instance = build_report_from_klavi_payload(body_payload)
        objects_to_test.append(report_instance)

        klavi_report_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-KlaviReport-dev"
        )

        assert len(objects_to_test) == 1
        assert objects_to_test[0].enquiry_cpf == body_payload["data"]["enquiry_cpf"]
        assert len(saved_objects["Items"]) == 1

    @mock_dynamodb
    def test_save_klavi_report_score_k1(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        create_all_klavi_tables()

        body_payload = score_k1_payload
        klavi_report_repository = KlaviReportRepository()
        objects_to_test = []

        report_instance = build_report_from_klavi_payload(body_payload)
        objects_to_test.append(report_instance)

        klavi_report_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-KlaviReport-dev"
        )

        assert len(objects_to_test) == 1
        assert objects_to_test[0].enquiry_cpf == body_payload["data"]["enquiry_cpf"]
        assert len(saved_objects["Items"]) == 1

    @mock_dynamodb
    def test_save_klavi_report_risk_label(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        create_all_klavi_tables()

        body_payload = risk_label_payload
        klavi_report_repository = KlaviReportRepository()
        objects_to_test = []

        report_instance = build_report_from_klavi_payload(body_payload)
        objects_to_test.append(report_instance)

        klavi_report_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-KlaviReport-dev"
        )

        assert len(objects_to_test) == 1
        assert objects_to_test[0].enquiry_cpf == body_payload["data"]["enquiry_cpf"]
        assert len(saved_objects["Items"]) == 1

    @mock_dynamodb
    def test_get_klavi_report_from_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        create_table("Klavi-KlaviReport-dev", "id")
        create_table("Klavi-CategoryChecking-dev", "report_id")
        create_table("Klavi-TransactionDetail-dev", "category_id")

        body_payload = klavi_report_payload
        klavi_report_repository = KlaviReportRepository()
        objects_to_test = []

        klavi_report_instance = build_report_from_klavi_payload(body_payload)
        objects_to_test.append(klavi_report_instance)

        klavi_report_repository.save(objects_to_test[0])

        retrieved_klavi_report = klavi_report_repository.getByReportId(str(objects_to_test[0].id), objects_to_test[0].enquiry_cpf)

        assert len(objects_to_test) == 1
        assert objects_to_test[0].enquiry_cpf == klavi_report_payload["data"]["enquiry_cpf"]
        assert retrieved_klavi_report.enquiry_cpf == objects_to_test[0].enquiry_cpf

    def test_export_klavi_report_to_excel(self):
        body_payload = klavi_report_payload
        klavi_report = build_report_from_klavi_payload(body_payload)
        excel_file_buffer = io.BytesIO()
        pandas_excel_writter = pandas.ExcelWriter(excel_file_buffer)
        klavi_report = export_klavi_report_to_excel(klavi_report, excel_file_buffer)

        workbook = klavi_report.book

        assert "Category Checking" in workbook.sheetnames





