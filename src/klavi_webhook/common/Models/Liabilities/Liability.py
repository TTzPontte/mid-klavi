from dataclasses import dataclass
from typing import List

from Models.Bank import Bankaccount


@dataclass
class LiabilityTransactions:
    liability_stream_type: str
    trans_date: str
    trans_amount: float
    trans_description: str


@dataclass
class Liabilities:
    bank: Bankaccount
    days_covered: int
    number_of_liability_streams: int
    total_liabilities_last_180_days: float
    total_liabilities_last_30_days: float
    total_liabilities_last_60_days: float
    total_liabilities_last_90_days: float
    liabilitystream: List[LiabilityTransactions]

