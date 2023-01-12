from dataclasses import dataclass
from marshmallow import Schema, fields
from DAOS.event_logger import EventLoggerDAO


@dataclass
class Logger:
    id: str = ""
    key: str = ""
    institution_id: str = ""
    enquiry_cpf: str = ""
    report_time: str = ""

    def __post_init__(self):
        print("ON POST INIT")
        self.schema = LoggerSchema()

    def save(self):
        dao = EventLoggerDAO('dev')
        dao.log_event(self.schema.dump(self))
        print("Object Saved")


class LoggerSchema(Schema):
    id = fields.Str()
    key = fields.Str()
    institution_id = fields.Str()
    enquiry_cpf = fields.Str()
    report_time = fields.Str()
