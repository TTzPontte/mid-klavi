from .base_dao import DynamoDbORM
from boto3.dynamodb.conditions import Key
import os


class IdentityDAO(DynamoDbORM):
    def __init__(self):
        env = os.getenv("ENV")
        table_name = "Klavi-Identity-{env}".format(env=env)
        super().__init__(env, table_name)
