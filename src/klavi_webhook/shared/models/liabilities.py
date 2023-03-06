from dataclasses import dataclass, field
from marshmallow import Schema
import marshmallow_dataclass
from shared.data_access_objects.liabilities import LiabilitiesDAO
from shared.data_access_objects.liability_stream import LiabilityStreamDAO
from shared.data_access_objects.liability_transaction import LiabilityTransactionDAO

import uuid

@dataclass
class Liabilities:
    id: str = ""
    report_id: str = ""
    account_holder: str = ""
    account_number: str = ""
    agency_number: str = ""
    bacen_id: str = ""
    bacen_name: str = ""
    bank_name: str = ""
    cpf_verified: str = ""
    days_covered: str = ""
    number_of_liability_streams: str = ""
    total_liabilities_last_180_days: str = ""
    total_liabilities_last_30_days: str = ""
    total_liabilities_last_60_days: str = ""
    total_liabilities_last_90_days: str = ""
    liability_streams: list = field(default_factory=list)

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()

class BaseLiabilitySchema(Schema):
    class Meta:
        exclude = ('liability_streams', )


LiabilitiesSchema = marshmallow_dataclass.class_schema(Liabilities, base_schema=BaseLiabilitySchema)


@dataclass
class LiabilityStream:
    id: str = ""
    category_id: str = ""
    liability_stream_type: str = ""
    liability_transactions: list = field(default_factory=list)

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()

class BaseLiabilityStreamSchema(Schema):
    class Meta:
        exclude = ('liability_transactions', )


LiabilityStreamSchema = marshmallow_dataclass.class_schema(LiabilityStream, base_schema=BaseLiabilityStreamSchema)



@dataclass
class LiabilityTransaction:
    id: str = ""
    category_id: str = ""
    trans_date: str = ""
    trans_amount: str = ""
    trans_description: str = ""

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()


LiabilityTransactionSchema = marshmallow_dataclass.class_schema(LiabilityTransaction)

