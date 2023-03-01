import pytest
from moto import mock_dynamodb
import io
import os
import boto3
import sys
import pandas
os.environ["ENV"] = "dev"


sys.path.append("/home/silvio/Workspacecs/Pontte/codebase/mid-klavi/src/klavi_webhook")

from src.klavi_webhook.shared.models.risk_label import RiskLabel
from src.klavi_webhook.shared.parsers.risk_label import parse_risk_label_payload_body
from src.klavi_webhook.shared.factory.risk_label import build_risk_label_from_kavli_payload
from src.klavi_webhook.shared.repository.risk_label import RiskLabelRepository
from src.klavi_webhook.shared.exports.risk_label import export_risk_label_to_excel
from src.klavi_webhook.shared.factory.klavi_report import build_report_from_klavi_payload


from ..helpers.mocked_payloads import risk_label_payload
from ..helpers.dynamodb import create_risk_label_tables



class TestRiskLabel:

    def test_parser_risk_label_body(self):
        body_payload = risk_label_payload["data"]["Risk_label"]
        objects_to_test = []
        parsed_data = parse_risk_label_payload_body(body_payload)
        objects_to_test.append(RiskLabel(**parsed_data))

        assert objects_to_test[0].account_info["bacen_id"] == body_payload["accountInfo"]["bacen_id"]


    def test_create_a_full_risk_label_instance_from_payload(self):
        body_payload = risk_label_payload["data"]["Risk_label"]
        objects_to_test = []

        risk_label_instance = build_risk_label_from_kavli_payload(body_payload)
        objects_to_test.append(risk_label_instance)

        assert objects_to_test[0].account_info["bacen_id"] == body_payload["accountInfo"]["bacen_id"]

    @mock_dynamodb
    def test_save_risk_label_into_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        create_risk_label_tables()
        body_payload = risk_label_payload["data"]["Risk_label"]
        risk_label_repository = RiskLabelRepository()
        objects_to_test = []

        risk_label_instance = build_risk_label_from_kavli_payload(body_payload)
        risk_label_instance.report_id = "some id"
        objects_to_test.append(risk_label_instance)

        risk_label_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-RiskLabel-dev"
        )


        assert objects_to_test[0].account_info["bacen_id"] == body_payload["accountInfo"]["bacen_id"]
        assert len(saved_objects["Items"]) == 1

    @mock_dynamodb
    def test_get_risk_label_from_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")

        create_risk_label_tables()
        body_payload = risk_label_payload["data"]["Risk_label"]
        risk_label_repository = RiskLabelRepository()
        objects_to_test = []

        risk_label_instance = build_risk_label_from_kavli_payload(body_payload)
        risk_label_instance.report_id = "some id"
        objects_to_test.append(risk_label_instance)

        risk_label_repository.save(objects_to_test[0])

        retrieved_risk_label = risk_label_repository.getByReportId({'id': str(objects_to_test[0].id), 'report_id': objects_to_test[0].report_id})


        assert retrieved_risk_label.account_info["bacen_id"] == body_payload["accountInfo"]["bacen_id"]

    def test_export_risk_label_to_excel(self):
        body_payload = risk_label_payload["data"]
        klavi_report = build_report_from_klavi_payload(risk_label_payload)
        excel_file_buffer = io.BytesIO()
        pandas_excel_writter = pandas.ExcelWriter(excel_file_buffer)
        risk_label_xlsx = export_risk_label_to_excel(klavi_report, pandas_excel_writter)

        workbook = pandas_excel_writter.book

        assert "RiskLabel" in workbook.sheetnames

