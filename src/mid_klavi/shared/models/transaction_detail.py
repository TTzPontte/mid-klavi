from dataclasses import dataclass
import marshmallow_dataclass
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

TransactionDetailSchema = marshmallow_dataclass.class_schema(TransactionDetail)

