import logging
from typing import Optional, Dict

import boto3
import os
table_name = os.getenv('EVENT_TABLE')

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
