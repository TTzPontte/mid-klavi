from dataclasses import dataclass
import marshmallow_dataclass
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


LiabilitiesSchema = marshmallow_dataclass.class_schema(LiabilitiesSchema)


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


LiabilityStreamSchema = marshmallow_dataclass.class_schema(LiabilityStream)



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


LiabilityTransactionSchema = marshmallow_dataclass.class_schema(LiabilityTransaction)

