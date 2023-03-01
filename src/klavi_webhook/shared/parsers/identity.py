def parse_identity_payload_body(payload):
    return {
        'account_number': payload.get('account_number'),
        'agency_number': payload.get('agency_number'),
        'bacen_id': payload.get('bacen_id'),
        'bacen_name': payload.get('bacen_name'),
        'bank_name': payload.get('bank_name'),
        'cpf_verified': payload.get('cpf_verified'),
        'name': payload.get('name'),
        'cellphone': payload.get('cellphone'),
        'email': payload.get('email'),
        'correspondence_address': payload.get('correspondence_address')
    }