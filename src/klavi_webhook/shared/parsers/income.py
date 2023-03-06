def parse_income_payload_body(payload):
    return {
        'account_holder': payload.get('account_holder'),
        'account_number': payload.get('account_number'),
        'agency_number': payload.get('agency_number'),
        'bacen_id': payload.get('bacen_id'),
        'bacen_name': payload.get('bacen_name'),
        'bank_name': payload.get('bank_name'),
        'cpf_verified': payload.get('cpf_verified'),
        'days_covered': payload.get('days_covered'),
        'number_of_income_streams': payload.get('number_of_income_streams'),
        'total_income_last_180_days': payload.get('total_income_last_180_days'),
        'total_income_last_30_days': payload.get('total_income_last_30_days'),
        'total_income_last_60_days': payload.get('total_income_last_60_days'),
        'total_income_last_90_days': payload.get('total_income_last_90_days')
    }


def parse_income_payload_income_stream(payload):
    return {
        'income_day': payload.get('incomeDay'),
        'income_stream_type': payload.get('income_stream_type'),
    }


def parse_income_payload_income_transaction(payload):
    return {
        'trans_date': payload.get('trans_date'),
        'trans_amount': payload.get('trans_amount'),
        'trans_description': payload.get('trans_description'),
    }
