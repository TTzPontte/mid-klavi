from shared.parsers.financial_insight import parse_financial_insight_payload_body, \
    parse_financial_insight_payload_cashflow_analysis, parse_financial_insight_payload_credit_analysis, \
    parse_financial_insight_payload_credit_card_spending, parse_financial_insight_payload_financial_profile
from shared.models.financial_insight import FinancialInsight, FinancialCashflowAnalysis, FinancialCreditAnalisys, \
    FinancialCreditCardSpending, FinancialProfile

def build_financial_insight_from_kavli_payload(payload):
    financial_insight = FinancialInsight(**parse_financial_insight_payload_body(payload))

    for cashflow_analysis_payload in payload['cashflowAnalysis']:
        cashflow_analysis = FinancialCashflowAnalysis(**parse_financial_insight_payload_cashflow_analysis(cashflow_analysis_payload))
        cashflow_analysis.category_id = financial_insight.id
        financial_insight.cashflow_analysis.append(cashflow_analysis)

    for credit_analysis_payload in payload['creditAnalysis']:
        credit_analysis = FinancialCreditAnalisys(**parse_financial_insight_payload_credit_analysis(credit_analysis_payload))
        credit_analysis.category_id = financial_insight.id
        financial_insight.credit_analysis.append(credit_analysis)

    if payload['creditcardSpending'] is not None:
        for creditcard_spending_payload in payload['creditcardSpending']:
            creditcard_spending = FinancialCreditCardSpending(**parse_financial_insight_payload_credit_card_spending(creditcard_spending_payload))
            creditcard_spending.category_id = financial_insight.id
            financial_insight.creditcard_spendings.append(creditcard_spending)

    for financial_profile_payload in payload['financialProfile']:
        financial_profile = FinancialProfile(**parse_financial_insight_payload_financial_profile(financial_profile_payload))
        financial_profile.category_id = financial_insight.id
        financial_insight.financial_profiles.append(financial_profile)

    return financial_insight

