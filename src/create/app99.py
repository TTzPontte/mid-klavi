import json
import logging
from dataclasses import dataclass
from http import HTTPStatus
from typing import Dict, Optional, List
from urllib.parse import urljoin

import boto3
from botocore.exceptions import ClientError
from common.handlerbase import Handler, Result

from helpers.Models.Payload import Parser
from helpers.email_helper.validate_payload import validate_payload

# ENV = os.getenv('ENV')
ENV = 'staging'
BUCKET_NAME = "openfinance-dev"
REPORT_TYPES = ["category_checking", "income"]
HE_BACEM_PHASE_ID = "319165329"
FI_BACEM_PHASE_ID = "319165324"


@dataclass
class S3Helper:
    enquiry_cpf: str
    report_type: str
    BUCKET_NAME: str = BUCKET_NAME
    s3_client = boto3.client("s3")
    json_report_url: Optional[str] = None
    xlsx_report_url: Optional[str] = None

    def __post_init__(self):
        self.json_key = f"{self.enquiry_cpf}/{self.report_type}.json"
        self.xlsx_key = f"{self.enquiry_cpf}/{self.report_type}.xlsx"
        self.json_report_url = self._build_report_url(self.json_key)
        self.xlsx_report_url = self._build_report_url(self.xlsx_key)

    def _build_report_url(self, key: str) -> str:
        base_url = f"https://s3.amazonaws.com/{self.BUCKET_NAME}"
        return urljoin(base_url, key)

    def save_to_s3(self, body, bucket_name, key):
        """Save data to S3."""
        try:
            self.s3_client.put_object(Body=body, Bucket=bucket_name, Key=key)
        except ClientError as e:
            logging.error(e)
            raise RuntimeError(f"Failed to save data to S3. Bucket: {bucket_name}, Key: {key}")

    def list_files_in_s3_bucket(self, enquiry_cpf: str, report_types: List[str]) -> List[str]:
        files = []
        for report_type in report_types:
            prefix = f"{enquiry_cpf}/{report_type}"
            response = self.s3_client.list_objects_v2(Bucket=self.BUCKET_NAME, Prefix=prefix)
            if 'Contents' in response:
                files.append(response['Contents'])
        return files

    def count_files_in_s3_bucket(self, enquiry_cpf: str, report_types: List[str]) -> Dict[str, int]:
        file_counts = {report_type: 0 for report_type in report_types}
        for report_type in report_types:
            prefix = f"{enquiry_cpf}/{report_type}"
            response = self.s3_client.list_objects_v2(Bucket=self.BUCKET_NAME, Prefix=prefix)
            if 'Contents' in response:
                file_counts[report_type] = len(response['Contents'])
            else:
                file_counts[report_type] = 0
        return file_counts


class ReportURLsDAO:
    TABLE_NAME: str = "ReportURLs"

    def __init__(self, environment: str):
        self.environment = environment
        self.table_name = f"{self.TABLE_NAME}.{self.environment}"
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(self.table_name)

    def get_item(self, enquiry_cpf: str, report_type: str) -> Optional[Dict[str, str]]:
        try:
            key = {"enquiry_cpf": enquiry_cpf}
            response = self.table.get_item(Key=key)
            return response.get("Item")
        except Exception as e:
            logging.error(f"Error retrieving report URLs from {self.table_name}: {e}")

    def get_items(self, attribute_value: str) -> Dict[str, str]:
        try:
            response = self.table.query(KeyConditionExpression='enquiry_cpf = :cpf',
                                        ExpressionAttributeValues={':cpf': attribute_value})
            items = response['Items']
            return items
        except Exception as e:
            logging.error(f"Error retrieving report URLs from {self.table_name}: {e}")

    def put_item(self, report_urls: Dict[str, str]) -> Optional[Dict[str, str]]:
        try:
            self.table.put_item(Item=report_urls)
            return report_urls
        except Exception as e:
            logging.error(f"Error saving report URLs to {self.table_name}: {e}")


class OpenFinanceCreate(Handler):
    def pre_process(self):
        if isinstance(self.event["body"], str):
            self.event["body"] = json.loads(self.event["body"])
        if "query_param" in self.event["body"]:
            del self.event["body"]["query_param"]

    def validate(self) -> Result:
        error = validate_payload(self.event['body'])
        if error:
            return Result(HTTPStatus.BAD_REQUEST, error)

    def handler(self):
        body = self.event["body"]
        if "query_param" in body:
            del body["query_param"]

        data = body.get("data")
        enquiry_cpf = data.get("enquiry_cpf")
        report_type = data.get("report_type", "").lower()

        if report_type in REPORT_TYPES:
            s3_helper = S3Helper(enquiry_cpf=enquiry_cpf, report_type=report_type)

            parser = Parser(**body)
            parser.generate_report(report_type, s3_helper.xlsx_report_url)

            dao = ReportURLsDAO(environment=ENV)
            existing_item = dao.get_items(enquiry_cpf)
            print("existing item", existing_item)
            report_urls = {"enquiry_cpf": enquiry_cpf, "json_report_url": s3_helper.json_report_url,
                           "xlsx_report_url": s3_helper.xlsx_report_url, 'report_type': report_type}

            if existing_item:
                existing_item["other_json_report_url"] = s3_helper.json_report_url
                existing_item["other_xlsx_report_url"] = s3_helper.xlsx_report_url
                result = dao.put_item(existing_item)
            else:
                result = dao.put_item(report_urls)
        print('result', result)

        return Result(HTTPStatus.OK, result)


def handler(event, context):
    return OpenFinanceCreate(event, context).run()
