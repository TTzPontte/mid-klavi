from .base_dao import DynamoDbORM
from boto3.dynamodb.conditions import Key


class LiabilityTransactionDAO(DynamoDbORM):
    def __init__(self, env: str):
        super().__init__(env, 'LiabilityTransaction')

    def list(self, start_time: int, end_time: int):
        filter_expression = Key('timestamp').between(start_time, end_time)
        return self.scan(self.table_name, filter_expression=filter_expression)
