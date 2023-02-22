from marshmallow_dataclass import dataclass

from Models.Bank import Transaction, Bankaccount


@dataclass
class Incomestream:
    first_income_day: str
    second_income_day: str
    income_transactions: list[Transaction]
    income_stream_type: str


@dataclass
class Income:
    bank: Bankaccount
    days_covered: int
    number_of_income_streams: int
    total_income_last_180_days: int
    total_income_last_30_days: int
    total_income_last_60_days: int
    total_income_last_90_days: int
    income_stream: list[Incomestream]

