from dataclasses import dataclass
from marshmallow import Schema, fields
from shared.data_access_objects.transaction_detail import TransactionDetailDAO

@dataclass
class TransactionDetail:
    id: str = ""
    trans_date: str = ""
    trans_amount: str = ""
    trans_currency: str = ""
    trans_description: str = ""
    category: str = ""
    payment_type: str = ""
    charge_identificator: str = ""
    charge_number: str = ""
    balance: str = ""

    def __post_init__(self):
        print("ON POST INIT")
        self.schema = TransactionDetailSchema()

    def save(self):
        dao = TransactionDetailDAO('dev')
        payload = self.schema.dump(self)
        payload['id'] = 'tste'
        payload['category_id'] = 'category_id'
        dao.put(payload)
        print("Object Saved")


class TransactionDetailSchema(Schema):
    id: fields.Str()
    trans_date: fields.Str()
    trans_amount: fields.Str()
    trans_currency: fields.Str()
    trans_description: fields.Str()
    category: fields.Str()
    payment_type: fields.Str()
    charge_identificator: fields.Str()
    charge_number: fields.Str()
    balance: fields.Str()
