def parse_credit_card_payload_body(payload):
    return {
        'bank_name': payload.get('bank_name'),
        'bacen_name': payload.get('bacen_name'),
        'bacen_id': payload.get('bacen_id'),
        'card_last4num': payload.get('card_last4num'),
        'cpf_verified': payload.get('cpf_verified'),
        'holder_name': payload.get('holder_name'),
        'card_type': payload.get('card_type'),
        'credit_limit': payload.get('credit_limit'),
        'available_limit': payload.get('available_limit'),
        'agency_number': payload.get('agency_number'),
        'bank_account': payload.get('bank_account'),
        'is_active': payload.get('is_active'),
        'is_vip': payload.get('is_vip')
    }


def parse_credit_card_payload_open_statement(payload):
        return {
        'bill_amount': payload.get('bill_amount'),
        'due_date': payload.get('due_date'),
        'billing_date': payload.get('billing_date'),
        'bill_month': payload.get('bill_month')
 }


def parse_credit_card_payload_closed_statement(payload):
    return {
        'billing_date': payload.get('billing_date'),
        'bill_month': payload.get('bill_month'),
        'bill_amount': payload.get('bill_amount'),
        'minimum_payment': payload.get('minimum_payment'),
        'payment_date': payload.get('payment_date'),
        'payment_amount': payload.get('payment_amount')
    }
