from .base_dao import DynamoDbORM
from boto3.dynamodb.conditions import Key
import os


class CategoryCreditCardDAO(DynamoDbORM):
    def __init__(self):
        env = os.getenv("ENV")
        table_name = "Klavi-CategoryCreditCard-{env}".format(env=env)
        super().__init__(env, table_name)

    def save(self, document: dict):
        self.put(document)
