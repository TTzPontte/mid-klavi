from .error import Errors
from ..result import Result


class AppException(Exception):
    """Definição das exceções da aplicação.

    Todas as exceções devem ser derivadas desta.
    """

    def __init__(self, error: Errors, exc: Exception = None, **kwargs):
        """Inicializa o erro.

        Args:
            error: o código do erro.
            exc: a exceção original que causou esta exceção (opcional).
            ..: os argumentos são de acordo com o esperado em cada mensagem de erro.
        """
        self.code = error.name
        self.status_code, template = error.value

        try:
            self.message = template.format(**kwargs)
        except KeyError:
            self.message = template

        self.original_exception = exc

        super().__init__(self.message)

    def as_result(self):
        """Retorna a exceção como um resultado para o API Gateway."""

        answer = {"statusCode": self.status_code.value, "error": {"code": self.code, "message": self.message, }}

        if self.original_exception:
            answer["error"]["type"] = type(self.original_exception).__name__
            answer["error"]["exception"] = str(self.original_exception)

        return Result(status_code=self.status_code.value, obj=answer)
