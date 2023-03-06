import pytest
from moto import mock_dynamodb
import io
import os
import boto3
import sys
import pandas
os.environ["ENV"] = "dev"


sys.path.append("/home/silvio/Workspacecs/Pontte/codebase/mid-klavi/src/klavi_webhook")

from src.klavi_webhook.shared.models.score_k1 import ScoreK1
from src.klavi_webhook.shared.parsers.score_k1 import parse_score_k1_payload_body
from src.klavi_webhook.shared.factory.score_k1 import build_score_k1_from_kavli_payload
from src.klavi_webhook.shared.repository.score_k1 import ScoreK1Repository
from src.klavi_webhook.shared.exports.score_k1 import export_score_k1_to_excel
from src.klavi_webhook.shared.factory.klavi_report import build_report_from_klavi_payload


from ..helpers.mocked_payloads import score_k1_payload
from ..helpers.dynamodb import create_score_k1_tables



class TestScoreK1:

    def test_parser_score_k1_body(self):
        body_payload = score_k1_payload["data"]["score_info"]
        objects_to_test = []
        parsed_data = parse_score_k1_payload_body(body_payload)
        objects_to_test.append(ScoreK1(**parsed_data))

        assert objects_to_test[0].score_detail["score_k1"] == body_payload["score_detail"]["score_k1"]


    def test_create_a_full_score_k1_instance_from_payload(self):
        body_payload = score_k1_payload["data"]["score_info"]
        objects_to_test = []

        score_k1_instance = build_score_k1_from_kavli_payload(body_payload)
        objects_to_test.append(score_k1_instance)

        assert objects_to_test[0].score_detail["score_k1"] == body_payload["score_detail"]["score_k1"]

    @mock_dynamodb
    def test_save_score_k1_into_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        create_score_k1_tables()
        body_payload = score_k1_payload["data"]["score_info"]
        score_k1_repository = ScoreK1Repository()
        objects_to_test = []

        score_k1_instance = build_score_k1_from_kavli_payload(body_payload)
        score_k1_instance.report_id = "some id"
        objects_to_test.append(score_k1_instance)

        score_k1_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-ScoreK1-dev"
        )


        assert objects_to_test[0].score_detail["score_k1"] == body_payload["score_detail"]["score_k1"]
        assert len(saved_objects["Items"]) == 1

    @mock_dynamodb
    def test_get_score_k1_from_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")

        create_score_k1_tables()
        body_payload = score_k1_payload["data"]["score_info"]
        score_k1_repository = ScoreK1Repository()
        objects_to_test = []

        score_k1_instance = build_score_k1_from_kavli_payload(body_payload)
        score_k1_instance.report_id = "some id"
        objects_to_test.append(score_k1_instance)

        score_k1_repository.save(objects_to_test[0])

        retrieved_score_k1 = score_k1_repository.getByReportId({'id': str(objects_to_test[0].id), 'report_id': objects_to_test[0].report_id})

        assert objects_to_test[0].score_detail["score_k1"] == body_payload["score_detail"]["score_k1"]

        assert retrieved_score_k1.score_detail["score_k1"] == body_payload["score_detail"]["score_k1"]

    def test_export_score_k1_to_excel(self):
        body_payload = score_k1_payload["data"]
        klavi_report = build_report_from_klavi_payload(score_k1_payload)
        excel_file_buffer = io.BytesIO()
        pandas_excel_writter = pandas.ExcelWriter(excel_file_buffer)
        score_k1_xlsx = export_score_k1_to_excel(klavi_report, pandas_excel_writter)

        workbook = pandas_excel_writter.book

        assert "ScoreK1" in workbook.sheetnames

