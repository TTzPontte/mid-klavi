from shared.parsers.balance import parse_balance_payload_body
from shared.models.balance import Balance

def build_balance_from_kavli_payload(payload):
    balance = Balance(**parse_balance_payload_body(payload))

    return balance
