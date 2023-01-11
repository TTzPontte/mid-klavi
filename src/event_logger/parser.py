def parse_payload_into_logger_object(payload):
    return {
        'id': payload['data']['connection_id'],
        'key': payload['data']['connection_key'],
        'institution_id': payload['data']['institution_id'],
        'enquire_cpf': payload['data']['enquire_cpf'],
        'report_time': payload['report_time']
    }
