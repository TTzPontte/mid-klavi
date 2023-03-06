from dataclasses import dataclass, field
from marshmallow import Schema, fields, pre_dump
from shared.data_access_objects.category_checking import CategoryCheckingDAO

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


class BaseClass(Schema):

    class Meta:
        exclude = ('transaction_details', )



CategoryCheckingSchema = marshmallow_dataclass.class_schema(CategoryChecking, base_schema=BaseClass)
