def parse_risk_label_payload_body(payload):
    return {
        'account_info': payload.get('accountInfo'),
    }

def parse_risk_label_payload_label_detail(payload):
    return {
        'label_code': payload.get('label_code'),
        'label_name': payload.get('label_name'),
        'label_value': payload.get('label_value')
    }