from shared.parsers.category_creditcard import parse_credit_card_payload_body, parse_credit_card_payload_open_statement, parse_credit_card_payload_closed_statement
from shared.parsers.transaction_detail import parse_transaction_detail_payload
from shared.models.category_creditcard import CategoryCreditCard, OpenStatement, ClosedStatement
from shared.models.transaction_detail import TransactionDetail

def build_category_creditcard_from_kavli_payload(payload):
    category_creditcard = CategoryCreditCard(**parse_credit_card_payload_body(payload))

    open_statement = OpenStatement(**parse_credit_card_payload_open_statement(payload['OpenStatement']))
    open_statement.category_id = category_creditcard.id

    for transaction_detail_payload in payload['OpenStatement']['TransactionDetail']:
        transaction_detail = TransactionDetail(**parse_transaction_detail_payload(transaction_detail_payload))
        transaction_detail.category_id = category_creditcard.id
        open_statement.transaction_details.append(transaction_detail)

    category_creditcard.open_statement = open_statement


    for closed_statement_payload in payload['ClosedStatement']:
        closed_statement = ClosedStatement(**parse_credit_card_payload_closed_statement(closed_statement_payload))
        closed_statement.category_id = category_creditcard.id

        for transaction_detail_payload in closed_statement_payload['TransactionDetail']:
            transaction_detail = TransactionDetail(**parse_transaction_detail_payload(transaction_detail_payload))
            transaction_detail.category_id = category_creditcard.id
            closed_statement.transaction_details.append(transaction_detail)

        category_creditcard.closed_statements.append(closed_statement)

    return category_creditcard

