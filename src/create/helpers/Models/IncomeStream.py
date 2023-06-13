from dataclasses import dataclass
from typing import List


@dataclass
class IncomeStream:
    income_day: dict
    income_transactions: List[dict]
    income_stream_type: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(income_day=data["incomeDay"], income_transactions=data["incomeTransactions"],
                   income_stream_type=data["income_stream_type"])

    def to_dict(self):
        return {"incomeDay": self.income_day, "incomeTransactions": self.income_transactions,
                "income_stream_type": self.income_stream_type}
