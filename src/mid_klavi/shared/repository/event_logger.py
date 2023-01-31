from dataclasses import dataclass
from shared.data_access_objects.event_logger import EventLoggerDAO
from shared.models.event_logger import EventLoggerSchema


@dataclass
class EventLoggerRepository:
    def save(self, event_logger):
        event_logger_schema = EventLoggerSchema()
        event_logger_dao = EventLoggerDAO('dev')
        event_logger_document = event_logger_schema.dump(event_logger)
        event_logger_dao.put(event_logger_document)
