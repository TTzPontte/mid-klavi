from dataclasses import dataclass, field
from marshmallow import Schema, fields
from shared.data_access_objects.category_checking import CategoryCheckingDAO

import marshmallow_dataclass


@dataclass
class CategoryChecking:
    id: str = ""
    bank_name: str = ""
    bacen_name: str = ""
    bacen_id: str = ""
    bank_branch: str = ""
    account: str = ""
    operation_code: str = ""
    cpf_verified: str = ""
    holder_name: str = ""
    balance: str = ""
    TransactionDetail: list = field(default_factory=list)


    def __post_init__(self):
        print("ON POST INIT")
        self.schema = CategoryCheckingSchema()

    def save(self):
        dao = CategoryCheckingDAO('dev')
        payload = self.schema.dump(self)
        payload["id"] = "testeId"
        payload["report_id"] = "reportId"
        dao.save(payload)
        print("Object Saved")

class BaseClass(Schema):
    class Meta:
        exclude = ("TransactionDetail", )

CategoryCheckingSchema = marshmallow_dataclass.class_schema(CategoryChecking, base_schema=BaseClass)
