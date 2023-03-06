from dataclasses import dataclass, field
from marshmallow import Schema

import marshmallow_dataclass
import uuid
import decimal

@dataclass
class RiskLabel:
    id: str = ""
    report_id: str = ""
    account_info: dict = field(default_factory=dict)
    label_detail: list = field(default_factory=list)

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()

class BaseRiskLabelSchema(Schema):
    class Meta:
        exclude = ('label_detail', )


RiskLabelSchema = marshmallow_dataclass.class_schema(RiskLabel, base_schema=BaseRiskLabelSchema)

@dataclass
class LabelDetail:
    id: str = ""
    category_id: str = ""
    label_code: str = ""
    label_name: str = ""
    label_value: str = ""

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()

LabelDetailSchema = marshmallow_dataclass.class_schema(LabelDetail)


