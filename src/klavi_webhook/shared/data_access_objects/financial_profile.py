from .base_dao import DynamoDbORM
from boto3.dynamodb.conditions import Key
import os


class FinancialProfileDAO(DynamoDbORM):
    def __init__(self, env: str):
        table_name = "Klavi-FinancialProfile-{env}".format(env=os.getenv("ENV"))
        super().__init__(env, table_name)

    def save(self, document: dict):
        self.put(document)

    def list(self, start_time: int, end_time: int):
        filter_expression = Key('timestamp').between(start_time, end_time)
        return self.scan(self.table_name, filter_expression=filter_expression)
