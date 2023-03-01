from dataclasses import dataclass
from shared.data_access_objects.score_k1 import ScoreK1DAO
from shared.models.score_k1 import ScoreK1, ScoreK1Schema


@dataclass
class ScoreK1Repository:
    def save(self, document):
        score_k1_schema = ScoreK1Schema()
        score_k1_document = score_k1_schema.dump(document)
        score_k1_dao = ScoreK1DAO()
        score_k1_dao.put(score_k1_document)


    def getByReportId(self, report_id):
        score_k1_dao = ScoreK1DAO()
        score_k1_obj = score_k1_dao.get(report_id)
        score_k1 = ScoreK1(**score_k1_obj)
        score_k1.score_k1_streams = []

        return score_k1