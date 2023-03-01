def parse_balance_payload_body(payload):
    return {
        'account_holder': payload.get('account_holder'),
        'account_type': payload.get('account_type'),
        'account_number': payload.get('account_number'),
        'agency_number': payload.get('agency_number'),
        'bacen_id': payload.get('bacen_id'),
        'bacen_name': payload.get('bacen_name'),
        'bank_name': payload.get('bank_name'),
        'cpf_verified': payload.get('cpf_verified'),
        'current_balance': payload.get('current_balance'),
        'available_limit': payload.get('available_limit'),
        'total_limit': payload.get('total_limit')
    }
