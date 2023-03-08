from dataclasses import dataclass, field
from marshmallow import Schema, pre_dump

from shared.models.new_models.category_checking import CategoryChecking

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
    income: list = field(default_factory=list)
    balance: list = field(default_factory=list)
    identity: dict = field(default_factory=dict)
    score_k1: dict = field(default_factory=dict)
    risk_label: dict = field(default_factory=dict)

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()


    @classmethod
    def from_payload(cls, payload):
        instance = cls()
        instance.enquiry_cpf = payload.get("data").get('enquiry_cpf')
        instance.user_consent = payload.get("data").get('user_consent')
        instance.allow_autoupdate = payload.get("data").get('allow_autoupdate')
        instance.connection_key = payload.get("data").get('connection_key')
        instance.connection_id = payload.get("data").get('connection_id')
        instance.institution_id = payload.get("data").get('institution_id')
        instance.report_type = payload.get("data").get('report_type')
        instance.report_id = payload.get("data").get('report_id')
        instance.report_version = payload.get("data").get('report_version')
        instance.category_checkings = [CategoryChecking.from_payload(item) for item in payload.get("data").get("Category_checking", [])]

        return instance

    def to_json(self):
        schema = KlaviReportSchema()
        return schema.dump(self)



class KlaviReportBase(Schema):

    class Meta:
        exclude = ('category_checkings', 'category_creditcards', 'liabilities', 'financial_insights', "income", "balance", "identity", "score_k1", "risk_label")


KlaviReportExcelSchema = marshmallow_dataclass.class_schema(KlaviReport, base_schema=KlaviReportBase)
KlaviReportSchema = marshmallow_dataclass.class_schema(KlaviReport, base_schema=KlaviReportBase)

