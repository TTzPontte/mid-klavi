"""Objetos base para os handlers."""
import logging

from aws_xray_sdk.core import patch_all
from aws_xray_sdk.core import xray_recorder

from .config import Config
from .errors_lib.app_exception import AppException
from .errors_lib.error import Errors
from .result import Result

xray_recorder.configure(service='Portal')
patch_all()


config = Config()

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name
logger.setLevel(config.LOGGING_LEVEL)


def convert_header_lowercase(event: object):
    """Converte os nomes dos cabeçalhos para minúsculo.

    Args:
        event: o evento recebido do API Gateway.
    """

    if "headers" in event:
        headers = {k.lower(): v for k, v in event["headers"].items()}
        event["headers"] = headers

    if "multiValueHeaders" in event:
        headers = {k.lower(): v for k, v in event["multiValueHeaders"].items()}
        event["multiValueHeaders"] = headers


class Handler():
    """Realiza o tratamento do evento do API Gateway"""

    def __init__(self, event, context):
        """Inicializa a classe de tratamento.

        Args:
            event: o evento recebido do API Gateway.
            context: o contexto recebido do API Gateway.
        """

        self._event = event
        convert_header_lowercase(self._event)

        self._context = context

    @property
    def event(self) -> object:
        """Retorna o evento do Handler.

        Returns:
            O evento recebido do API Gateway já tratado.
        """
        return self._event

    def aws_local_preprocess(self):
        """Realiza o pré processamento se estiver rodando em DEV."""

    def pre_process(self):
        """Realiza o pré processamento das informações."""

    def check_authorization(self):
        """Valida a autorização."""

    def validate(self):
        """Valida as informações enviadas"""

    def handler(self) -> Result:
        """Execução do handler do evento."""
        raise NotImplementedError()

    def run(self):
        """Executa o handler."""

        if config.AWS_SAM_LOCAL:
            print("AWS_SAM_LOCAL: %s", config.AWS_SAM_LOCAL)

        try:
            if config.AWS_SAM_LOCAL:
                self.aws_local_preprocess()

            self.pre_process()

            if not config.AWS_SAM_LOCAL:
                self.check_authorization()

            self.validate()

            res = self.handler()

            if not isinstance(res, Result):
                raise TypeError("handler result is not a Result")

            return res.answer()

        except AppException as err:
            logger.error("execution exception received: %s", err, exc_info=1)
            res = err.as_result()
        except Exception as err:  # pylint: disable=broad-except
            logger.critical("exception received: %s", err, exc_info=1)
            res = AppException(Errors.UNKNOWN).as_result()
        else:
            logger.critical("code did not return")
            res = errors.AppException(errors.Errors.RUNTIME,
                                      message="code did not return").as_result()

        return res.answer()
