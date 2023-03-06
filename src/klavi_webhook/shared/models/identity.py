from dataclasses import dataclass, field
from marshmallow import Schema

import marshmallow_dataclass
import uuid
import decimal

@dataclass
class Identity:
    id: str = ""
    report_id: str = ""
    account_number: str = ""
    agency_number: str = ""
    bacen_id: str = ""
    bacen_name: str = ""
    bank_name: str = ""
    cpf_verified: str = ""
    name: str = ""
    cellphone: str = ""
    email: str = ""
    correspondence_address: dict = field(default_factory=dict)

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()

IdentitySchema = marshmallow_dataclass.class_schema(Identity)
