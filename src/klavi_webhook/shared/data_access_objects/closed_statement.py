from .base_dao import DynamoDbORM
from boto3.dynamodb.conditions import Key
import os

class ClosedStatementDAO(DynamoDbORM):
    def __init__(self):
        env = os.getenv("ENV")
        table_name = "Klavi-ClosedStatement-{env}".format(env=env)
        super().__init__(env, table_name)
