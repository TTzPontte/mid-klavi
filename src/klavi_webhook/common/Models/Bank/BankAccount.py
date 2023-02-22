from dataclasses import dataclass
from typing import Optional


@dataclass
class BankAccount:
    id: Optional[str] = None
    bank_name: Optional[str] = None
    bacen_name: Optional[str] = None
    branch: Optional[str] = None
    bacen_id: Optional[str] = None
    cpf_verified: Optional[str] = None
    holder_name: Optional[str] = None
    operation_code: Optional[str] = None
    balance: Optional[float] = None
    number: Optional[float] = None
    bank_id: Optional[str] = None
