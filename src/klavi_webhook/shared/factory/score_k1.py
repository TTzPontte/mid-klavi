from shared.parsers.score_k1 import parse_score_k1_payload_body
from shared.models.score_k1 import ScoreK1

def build_score_k1_from_kavli_payload(payload):
    score_k1 = ScoreK1(**parse_score_k1_payload_body(payload))

    return score_k1

