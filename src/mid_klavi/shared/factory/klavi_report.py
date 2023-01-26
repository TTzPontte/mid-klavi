from shared.parsers.klavi_report import parse_klavi_report_payload_body
from shared.models.klavi_report import KlaviReport

def build_report_from_klavi_payload(payload):
    klavi_report_data = parse_klavi_report_payload_body(payload)
    klavi_report = KlaviReport(**klavi_report_data)

    if klavi_report_data.get('report_type') == "category_checking":
        for category_checking_payload in payload.get('data').get("Category_checking"):
            category_checking = build_category_checking_from_kavli_payload(category_checking_payload)
            klavi_report.category_checking.append(category_checking)
    if klavi_report_data.get('report_type') == "category_creditcard":
        for category_creditcard_payload in payload.get('data').get("Category_creditcard"):
            category_creditcard = build_category_creditcard_from_kavli_payload(category_creditcard_payload)
            klavi_report.category_creditcard.append(category_creditcard)
    if klavi_report_data.get('report_type') == "financial_insights":
        for financial_insights_payload in payload.get('data').get("financial_insights"):
            financial_insights = build_financial_insights_from_kavli_payload(financial_insights_payload)
            klavi_report.financial_insights.append(financial_insights)
    if klavi_report_data.get('report_type') == "liabilities":
        for liabilites_payload in payload.get('data').get("liabilites"):
            liabilites = build_liabilites_from_kavli_payload(liabilites_payload)
            klavi_report.liabilites.append(liabilites)


    return klavi_report

