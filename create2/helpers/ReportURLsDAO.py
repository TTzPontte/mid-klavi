import boto3
from botocore.exceptions import ClientError


class ReportURLsDAO:
    TABLE_NAME = "ReportURLs"

    def __init__(self, environment):
        self._table_name = f"{self.TABLE_NAME}.{environment}"
        self._dynamodb = boto3.resource("dynamodb")

    def get_item(self, enquiry_cpf: str, report_type: str):
        table = self._dynamodb.Table(self._table_name)
        try:
            response = table.get_item(Key={"enquiry_cpf": enquiry_cpf, "report_type": report_type})
            return response.get("Item")
        except ClientError as e:
            print(f"Error getting item from {self._table_name}: {e.response['Error']['Message']}")

    def put_item(self, item):
        table = self._dynamodb.Table(self._table_name)
        try:
            response = table.put_item(Item=item)
            print(f"Item {item} added to {self._table_name}")
            return response
        except ClientError as e:
            print(f"Error adding item to {self._table_name}: {e.response['Error']['Message']}")
