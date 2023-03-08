from .base_dao import DynamoDbORM
from .category_checking import CategoryCheckingDAO
from boto3.dynamodb.conditions import Key
import os


class KlaviReportDAO(DynamoDbORM):
    def __init__(self):
        env = os.getenv("ENV")
        table_name = "Klavi-KlaviReport-{env}".format(env=env)
        super().__init__(env, table_name)

    def save(self, klavi_report: dict):
        self.put(klavi_report.to_json())

        category_checking_dao = CategoryCheckingDAO()

        for category_checking in klavi_report.category_checkings:
            category_checking_dao.put(category_checking.to_json())
