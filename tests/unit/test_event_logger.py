import pytest
from moto import mock_dynamodb
import io
import os
import boto3
import sys
import pandas
os.environ["ENV"] = "dev"


sys.path.append("/home/silvio/Workspacecs/Pontte/codebase/mid-klavi/src/klavi_webhook")

from src.klavi_webhook.shared.models.event_logger import EventLogger
from src.klavi_webhook.shared.parsers.event_logger import parse_payload_into_logger_object
from src.klavi_webhook.shared.factory.event_logger import build_event_logger_from_klavi_payload
from src.klavi_webhook.shared.repository.event_logger import EventLoggerRepository
from src.klavi_webhook.shared.factory.klavi_report import build_report_from_klavi_payload

#from src.klavi_webhook.shared.factory.category_creditcard import build_category_creditcard_from_kavli_payload
#from src.klavi_webhook.shared.repository.category_creditcard import CategoryCreditCardRepository
#from src.klavi_webhook.shared.parsers.category_creditcard import parse_credit_card_payload_body, parse_credit_card_payload_open_statement, parse_credit_card_payload_closed_statement
#from src.klavi_webhook.shared.models.category_creditcard import CategoryCreditCard, OpenStatement, ClosedStatement

event_payload = {
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

class TestEventLogger:

    def test_parser_payload_into_report(self):
        objects_to_test = []
        parsed_data = parse_payload_into_logger_object(event_payload)
        objects_to_test.append(EventLogger(**parsed_data))

        assert len(objects_to_test) == 1
        assert objects_to_test[0].institution_id == event_payload["data"]["institution_id"]


    def test_create_a_full_event_logger_instance_from_payload(self):
        body_payload = event_payload["data"]["Category_checking"]
        objects_to_test = []

        event_logger_instance = build_event_logger_from_klavi_payload(event_payload)
        objects_to_test.append(event_logger_instance)

        assert len(objects_to_test) == 1
        assert objects_to_test[0].institution_id == event_payload["data"]["institution_id"]

    @mock_dynamodb
    def test_save_event_logger_into_database(self):
        conn = boto3.resource("dynamodb", region_name="us-east-1")
        client = boto3.client("dynamodb")
        table_args = {
            "TableName": "Klavi-EventLogger-dev",
            'KeySchema': [
                {'AttributeName': 'id', 'KeyType': 'HASH'},
            ],
            'AttributeDefinitions': [
                {'AttributeName': 'id', 'AttributeType': 'S'}
            ],
            'ProvisionedThroughput': {
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        }
        conn.create_table(**table_args)

        event_logger_repository = EventLoggerRepository()
        objects_to_test = []

        event_instance = build_event_logger_from_klavi_payload(event_payload)
        event_instance.report_id = "some-item"
        objects_to_test.append(event_instance)

        event_logger_repository.save(objects_to_test[0])

        saved_objects = client.scan(
            TableName="Klavi-EventLogger-dev"
        )


        assert len(objects_to_test) == 1
        assert objects_to_test[0].institution_id == event_payload["data"]["institution_id"]
        assert len(saved_objects["Items"]) == 1
