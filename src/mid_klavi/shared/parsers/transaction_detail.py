def parse_transaction_detail_payload(payload):
    return {
        'trans_date': payload.get('trans_date', ''),
        'trans_amount': payload.get('trans_amount', ''),
        'trans_currency': payload.get('trans_currency', ''),
        'trans_description': payload.get('trans_description', ''),
        'category': payload.get('category', ''),
        'payment_type': payload.get('payment_type', ''),
        'charge_identificator': payload.get('charge_identificator', ''),
        'charge_number': payload.get('charge_number', ''),
        'balance': payload.get('balance', '')
    }
