def parse_payload_into_logger_object(payload):
    return {
        'id': payload['data']['connection_id']
    }
