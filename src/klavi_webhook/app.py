"""Simulador.Simulate

Realiza simulação de emprestimo.
"""
import json
import logging
from http import HTTPStatus

from src.klavi_webhook.helpers import common
from src.klavi_webhook.helpers.common.errors import AppException, Errors
from src.klavi_webhook.helpers.common.handlerbase import Handler, Result

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name
logger.setLevel(common.config.LOGGING_LEVEL)


class CreateFn(Handler):  # pylint: disable=too-few-public-methods
    def pre_process(self):
        if self.event["body"]:
            self.event["body"] = json.loads(self.event["body"])

    def validate(self):
        pass

    def handler(self):
        body = self.event['body']

        try:
            pass
            return Result(HTTPStatus.OK, {"message": "hello world"})
        except Exception:
            raise AppException(Errors.EMAIL_NOT_SENT, email_recipient=str(to_email))


def lambda_handler(event, context):
    logger.debug("Event: %s", event)

    return CreateFn(event, context).run()
