import decimal
import json
from dataclasses import dataclass
from http import HTTPStatus


class CustomEncoder(json.JSONEncoder):
    """Codificador para o JSON.

    Transforma o Decimal em números.
    """

    def default(self, o):  # pylint: disable=E0202
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            return int(o)
        return super(CustomEncoder, self).default(o)


@dataclass
class Result():
    """Classe para indicação do resultado."""

    status_code: HTTPStatus
    obj: dict

    def answer(self) -> object:
        """Retorna o resultado para o API Gateway.

        Returns:
            Objeto com as informações que o API Gateway aguarda.
        """
        data = {"statusCode": self.status_code,
            "headers": {"Cache-Control": "no-cache, no-store, must-revalidate", "Pragma": "no-cache", "Expires": "0",
                "Access-Control-Allow-Origin": "*", }}

        if self.obj:
            data["body"] = json.dumps(self.obj, cls=CustomEncoder)
            data["headers"]["Content-Type"] = "application/json"

        return data
