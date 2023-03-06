from shared.models.score_k1 import ScoreK1Schema

import pandas


def export_score_k1_to_excel(report, writer):
    score_k1_schema = ScoreK1Schema()
    score_k1 = score_k1_schema.dump(report.score_k1)
    print("OOOPA")
    print(score_k1)
    line = {}
    for key in score_k1["account_info"]:
        line[key] = score_k1["account_info"][key]
    for key in score_k1["score_detail"]:
        line[key] = score_k1["score_detail"][key]


    data_frame_score_k1 = pandas.DataFrame([line])

    data_frame_score_k1.to_excel(writer, sheet_name="ScoreK1")
