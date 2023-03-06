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


TransactionDetailSchema = marshmallow_dataclass.class_schema(TransactionDetail)

