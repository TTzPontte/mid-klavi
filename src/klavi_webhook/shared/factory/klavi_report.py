from shared.parsers.klavi_report import parse_klavi_report_payload_body
from shared.models.klavi_report import KlaviReport
from shared.factory.category_checking import build_category_checking_from_kavli_payload
from shared.factory.category_creditcard import build_category_creditcard_from_kavli_payload
from shared.factory.liabilities import build_liability_from_kavli_payload
from shared.factory.financial_insight import build_financial_insight_from_kavli_payload
from shared.factory.income import build_income_from_kavli_payload
from shared.factory.score_k1 import build_score_k1_from_kavli_payload
from shared.factory.balance import build_balance_from_kavli_payload
from shared.factory.risk_label import build_risk_label_from_kavli_payload

def build_report_from_klavi_payload(payload):
    klavi_report_data = parse_klavi_report_payload_body(payload)
    klavi_report = KlaviReport(**klavi_report_data)

    if klavi_report_data.get('report_type') == "category_checking":
        for category_checking_payload in payload.get('data').get("Category_checking"):
            category_checking = build_category_checking_from_kavli_payload(category_checking_payload)
            category_checking.report_id = klavi_report.id
            klavi_report.category_checkings.append(category_checking)
            
    if klavi_report_data.get('report_type') == "category_creditcard":
        for category_creditcard_payload in payload.get('data').get("Category_creditcard"):
            category_creditcard = build_category_creditcard_from_kavli_payload(category_creditcard_payload)
            category_creditcard.report_id = klavi_report.id
            klavi_report.category_creditcards.append(category_creditcard)

    if klavi_report_data.get('report_type') == "liabilities":
        for liability_payload in payload.get('data').get("Liabilities"):
            liability = build_liability_from_kavli_payload(liability_payload)
            liability.report_id = klavi_report.id
            klavi_report.liabilities.append(liability)

    if klavi_report_data.get('report_type') == "financial_insight":
        for financial_insight_payload in payload.get('data').get("financial_insight"):
            financial_insight = build_financial_insight_from_kavli_payload(financial_insight_payload)
            financial_insight.report_id = klavi_report.id
            klavi_report.financial_insights.append(financial_insight)

    if klavi_report_data.get('report_type') == "income":
        for income_payload in payload.get('data').get("Income"):
            income = build_income_from_kavli_payload(income_payload)
            income.report_id = klavi_report.id
            klavi_report.income.append(income)

    if klavi_report_data.get('report_type') == "score_k1":
        score_k1 = build_score_k1_from_kavli_payload(payload.get('data').get("score_info"))
        score_k1.report_id = klavi_report.id
        klavi_report.score_k1 = score_k1

    if klavi_report_data.get('report_type') == "identity":
        identity = build_score_k1_from_kavli_payload(payload.get('data').get("identity"))
        identity.report_id = klavi_report.id
        klavi_report.identity = identity

    if klavi_report_data.get('report_type') == "balance":
        for balance_payload in payload.get('data').get("accountBalance"):
            balance = build_balance_from_kavli_payload(balance_payload)
            balance.report_id = klavi_report.id
            klavi_report.balance.append(balance)

    if klavi_report_data.get('report_type') == "k_label":
        risk_label = build_risk_label_from_kavli_payload(payload.get('data').get("Risk_label"))
        risk_label.report_id = klavi_report.id
        klavi_report.risk_label = risk_label

    return klavi_report

