def parse_financial_insight_payload_body(payload):
    return {
        'bacen_id': payload.get('bacen_id'),
        'bacen_name': payload.get('bacen_name'),
        'bank_name': payload.get('bank_name'),
        'agency_number': payload.get('agency_number'),
        'account_number': payload.get('account_number'),
        'cpf_verified': payload.get('cpf_verified'),
        'account_holder': payload.get('account_holder'),
        'days_covered': payload.get('days_covered')
    }


def parse_financial_insight_payload_cashflow_analysis(payload):
    return {'checking_account_balance': payload.get('checking_account_balance'),
        'avg_daily_balance_last_180_days': payload.get('avg_daily_balance_last_180_days'),
        'avg_daily_balance_last_30_days': payload.get('avg_daily_balance_last_30_days'),
        'avg_daily_balance_last_60_days': payload.get('avg_daily_balance_last_60_days'),
        'avg_daily_balance_last_90_days': payload.get('avg_daily_balance_last_90_days'),
        'inflow_last_180_days': payload.get('inflow_last_180_days'),
        'inflow_last_30_days': payload.get('inflow_last_30_days'),
        'inflow_last_60_days': payload.get('inflow_last_60_days'),
        'inflow_last_90_days': payload.get('inflow_last_90_days'),
        'outflow_last_180_days': payload.get('outflow_last_180_days'),
        'outflow_last_30_days': payload.get('outflow_last_30_days'),
        'outflow_last_60_days': payload.get('outflow_last_60_days'),
        'outflow_last_90_days': payload.get('outflow_last_90_days'),
        'saving_account_balance': payload.get('saving_account_balance')}


def parse_financial_insight_payload_credit_analysis(payload):
    return {'overdraft_limit': payload.get('overdraft_limit'), 'preapproved_loan': payload.get('preapproved_loan'),

    }


def parse_financial_insight_payload_credit_card_spending(payload):
    return {'card_holder': payload.get('card_holder'), 'card_last_4_digit': payload.get('card_last_4_digit'),
        'card_type': payload.get('card_type'), 'credit_limit': payload.get('credit_limit'),
        'closed_bills_covered': payload.get('closed_bills_covered'),
        'open_bill_balance': payload.get('open_bill_balance'), 'last_closed_bill': payload.get('last_closed_bill'),
        'avg_last_3_closed_bills': payload.get('avg_last_3_closed_bills'), 'days_covered': payload.get('days_covered'),
        'has_late_payment': payload.get('has_late_payment'),
        'pay_bills_in_installment': payload.get('pay_bills_in_installment')}


def parse_financial_insight_payload_financial_profile(payload):
    return {'additional_overdraft_interest': payload.get('additional_overdraft_interest'),
        'atm_withdrawal': payload.get('atm_withdrawal'), 'has_inss': payload.get('has_inss'),
        'has_iptu_payment': payload.get('has_iptu_payment'), 'has_ipva_payment': payload.get('has_ipva_payment'),
        'has_returned_cheque': payload.get('has_returned_cheque'), 'has_severance': payload.get('has_severance'),
        'iof': payload.get('iof'), 'overdraft_interest': payload.get('overdraft_interest'), }
