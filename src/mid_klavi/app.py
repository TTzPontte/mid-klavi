from http import HTTPStatus
from shared.helpers.handler_base import Handler, Result
from shared.helpers.hw_helper import helper_fn
from shared.repository.event_logger import EventLoggerRepository
from shared.factory.event_logger import build_event_logger_from_klavi_payload
from shared.parsers.event_logger import parse_payload_into_logger_object
import json
import io
import boto3
s3client = boto3.client('s3')


class MidKlavi(Handler):
    body: str

    def pre_process(self):
        if self.event['body']:
            self.body = json.loads(self.event['body'])

    def log_request(self):
        event_logger = build_event_logger_from_klavi_payload(self.body)
        event_logger_repository = EventLoggerRepository()
        event_logger_repository.save(event_logger)

        return event_logger

    def handler(self):
        log = self.log_request()

        return Result(HTTPStatus.OK, {"id": str(log.id)})


def lambda_handler(event, context):
    helper_fn()
    return MidKlavi(event, context).run()
