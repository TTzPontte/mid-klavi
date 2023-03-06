from shared.parsers.income import parse_income_payload_body, parse_income_payload_income_stream, parse_income_payload_income_transaction
from shared.models.income import Income, IncomeStream, IncomeTransaction

def build_income_from_kavli_payload(payload):
    income = Income(**parse_income_payload_body(payload))

    for income_stream_payload in payload['incomeStream']:
        income_stream = IncomeStream(**parse_income_payload_income_stream(income_stream_payload))
        income_stream.category_id = income.id

        for income_transaction_payload in income_stream_payload['incomeTransactions']:
            transaction_detail = IncomeTransaction(**parse_income_payload_income_transaction(income_transaction_payload))
            transaction_detail.category_id = income_stream.id
            income_stream.income_transactions.append(transaction_detail)

        income.income_streams.append(income_stream)

    return income

