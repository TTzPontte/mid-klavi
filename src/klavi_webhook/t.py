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


class SendCreateUserEmailFn(Handler):  # pylint: disable=too-few-public-methods
    def pre_process(self):
        if self.event["body"]:
            self.event["body"] = json.loads(self.event["body"])

    def validate(self):
        helper.validate(
            props=["to_email", "contractId", "contractEvent"],
            validation_obj=self.event["body"]
        )

    def handler(self):
        body = self.event['body']

        try:
            signup_dao = SignUpDao()
            uuid = signup_dao.create(contract_id)
            send_email_create_user(to_email, uuid)
            return Result(HTTPStatus.OK, {"message": "Email successfully sent"})
        except Exception:
            raise AppException(Errors.EMAIL_NOT_SENT, email_recipient=str(to_email))


def handler(event, context):
    logger.debug("Event: %s", event)

    return SendCreateUserEmailFn(event, context).run()
