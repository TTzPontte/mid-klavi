from dataclasses import dataclass, field
from marshmallow import Schema, fields
from shared.data_access_objects.category_checking import CategoryCheckingDAO

import marshmallow_dataclass


@dataclass
class KlaviReport:
    id: str = ""
    enquiry_cpf: str = ""
    user_consent: str = ""
    allow_autoupdate: str = ""
    connection_key: str = ""
    connection_id: str = ""
    report_type: str = ""
    report_id: str = ""
    institution_id: str = ""
    report_version: str = ""
    report_time: str = ""
    category_checking: list = field(default_factory=list)

    def __post_init__(self):
        print("ON POST INIT")
        self.schema = KlaviReportSchema()

    def save(self):
        print("Object Saved")


KlaviReportSchema = marshmallow_dataclass.class_schema(KlaviReport)

class KlaviReportBase(Schema):
    class Meta:
        exclude = ('category_checking', )


KlaviReportExcelSchema = marshmallow_dataclass.class_schema(KlaviReport, base_schema=KlaviReportBase)
