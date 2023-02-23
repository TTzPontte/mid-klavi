from dataclasses import dataclass, field
from marshmallow import Schema, pre_dump

import marshmallow_dataclass
import uuid


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
    json_object: dict = field(default_factory=dict)
    category_checkings: list = field(default_factory=list)
    category_creditcards: list = field(default_factory=list)
    liabilities: list = field(default_factory=list)
    financial_insights: list = field(default_factory=list)

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()



class KlaviReportBase(Schema):
   # @pre_dump
   # def extract_relation_ids(self, out_data, **kwargs):
   #     category_ids = []
   #     for category in out_data.category_checkings:
   #         category_ids.append(str(category.id))
   #     out_data.category_checkings = category_ids
   #     print("Karalha")
   #     print(out_data)

   #     return out_data
    class Meta:
        exclude = ('category_checkings', 'category_creditcards', 'liabilities', 'financial_insights')


KlaviReportExcelSchema = marshmallow_dataclass.class_schema(KlaviReport, base_schema=KlaviReportBase)
KlaviReportSchema = marshmallow_dataclass.class_schema(KlaviReport, base_schema=KlaviReportBase)

