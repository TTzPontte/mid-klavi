from shared.parsers.category_checking import parse_category_checking_payload_body
from shared.parsers.transaction_detail import parse_transaction_detail_payload
from shared.models.category_checking import CategoryChecking
from shared.models.transaction_detail import TransactionDetail

def build_category_checking_from_kavli_payload(payload):
    category_checking = CategoryChecking(**parse_category_checking_payload_body(payload))
    #category_checking_body = parse_category_checking_payload_body(payload)
    category_checking_transactions = list()
    for transaction_detail in payload['TransactionDetail']:
        new_transaction = TransactionDetail(**parse_transaction_detail_payload(transaction_detail))
        category_checking_transactions.append(new_transaction)
        category_checking.TransactionDetail.append(new_transaction)
        #category_checking.TransactionDetail += new_transaction
    #category_checking['TransactionDetail'] = category_checking_transactions
    #category_checking.set('TransactionDetail', category_checking_transactions)

    return category_checking

