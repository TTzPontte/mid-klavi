"""Definição dos erros."""

from enum import Enum
from http import HTTPStatus

from src.klavi_webhook.helpers.common import handlerbase


class OpErrors(Enum):
    """Lista de errors de operação """
    MINIMUM_AGE = (0x8001, "a idade é menor que a mínima permitida")
    MAXIMUM_AGE = (0x8001, "a idade é maior que a máxima permitida")
    MINIMUM_PROPERTY_VALUE = (0x8001, "o valor do imóvel é menor que o mínimo permitido")
    MINIMUM_LOAN_VALUE = (0x8001, "o valor do emprestimo é menor que o mínimo permitido")
    MAXIMUM_LOAN_VALUE = (0x8001, "o valor do emprestimo é maior que o máximo permitido")


class Errors(Enum):
    """Lista das exceções."""
    UNKNOWN = (HTTPStatus.INTERNAL_SERVER_ERROR, "erro desconhecido")
    RUNTIME = (HTTPStatus.INTERNAL_SERVER_ERROR, "erro desconhecido em execução: {message}")
    PROPERTIES_MISSING = (HTTPStatus.BAD_REQUEST, "as propriedades {properties} não foram enviadas")
    PROPERTY_MISSING = (HTTPStatus.BAD_REQUEST, "a propriedade {property} não foi enviada")
    INCORRECT_FORMAT = (HTTPStatus.BAD_REQUEST, "o formato da propriedade {property} é inválido")
    OPERATION_NOT_SUPPORTED = (HTTPStatus.BAD_REQUEST, "a operação {op} não é suportada")
    ENTITY_NOT_FOUND = (HTTPStatus.BAD_REQUEST, "a entidade {entity} não existe")
    INCORRECT_VALUE = (HTTPStatus.BAD_REQUEST, "o valor do campo {field} não está dentro do permitido")
    INVALID_VALUE = (HTTPStatus.BAD_REQUEST, "o valor do campo {field} é inválido")
    VALUE_ALREADY_EXISTS = (HTTPStatus.UNAUTHORIZED, "o valor do campo {field} já existe no banco de dados")
    COULD_NOT_GET_CEP = (HTTPStatus.INTERNAL_SERVER_ERROR, "não foi possível acessar o cep informado")
    COULD_NOT_FIND_RESOURCE = (HTTPStatus.NOT_FOUND, "O recurso não foi encontrado")
    COULD_NOT_UPDATE_RESOURCE = (HTTPStatus.INTERNAL_SERVER_ERROR, "Não foi possível atualizar os dados do recurso")
    COULD_NOT_CREATE_RESOURCE = (HTTPStatus.INTERNAL_SERVER_ERROR, "Não foi possível criar o recurso no banco de dados")
    COULD_NOT_READ_CITIES = (HTTPStatus.INTERNAL_SERVER_ERROR, "não foi possível ler a lista de cidades atendidas")
    FIELD_NOT_ALLOWED = (HTTPStatus.UNAUTHORIZED, "O(s) campo(s) {fields} não pode(m) ser inserido(s)")
    FORBIDDEN = (HTTPStatus.UNAUTHORIZED, "Voce nao tem permissao para acessar este recurso")
    LOAN_VALUE_LESS_MINIMUM = (HTTPStatus.BAD_REQUEST, "O valor do empréstimo é menor que o mínimo")
    LOAN_VALUE_MORE_MAXIMUM = (HTTPStatus.BAD_REQUEST, "O valor do empréstimo é maior que o máximo")
    REALTY_VALUE_LESS_MINIMUM = (HTTPStatus.BAD_REQUEST, "O valor do imóvel é menor que o mínimo")
    AGE_LESS_MINIMUM = (HTTPStatus.BAD_REQUEST, "A idade é menor que o mínimo")
    AGE_MORE_MAXIMUM = (HTTPStatus.BAD_REQUEST, "A idade é maior que o máximo")
    GROSS_VALUE_NOT_CONVERGED = (HTTPStatus.INTERNAL_SERVER_ERROR, "Cálculo do valor bruto não convergiu")
    NET_VALUE_NOT_CONVERGED = (HTTPStatus.INTERNAL_SERVER_ERROR, "Cálculo do valor do empréstimo líquido não convergiu")
    IRR_VALUE_NOT_CONVERGED = (HTTPStatus.INTERNAL_SERVER_ERROR, "Cálculo da taxa interna de retorno não convergiu")
    INVALID_TEO_RANGE_ITEM = (HTTPStatus.INTERNAL_SERVER_ERROR, "Valor do item do TEO é inválido: {item}")
    GRACE_PERIOD_NOT_IN_RANGE = (HTTPStatus.BAD_REQUEST, "A carência não está na faixa permitida")
    INVALID_SKIP_INSTALLMENT_MONTH = (HTTPStatus.BAD_REQUEST, "O mês para pular é inválido")
    INVALID_DATE_FORMAT = (HTTPStatus.BAD_REQUEST, "Formato da data inválida em {field}")
    SIMULATION_NOT_CONVERGED = (HTTPStatus.INTERNAL_SERVER_ERROR, "Simulação não convergiu")
    SKIP_INSTALLMENT_MAX_ITERATIONS_NOT_CONFIGURED = (HTTPStatus.INTERNAL_SERVER_ERROR, "Quantidade máxima de "
                                                                                        "iterações para pular parcela "
                                                                                        "não configurada")
    INCORRECT_TABLE = (HTTPStatus.BAD_REQUEST, "não realizamos o cálculo da tabela: {table}")
    INCORRECT_AMORTIZATION = (HTTPStatus.BAD_REQUEST, "não realizamos o cálculo da amortization: {amortization}")
    EMAIL_NOT_SENT = (HTTPStatus.INTERNAL_SERVER_ERROR,  "Não foi possivel enviar email para: {to_email}")


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

        answer = {
            "statusCode": self.status_code.value,
            "error": {
                "code": self.code,
                "message": self.message,
            }
        }

        if self.original_exception:
            answer["error"]["type"] = type(self.original_exception).__name__
            answer["error"]["exception"] = str(self.original_exception)

        return handlerbase.Result(status_code=self.status_code.value,
                                         obj=answer)
