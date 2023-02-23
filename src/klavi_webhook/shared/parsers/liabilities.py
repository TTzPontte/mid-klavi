def parse_liabilities_payload_body(payload):

    return {
        'account_holder': payload.get('account_holder'),
        'account_number': payload.get('account_number'),
        'agency_number': payload.get('agency_number'),
        'bacen_id': payload.get('bacen_id'),
        'bacen_name': payload.get('bacen_name'),
        'bank_name': payload.get('bank_name'),
        'cpf_verified': payload.get('cpf_verified'),
        'days_covered': payload.get('days_covered'),
        'number_of_liability_streams': payload.get('number_of_liability_streams'),
        'total_liabilities_last_180_days': payload.get('total_liabilities_last_180_days'),
        'total_liabilities_last_30_days': payload.get('total_liabilities_last_30_days'),
        'total_liabilities_last_60_days': payload.get('total_liabilities_last_60_days'),
        'total_liabilities_last_90_days': payload.get('total_liabilities_last_90_days')
    }


def parse_liabilities_payload_payload_liability_stream(payload):
        return {
        'liability_stream_type': payload.get('liability_stream_type')
 }


def parse_liabilities_payload_liability_transaction(payload):
    return {
        'trans_date': payload.get('trans_date'),
        'trans_amount': payload.get('trans_amount'),
        'trans_description': payload.get('trans_description'),
    }
