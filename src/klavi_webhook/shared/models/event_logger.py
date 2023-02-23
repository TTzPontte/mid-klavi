from dataclasses import dataclass
import marshmallow_dataclass


@dataclass
class EventLogger:
    id: str = ""
    key: str = ""
    institution_id: str = ""
    enquiry_cpf: str = ""
    report_time: str = ""
    payload: str = ""


EventLoggerSchema = marshmallow_dataclass.class_schema(EventLogger)
