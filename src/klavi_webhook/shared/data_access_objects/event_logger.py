from .base_dao import DynamoDbORM
from boto3.dynamodb.conditions import Key
import os


class EventLoggerDAO(DynamoDbORM):
    def __init__(self, env):
        table_name = "Klavi-EventLogger-{env}".format(env=os.getenv("ENV"))
        super().__init__(env, table_name)

    def log_event(self, event: dict):
        self.put(event)

    def get_logs(self, start_time: int, end_time: int):
        filter_expression = Key('timestamp').between(start_time, end_time)
        return self.scan(self.table_name, filter_expression=filter_expression)
