def parse_payload_into_logger_object(payload):
    return {
        'id': payload.get('data').get('connection_id'),
        'key': payload.get('data').get('connection_key'),
        'institution_id': payload.get('data').get('institution_id'),
        'enquiry_cpf': payload.get('data').get('enquiry_cpf'),
        'report_time': payload.get('report_time')
    }
