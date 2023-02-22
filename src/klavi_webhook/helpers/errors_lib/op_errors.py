from enum import Enum


class OpErrors(Enum):
    """Lista de errors_lib de operação """
    MINIMUM_AGE = (0x8001, "a idade é menor que a mínima permitida")
    MAXIMUM_AGE = (0x8001, "a idade é maior que a máxima permitida")
    MINIMUM_PROPERTY_VALUE = (0x8001, "o valor do imóvel é menor que o mínimo permitido")
    MINIMUM_LOAN_VALUE = (0x8001, "o valor do emprestimo é menor que o mínimo permitido")
    MAXIMUM_LOAN_VALUE = (0x8001, "o valor do emprestimo é maior que o máximo permitido")
