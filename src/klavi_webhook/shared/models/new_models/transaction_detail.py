from dataclasses import dataclass
import marshmallow_dataclass
import uuid
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
    category_id: str = ""

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()

    def to_json(self):
        schema = TransactionDetailSchema()
        print("KCETA")
        print(self)
        return schema.dump(self)

    @classmethod
    def from_payload(cls, payload):
        instance = cls()
        instance.trans_date = payload.get('trans_date')
        instance.trans_amount = payload.get('trans_amount')
        instance.trans_currency = payload.get('trans_currency')
        instance.trans_description = payload.get('trans_description')
        instance.category = payload.get('category')
        instance.payment_type = payload.get('payment_type')
        instance.charge_identificator = payload.get('charge_identificator')
        instance.charge_number = payload.get('charge_number')
        instance.balance = payload.get('balance')

        return instance


TransactionDetailSchema = marshmallow_dataclass.class_schema(TransactionDetail)

