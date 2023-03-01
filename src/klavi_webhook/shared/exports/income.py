from shared.models.income import IncomeSchema, IncomeStreamSchema, IncomeTransactionSchema

import pandas


def export_income_to_excel(report, writer):
    income_schema = IncomeSchema()
    income_stream_schema = IncomeStreamSchema()
    income_transaction_schema = IncomeTransactionSchema()

    income_list = []
    income_steams = []
    income_transactions = []
    for income in report.income:
        income_list.append(income_schema.dump(income))
        for income_stream in income.income_streams:
            income_steams.append(income_stream_schema.dump(income_stream))
            for income_transaction in income_stream.income_transactions:
                income_transactions.append(income_transaction_schema.dump(income_transaction))
    data_frame_income = pandas.DataFrame(income_list)
    data_frame_income_stream = pandas.DataFrame(income_steams)
    data_frame_income_transactions = pandas.DataFrame(income_transactions)

    data_frame_income.to_excel(writer, sheet_name="Income")
    data_frame_income_stream.to_excel(writer, sheet_name="Income Streams")
    data_frame_income_transactions.to_excel(writer, sheet_name="Income Transactions")

