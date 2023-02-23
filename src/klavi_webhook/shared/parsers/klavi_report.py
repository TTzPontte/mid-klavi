def parse_klavi_report_payload_body(payload):
    return {
        'report_time': payload.get('report_time'),
        'enquiry_cpf': payload.get('data').get('enquiry_cpf'),
        'user_consent': payload.get('data').get('user_consent'),
        'allow_autoupdate': payload.get('data').get('allow_autoupdate'),
        'connection_key': payload.get('data').get('connection_key'),
        'connection_id': payload.get('data').get('connection_id'),
        'institution_id': payload.get('data').get('institution_id'),
        'report_type': payload.get('data').get('report_type'),
        'report_id': payload.get('data').get('report_id'),
        'report_version': payload.get('data').get('report_version')
    }
