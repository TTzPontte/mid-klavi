def parse_score_k1_payload_body(payload):
    return {
        "account_info": payload.get('account_info'),
        "score_detail": payload.get('score_detail')
    }

