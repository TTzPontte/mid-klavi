from dataclasses import dataclass, field
from marshmallow import Schema

import marshmallow_dataclass
import uuid
import decimal

@dataclass
class Balance:
    id: str = ""
    report_id: str = ""
    account_holder: str = ""
    account_number: str = ""
    account_type: str = ""
    agency_number: str = ""
    bacen_id: str = ""
    bacen_name: str = ""
    bank_name: str = ""
    cpf_verified: str = ""
    available_limit: decimal.Decimal = 0.0
    total_limit: decimal.Decimal = 0.0
    current_balance: decimal.Decimal = 0.0

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()

BalanceSchema = marshmallow_dataclass.class_schema(Balance)
