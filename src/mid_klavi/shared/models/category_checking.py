from dataclasses import dataclass
from marshmallow import Schema, fields
from shared.data_access_objects.category_checking import CategoryCheckingDAO


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


class CategoryCheckingSchema(Schema):
    id: fields.Str()
    bank_name: fields.Str()
    bacen_name: fields.Str()
    bacen_id: fields.Str()
    bank_branch: fields.Str()
    account: fields.Str()
    operation_code: fields.Str()
    cpf_verified: fields.Str()
    holder_name: fields.Str()
    balance: fields.Str()
