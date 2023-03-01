import pytest
from moto import mock_dynamodb, mock_s3
import io
import os
import boto3
import sys
import pandas
os.environ["ENV"] = "dev"


sys.path.append("/home/silvio/Workspacecs/Pontte/codebase/mid-klavi/src/klavi_webhook")

from src.klavi_webhook.app import lambda_handler
from ..helpers.dynamodb import create_table


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

event_sample = {
  "body": "{\"code\":200,\"msg\":\"ok\",\"report_time\":\"2022-03-03 12:52:13\",\"data\":{\"enquiry_cpf\":\"12345678901\",\"user_consent\":\"Yes\",\"allow_autoupdate\":\"Yes\",\"connection_key\":\"gPuKXrCJU0kUDQO65J4k\",\"connection_id\":\"f45c899f-11eb-231f-97c4-4b2c16484587\",\"institution_id\":\"033\",\"report_type\":\"liabilities\",\"report_id\":\"4b2c1648-231f-11eb-97c4-f45c899f4592\",\"report_version\":\"V1.1\",\"Liabilities\":[{\"account_holder\":\"JOHN DOE\",\"account_number\":\"01.12345.4\",\"agency_number\":\"1076\",\"bacen_id\":\"033\",\"bacen_name\":\"BANCO SANTANDER (BRASIL) S.A.\",\"bank_name\":\"Santander\",\"cpf_verified\":\"01234567890\",\"days_covered\":180,\"number_of_liability_streams\":1,\"total_liabilities_last_180_days\":17.25,\"total_liabilities_last_30_days\":0,\"total_liabilities_last_60_days\":0,\"total_liabilities_last_90_days\":0,\"liabilityStream\":[{\"liability_stream_type\":\"Credit card\",\"liabilityTransactions\":[{\"trans_date\":\"2021-11-22\",\"trans_amount\":-17.25,\"trans_description\":\"CARTAO CX\"}]}]},{\"account_holder\":\"JOHN DOE\",\"account_number\":\"01.23456.2\",\"agency_number\":\"1076\",\"bacen_id\":\"033\",\"bacen_name\":\"BANCO SANTANDER (BRASIL) S.A.\",\"bank_name\":\"Santander\",\"cpf_verified\":\"01234567890\",\"days_covered\":180,\"number_of_liability_streams\":1,\"total_liabilities_last_180_days\":37.25,\"total_liabilities_last_30_days\":0,\"total_liabilities_last_60_days\":0,\"total_liabilities_last_90_days\":37.25,\"liabilityStream\":[{\"liability_stream_type\":\"Credit card\",\"liabilityTransactions\":[{\"trans_date\":\"2021-12-22\",\"trans_amount\":-37.25,\"trans_description\":\"CARTAO CX\"}]}]}]}}",
  "resource": "/hello",
  "path": "/hello",
  "httpMethod": "GET",
  "isBase64Encoded": False,
  "queryStringParameters": {
    "foo": "bar"
  },
  "pathParameters": {
    "proxy": "/path/to/resource"
  },
  "stageVariables": {
    "baz": "qux"
  },
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "en-US,en;q=0.8",
    "Cache-Control": "max-age=0",
    "CloudFront-Forwarded-Proto": "https",
    "CloudFront-Is-Desktop-Viewer": "true",
    "CloudFront-Is-Mobile-Viewer": "False",
    "CloudFront-Is-SmartTV-Viewer": "False",
    "CloudFront-Is-Tablet-Viewer": "False",
    "CloudFront-Viewer-Country": "US",
    "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Custom User Agent String",
    "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
    "X-Amz-Cf-Id": "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA==",
    "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
    "X-Forwarded-Port": "443",
    "X-Forwarded-Proto": "https"
  },
  "requestContext": {
    "accountId": "123456789012",
    "resourceId": "123456",
    "stage": "prod",
    "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
    "requestTime": "09/Apr/2015:12:34:56 +0000",
    "requestTimeEpoch": 1428582896000,
    "identity": {
      "cognitoIdentityPoolId": None,
      "accountId": None,
      "cognitoIdentityId": None,
      "caller": None,
      "accessKey": None,
      "sourceIp": "127.0.0.1",
      "cognitoAuthenticationType": None,
      "cognitoAuthenticationProvider": None,
      "userArn": None,
      "userAgent": "Custom User Agent String",
      "user": None
    },
    "path": "/prod/hello",
    "resourcePath": "/hello",
    "httpMethod": "POST",
    "apiId": "1234567890",
    "protocol": "HTTP/1.1"
  }
}

sample_context = {
    "accountId": "123456789012",
    "resourceId": "123456",
    "stage": "prod",
    "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
    "requestTime": "09/Apr/2015:12:34:56 +0000",
    "requestTimeEpoch": 1428582896000,
    "identity": {
      "cognitoIdentityPoolId": None,
      "accountId": None,
      "cognitoIdentityId": None,
      "caller": None,
      "accessKey": None,
      "sourceIp": "127.0.0.1",
      "cognitoAuthenticationType": None,
      "cognitoAuthenticationProvider": None,
      "userArn": None,
      "userAgent": "Custom User Agent String",
      "user": None
    },
    "path": "/prod/hello",
    "resourcePath": "/hello",
    "httpMethod": "POST",
    "apiId": "1234567890",
    "protocol": "HTTP/1.1"
  }


class TestKlaviWebhookHandler:

    @mock_dynamodb
    @mock_s3
    def test_can_handler_a_category_checking_request(self):
        create_table("Klavi-LiabilityTransaction-dev", "category_id")
        create_table("Klavi-LiabilityStream-dev", "category_id")
        create_table("Klavi-Liabilities-dev", "report_id")
        create_table("Klavi-KlaviReport-dev", "id")
        create_table("Klavi-EventLogger-dev", "id")
        event = {
            "body": klavi_report_payload
        }
        context = {}
        response = lambda_handler(event_sample, sample_context)
        print("RESPONSE")
        print(response)

        assert response["statusCode"] == 200






