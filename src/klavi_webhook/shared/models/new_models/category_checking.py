from dataclasses import dataclass, field
from marshmallow import Schema, fields, pre_dump
from shared.data_access_objects.category_checking import CategoryCheckingDAO
from shared.models.transaction_detail import TransactionDetail

import marshmallow_dataclass
import uuid


@dataclass
class CategoryChecking:
    id: str = ""
    report_id: str = ""
    bank_name: str = ""
    bacen_name: str = ""
    bacen_id: str = ""
    bank_branch: str = ""
    account: str = ""
    operation_code: str = ""
    cpf_verified: str = ""
    holder_name: str = ""
    balance: str = ""
    transaction_details: list = field(default_factory=list)

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()

    @classmethod
    def from_payload(cls, payload):
        instance = cls()

        instance.bank_name = payload.get('bank_name')
        instance.bacen_name = payload.get('bacen_name')
        instance.bacen_id = payload.get('bacen_id')
        instance.bank_branch = payload.get('bank_branch')
        instance.account = payload.get('account')
        instance.operation_code = payload.get('operation_code')
        instance.cpf_verified = payload.get('cpf_verified')
        instance.holder_name = payload.get('holder_name')
        instance.balance = payload.get('balance')
        instance.transaction_details = [TransactionDetail.from_payload(item) for item in payload.get("TransactionDetail", [])]

        return instance


    def to_json(self):
        schema = CategoryCheckingSchema()
        return schema.dump(self)



class BaseClass(Schema):

    class Meta:
        exclude = ('transaction_details', )



CategoryCheckingSchema = marshmallow_dataclass.class_schema(CategoryChecking, base_schema=BaseClass)
