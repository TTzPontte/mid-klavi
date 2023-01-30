from shared.parsers.klavi_report import parse_klavi_report_payload_body
from shared.models.klavi_report import KlaviReport
from shared.factory.category_checking import build_category_checking_from_kavli_payload

def build_report_from_klavi_payload(payload):
    klavi_report_data = parse_klavi_report_payload_body(payload)
    klavi_report = KlaviReport(**klavi_report_data)

    if klavi_report_data.get('report_type') == "category_checking":
        for category_checking_payload in payload.get('data').get("Category_checking"):
            category_checking = build_category_checking_from_kavli_payload(category_checking_payload)
            category_checking.report_id = klavi_report.id
            klavi_report.category_checkings.append(category_checking)

    return klavi_report

