from shared.models.risk_label import RiskLabelSchema, LabelDetailSchema

import pandas


def export_risk_label_to_excel(report, writer):
    risk_label_schema = RiskLabelSchema()
    label_detail_schema = LabelDetailSchema()
    risk_label = risk_label_schema.dump(report.risk_label)

    line = {}
    label_details = []
    for key in risk_label["account_info"]:
        line[key] = risk_label["account_info"][key]

    for label_detail in report.risk_label.label_detail:
        label_details.append(label_detail_schema.dump(label_detail))

    data_frame_risk_label = pandas.DataFrame([line])
    data_frame_label_detail = pandas.DataFrame(label_details)

    data_frame_risk_label.to_excel(writer, sheet_name="RiskLabel")
    data_frame_label_detail.to_excel(writer, sheet_name="RiskLabel LabelDetail")

