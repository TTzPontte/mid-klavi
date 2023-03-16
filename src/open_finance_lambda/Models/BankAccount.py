from dataclasses import dataclass, asdict
from typing import Optional, Dict


@dataclass
class BankAccount:
    bank_name: Optional[str] = None
    bacen_name: Optional[str] = None
    bacen_id: Optional[str] = None
    balance: Optional[float] = None
    cpf_verified: Optional[str] = None
    holder_name: Optional[str] = None
    bank_branch: Optional[str] = None
    account: Optional[str] = None
    account_number: Optional[str] = None
    agency_number: Optional[str] = None

    @classmethod
    def from_dict(cls, payload: Dict[str, str]):
        return cls(holder_name=payload.get("account_holder"), account_number=payload.get("account_number"),
                   agency_number=payload.get("agency_number"), bacen_id=payload.get("bacen_id"),
                   bacen_name=payload.get("bacen_name"), bank_name=payload.get("bank_name"),
                   cpf_verified=payload.get("cpf_verified"), )

    def to_dict(self):
        return asdict(self)


@dataclass
class Transaction:
    trans_date: str
    trans_amount: float
    trans_description: str
    category: str
    balance: Optional[float] = None

    def to_dict(self):
        return asdict(self)
