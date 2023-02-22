from dataclasses import dataclass


@dataclass
class Transaction:
    date: str
    amount: float
    description: str
    balance: float
    category: str
