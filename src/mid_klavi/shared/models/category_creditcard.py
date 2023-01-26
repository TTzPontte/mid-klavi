from dataclasses import dataclass
import marshmallow_dataclass
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

CategoryCreditCardSchema = marshmallow_dataclass.class_schema(CategoryCreditCard)


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

OpenStatementSchema = marshmallow_dataclass.class_schema(OpenStatement)


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

ClosedStatementSchema = marshmallow_dataclass.class_schema(ClosedStatement)

