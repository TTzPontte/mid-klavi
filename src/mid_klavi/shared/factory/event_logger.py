from shared.parsers.event_logger import parse_payload_into_logger_object
from shared.models.event_logger import EventLogger

def build_event_logger_from_klavi_payload(payload):
    event_logger_data = parse_payload_into_logger_object(payload)
    event_logger = EventLogger(**event_logger_data)

    return event_logger
