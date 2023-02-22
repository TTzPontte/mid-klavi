from dataclasses import dataclass, field
from marshmallow import Schema
import marshmallow_dataclass
import uuid


@dataclass
class CategoryCreditCard:
    id: str = ""
    report_id: str = ""
    bank_name: str = ""
    bacen_name: str = ""
    bacen_id: str = ""
    card_last4num: str = ""
    cpf_verified: str = ""
    holder_name: str = ""
    card_type: str = ""
    credit_limit: str = ""
    available_limit: str = ""
    agency_number: str = ""
    bank_account: str = ""
    is_active: str = ""
    is_vip: str = ""
    open_statement: dict = field(default_factory=dict)
    closed_statements: list = field(default_factory=list)

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()


class BaseCreditCardSchema(Schema):
    class Meta:
        exclude = ('open_statement', 'closed_statements')


CategoryCreditCardSchema = marshmallow_dataclass.class_schema(CategoryCreditCard, base_schema=BaseCreditCardSchema)


@dataclass
class OpenStatement:
    id: str = ""
    category_id: str = ""
    bill_amount: str = ""
    due_date: str = ""
    billing_date: str = ""
    bill_month: str = ""
    category_id: str = ""
    transaction_details: list = field(default_factory=list)

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()

class BaseSchemaStatement(Schema):
    class Meta:
        exclude = ('transaction_details', )


OpenStatementSchema = marshmallow_dataclass.class_schema(OpenStatement, base_schema=BaseSchemaStatement)


@dataclass
class ClosedStatement:
    id: str = ""
    category_id: str = ""
    billing_date: str = ""
    bill_month: str = ""
    bill_amount: str = ""
    minimum_payment: str = ""
    payment_date: str = ""
    payment_amount: str = ""
    transaction_details: list = field(default_factory=list)

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()


ClosedStatementSchema = marshmallow_dataclass.class_schema(ClosedStatement, base_schema=BaseSchemaStatement)
