from dataclasses import dataclass
import marshmallow_dataclass
import uuid


@dataclass
class EventLogger:
    id: str = ""
    connection_id: str = ""
    connection_key: str = ""
    institution_id: str = ""
    enquiry_cpf: str = ""
    report_time: str = ""
    payload: str = ""

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()


EventLoggerSchema = marshmallow_dataclass.class_schema(EventLogger)
