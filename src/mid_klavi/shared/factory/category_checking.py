from shared.parsers.category_checking import parse_category_checking_payload_body
from shared.parsers.transaction_detail import parse_transaction_detail_payload
from shared.models.category_checking import CategoryChecking
from shared.models.transaction_detail import TransactionDetail

def build_category_checking_from_kavli_payload(payload):
    category_checking = CategoryChecking(**parse_category_checking_payload_body(payload))
    for transaction_detail in payload['TransactionDetail']:
        transaction = TransactionDetail(**parse_transaction_detail_payload(transaction_detail))
        transaction.category_id = category_checking.id
        category_checking.transaction_details.append(transaction)

    return category_checking

