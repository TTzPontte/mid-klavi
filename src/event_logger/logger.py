from dataclasses import dataclass
from marshmallow import Schema, fields
from src.klavi_webhook.DAOS.event_logger import log_event


@dataclass
class Logger:
    id: str = ""
    key: str = ""
    institution_id: str = ""
    enquire_cpf: str = ""
    report_time: str = ""

    def __post_init__(self):
        self.schema = LoggerSchema()

    def save(self):
        log_event(self.schema.dump(self))
        print("Object Saved")


class LoggerSchema(Schema):
    id = fields.Str()
    key = fields.Str()
    institution_id = fields.Str()
    enquire_cpf = fields.Str()
    report_time = fields.Str()
