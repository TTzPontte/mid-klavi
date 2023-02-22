from dataclasses import dataclass, field
from typing import Optional

from app.Models.Bank.BankAccount import BankAccount
from app.Models.Transaction import Transaction


@dataclass
class Categorychecking:
    bank: BankAccount
    transactions: Optional[list[Transaction]] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict):
        bank = BankAccount(**data['bank_data'])
        transactions = [Transaction(**trans) for trans in data.get('transactiondetail', [])]
        return cls(bank=bank, transactions=transactions)

