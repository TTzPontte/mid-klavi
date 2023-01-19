from dataclasses import dataclass
from marshmallow import Schema, fields
from shared.data_access_objects.liabilities import LiabilitiesDAO
from shared.data_access_objects.liability_stream import LiabilityStreamDAO
from shared.data_access_objects.liability_transaction import LiabilityTransactionDAO


@dataclass
class Liabilities:
    id: str = ""
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

    def __post_init__(self):
        print("ON POST INIT")
        self.schema = LiabilitiesSchema()

    def save(self):
        dao = LiabilitiesDAO('dev')
        payload = self.schema.dump(self)
        payload['id'] = 'meuid'
        payload['report_id'] = "category_id"
        dao.put(payload)
        print("Object Saved")


class LiabilitiesSchema(Schema):
    id: fields.Str()
    account_holder: fields.Str()
    account_number: fields.Str()
    agency_number: fields.Str()
    bacen_id: fields.Str()
    bacen_name: fields.Str()
    bank_name: fields.Str()
    cpf_verified: fields.Str()
    days_covered: fields.Str()
    number_of_liability_streams: fields.Str()
    total_liabilities_last_180_days: fields.Str()
    total_liabilities_last_30_days: fields.Str()
    total_liabilities_last_60_days: fields.Str()
    total_liabilities_last_90_days: fields.Str()

@dataclass
class LiabilityStream:
    id: str = ""
    liability_stream_type: str = ""


    def __post_init__(self):
        print("ON POST INIT")
        self.schema = LiabilityStreamSchema()

    def save(self):
        dao = LiabilityStreamDAO('dev')
        payload = self.schema.dump(self)
        payload['id'] = 'meuid'
        payload['category_id'] = "category_id"
        dao.put(payload)
        print("Object Saved")


class LiabilityStreamSchema(Schema):
    id: fields.Str()
    liability_stream_type: fields.Str()


@dataclass
class LiabilityTransaction:
    id: str = ""
    trans_date: str = ""
    trans_amount: str = ""
    trans_description: str = ""

    def __post_init__(self):
        print("ON POST INIT")
        self.schema = LiabilityTransactionSchema()

    def save(self):
        dao = LiabilityTransactionDAO('dev')
        payload = self.schema.dump(self)
        payload['id'] = 'meuid'
        payload['category_id'] = "category_id"
        dao.put(payload)
        print("Object Saved")


class LiabilityTransactionSchema(Schema):
    id: fields.Str()
    trans_date: fields.Str()
    trans_amount: fields.Str()
    trans_description: fields.Str()
