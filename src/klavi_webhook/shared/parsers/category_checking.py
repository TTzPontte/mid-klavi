def parse_category_checking_payload_body(payload):
    return {
        'bank_name': payload.get('bank_name'),
        'bacen_name': payload.get('bacen_name'),
        'bacen_id': payload.get('bacen_id'),
        'bank_branch': payload.get('bank_branch'),
        'account': payload.get('account'),
        'operation_code': payload.get('operation_code'),
        'cpf_verified': payload.get('cpf_verified'),
        'holder_name': payload.get('holder_name'),
        'balance': payload.get('balance'),
    }
