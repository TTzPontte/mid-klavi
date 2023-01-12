def parse_payload_into_logger_object(payload):
    return {
        'id': payload['data']['connection_id'],
        'key': payload['data']['connection_key'],
        'institution_id': payload['data']['institution_id'],
        'enquiry_cpf': payload['data']['enquiry_cpf'],
        'report_time': payload['report_time']
    }
