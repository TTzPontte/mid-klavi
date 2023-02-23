from shared.parsers.liabilities import parse_liabilities_payload_body, parse_liabilities_payload_payload_liability_stream, parse_liabilities_payload_liability_transaction
from shared.models.liabilities import Liabilities, LiabilityStream, LiabilityTransaction

def build_liability_from_kavli_payload(payload):
    liability = Liabilities(**parse_liabilities_payload_body(payload))

    for liability_stream_payload in payload['liabilityStream']:
        liability_stream = LiabilityStream(**parse_liabilities_payload_payload_liability_stream(liability_stream_payload))
        liability_stream.category_id = liability.id

        for liability_transaction_payload in liability_stream_payload['liabilityTransactions']:
            transaction_detail = LiabilityTransaction(**parse_liabilities_payload_liability_transaction(liability_transaction_payload))
            transaction_detail.category_id = liability_stream.id
            liability_stream.liability_transactions.append(transaction_detail)

        liability.liability_streams.append(liability_stream)

    return liability

