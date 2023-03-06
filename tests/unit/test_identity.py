import pytest
from moto import mock_dynamodb
import io
import os
import boto3
import sys
import pandas
os.environ["ENV"] = "dev"


sys.path.append("/home/silvio/Workspacecs/Pontte/codebase/mid-klavi/src/klavi_webhook")

from src.klavi_webhook.shared.models.identity import Identity
from src.klavi_webhook.shared.parsers.identity import parse_identity_payload_body
from src.klavi_webhook.shared.factory.identity import build_identity_from_kavli_payload
from src.klavi_webhook.shared.repository.identity import IdentityRepository
from src.klavi_webhook.shared.exports.identity import export_identity_to_excel
from src.klavi_webhook.shared.factory.klavi_report import build_report_from_klavi_payload


from ..helpers.mocked_payloads import identity_payload
from ..helpers.dynamodb import create_identity_tables



class TestIdentity:

    def test_parser_identity_body(self):
        body_payload = identity_payload["data"]["identity"]
        objects_to_test = []
        parsed_data = parse_identity_payload_body(body_payload)
        objects_to_test.append(Identity(**parsed_data))

        assert objects_to_test[0].email == body_payload["email"]


    def test_create_a_full_identity_instance_from_payload(self):
        body_payload = identity_payload["data"]["identity"]
        objects_to_test = []

        identity_instance = build_identity_from_kavli_payload(body_payload)
        objects_to_test.append(identity_instance)

        assert objects_to_test[0].email == body_payload["email"]

    @mock_dynamodb
    def test_save_identity_into_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        create_identity_tables()
        body_payload = identity_payload["data"]["identity"]
        identity_repository = IdentityRepository()
        objects_to_test = []

        identity_instance = build_identity_from_kavli_payload(body_payload)
        identity_instance.report_id = "some id"
        objects_to_test.append(identity_instance)

        identity_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-Identity-dev"
        )


        assert objects_to_test[0].email == body_payload["email"]
        assert len(saved_objects["Items"]) == 1

    @mock_dynamodb
    def test_get_identity_from_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")

        create_identity_tables()
        body_payload = identity_payload["data"]["identity"]
        identity_repository = IdentityRepository()
        objects_to_test = []

        identity_instance = build_identity_from_kavli_payload(body_payload)
        identity_instance.report_id = "some id"
        objects_to_test.append(identity_instance)

        identity_repository.save(objects_to_test[0])

        retrieved_identity = identity_repository.getByReportId({'id': str(objects_to_test[0].id), 'report_id': objects_to_test[0].report_id})

        assert objects_to_test[0].email == body_payload["email"]

        assert retrieved_identity.email == body_payload["email"]

    def test_export_identity_to_excel(self):
        body_payload = identity_payload["data"]
        klavi_report = build_report_from_klavi_payload(identity_payload)
        excel_file_buffer = io.BytesIO()
        pandas_excel_writter = pandas.ExcelWriter(excel_file_buffer)
        identity_xlsx = export_identity_to_excel(klavi_report, pandas_excel_writter)

        workbook = pandas_excel_writter.book

        assert "Identity" in workbook.sheetnames

