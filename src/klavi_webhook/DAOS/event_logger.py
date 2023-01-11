class EventLoggerDAO(BaseDao):
    def __init__(self, env: str):
        super().__init__(env)
        self.table_name = 'EventLogger'

    def log_event(self, event: dict):
        self.save(self.table_name, event)

    def get_logs(self, start_time: int, end_time: int):
        filter_expression = Key('timestamp').between(start_time, end_time)
        return self.scan(self.table_name, filter_expression=filter_expression)




