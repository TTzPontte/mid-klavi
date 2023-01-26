from dataclasses import dataclass
import marshmallow_dataclass
from shared.data_access_objects.event_logger import EventLoggerDAO


@dataclass
class Logger:
    id: str = ""
    key: str = ""
    institution_id: str = ""
    enquiry_cpf: str = ""
    report_time: str = ""

    def __post_init__(self):
        self.schema = LoggerSchema()

    def save(self):
        dao = EventLoggerDAO('dev')
        dao.log_event(self.schema.dump(self))


LoggerSchema = marshmallow_dataclass.class_schema(Logger)

