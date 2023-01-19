from dataclasses import dataclass
from marshmallow import Schema, fields
from shared.data_access_objects.category_creditcard import CategoryCreditCardDAO
from shared.data_access_objects.open_statement import OpenStatementDAO
from shared.data_access_objects.closed_statement import ClosedStatementDAO




@dataclass
class CategoryCreditCard:
    id: str = ""
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

    def __post_init__(self):
        print("ON POST INIT")
        self.schema = CategoryCreditCardSchema()

    def save(self):
        dao = CategoryCreditCardDAO('dev')
        payload = self.schema.dump(self)
        payload['id'] = 'meuid'
        payload['report_id'] = "category_id"
        dao.save(payload)
        print("Object Saved")


class CategoryCreditCardSchema(Schema):
    id: fields.Str()
    bank_name: fields.Str()
    bacen_name: fields.Str()
    bacen_id: fields.Str()
    card_last4num: fields.Str()
    cpf_verified: fields.Str()
    holder_name: fields.Str()
    card_type: fields.Str()
    credit_limit: fields.Str()
    available_limit: fields.Str()
    agency_number: fields.Str()
    bank_account: fields.Str()
    is_active: fields.Str()
    is_vip: fields.Str()


@dataclass
class OpenStatement:
    id: str = ""
    bill_amount: str = ""
    due_date: str = ""
    billing_date: str = ""
    bill_month: str = ""

    def __post_init__(self):
        print("ON POST INIT")
        self.schema = OpenStatementSchema()

    def save(self):
        dao = OpenStatementDAO('dev')
        payload = self.schema.dump(self)
        payload['id'] = 'meuid'
        payload['category_id'] = "category_id"
        dao.save(payload)


class OpenStatementSchema(Schema):
    id: fields.Str()
    bill_amount: fields.Str()
    due_date: fields.Str()
    billing_date: fields.Str()
    bill_month: fields.Str()


@dataclass
class ClosedStatement:
    id: str = ""
    billing_date: str = ""
    bill_month: str = ""
    bill_amount: str = ""
    minimum_payment: str = ""
    payment_date: str = ""
    payment_amount: str = ""

    def __post_init__(self):
        print("ON POST INIT")
        self.schema = ClosedStatementSchema()

    def save(self):
        dao = ClosedStatementDAO('dev')
        payload = self.schema.dump(self)
        payload['id'] = 'meuid'
        payload['category_id'] = "category_id"
        dao.save(payload)


class ClosedStatementSchema(Schema):
    id: fields.Str()
    billing_date: fields.Str()
    bill_month: fields.Str()
    bill_amount: fields.Str()
    minimum_payment: fields.Str()
    payment_date: fields.Str()
    payment_amount: fields.Str()
