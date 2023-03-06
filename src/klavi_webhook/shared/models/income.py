from dataclasses import dataclass, field
from marshmallow import Schema

import marshmallow_dataclass
import uuid

@dataclass
class Income:
    id: str = ""
    report_id: str = ""
    account_holder: str = ""
    account_number: str = ""
    agency_number: str = ""
    bacen_id: str = ""
    bacen_name: str = ""
    bank_name: str = ""
    cpf_verified: str = ""
    days_covered: str = ""
    number_of_income_streams: str = ""
    total_income_last_180_days: str = ""
    total_income_last_30_days: str = ""
    total_income_last_60_days: str = ""
    total_income_last_90_days: str = ""
    income_streams: list = field(default_factory=list)

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()

class BaseIncomeSchema(Schema):
    class Meta:
        exclude = ('income_streams', )


IncomeSchema = marshmallow_dataclass.class_schema(Income, base_schema=BaseIncomeSchema)


@dataclass
class IncomeStream:
    id: str = ""
    category_id: str = ""
    income_stream_type: str = ""
    income_day: dict = field(default_factory=dict)
    income_transactions: list = field(default_factory=list)

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()

class BaseIncomeStreamSchema(Schema):
    class Meta:
        exclude = ('income_transactions', )


IncomeStreamSchema = marshmallow_dataclass.class_schema(IncomeStream, base_schema=BaseIncomeStreamSchema)



@dataclass
class IncomeTransaction:
    id: str = ""
    category_id: str = ""
    trans_date: str = ""
    trans_amount: str = ""
    trans_description: str = ""

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()


IncomeTransactionSchema = marshmallow_dataclass.class_schema(IncomeTransaction)
