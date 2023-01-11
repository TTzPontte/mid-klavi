from dataclasses import dataclass
from marshmallow import Schema, fields


@dataclass()
class Logger:
    id: str = ""
    key: str = ""
    institution_id: str = ""
    enquire_cpf: str = ""
    report_time: str = ""
    def save(self):
        #Call DAO to save object into database
        pass


class LoggerSchema(Schema):
    id = fields.Str()
    key = fields.Str()
    institution_id = fields.Str()
    enquire_cpf = fields.Str()
    report_time = fields.Str()
