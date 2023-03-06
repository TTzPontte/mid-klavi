from dataclasses import dataclass
from shared.data_access_objects.risk_label import RiskLabelDAO
from shared.data_access_objects.label_detail import LabelDetailDAO
from shared.models.risk_label import RiskLabelSchema, LabelDetailSchema
from shared.models.risk_label import RiskLabel, LabelDetail


@dataclass
class RiskLabelRepository:
    def save(self, document):
        risk_label_schema = RiskLabelSchema()
        label_detail_schema = LabelDetailSchema()
        risk_label_document = risk_label_schema.dump(document)
        label_detail_ids = []

        for label_detail in document.label_detail:
            label_detail_ids.append(str(label_detail.id))
        risk_label_document['label_detail'] = label_detail_ids
        risk_label_dao = RiskLabelDAO()
        label_detail_dao = LabelDetailDAO()
        risk_label_dao.put(risk_label_document)

        for label_detail in document.label_detail:
            label_detail_document = label_detail_schema.dump(label_detail)
            label_detail_document['category_id'] = str(document.id)
            label_detail_dao.put(label_detail_document)


    def getByReportId(self, report_id):
        risk_label_dao = RiskLabelDAO()
        label_detail_dao = LabelDetailDAO()
        risk_label_obj = risk_label_dao.get(report_id)
        risk_label = RiskLabel(**risk_label_obj)
        risk_label.label_detail = []

        for label_detail_id in risk_label_obj['label_detail']:
            label_detail_obj = label_detail_dao.get({'id': label_detail_id, 'category_id': str(risk_label.id)})
            label_detail = LabelDetail(**label_detail_obj)
            risk_label.label_detail.append(label_detail)

        return risk_label
