from shared.parsers.risk_label import parse_risk_label_payload_body, parse_risk_label_payload_label_detail
from shared.models.risk_label import RiskLabel, LabelDetail

def build_risk_label_from_kavli_payload(payload):
    risk_label = RiskLabel(**parse_risk_label_payload_body(payload))

    for label_detail_payload in payload['labelDetail']:
        label_detail = LabelDetail(**parse_risk_label_payload_label_detail(label_detail_payload))
        label_detail.category_id = risk_label.id
        risk_label.label_detail.append(label_detail)

    return risk_label

