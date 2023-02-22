from shared.models.category_creditcard import CategoryCreditCardSchema, OpenStatementSchema, ClosedStatementSchema
from shared.models.transaction_detail import TransactionDetailSchema

import pandas


def export_category_creditcard_to_excel(report, writer):
    print("REPORT TO BE EXPORTED")
    print(report)
    category_creditcard_schema = CategoryCreditCardSchema()
    open_statement_schema = OpenStatementSchema()
    closed_statement_schema = ClosedStatementSchema()
    transaction_detail_schema = TransactionDetailSchema()

    category_credicards = []
    open_statements = []
    closed_statements = []
    open_transaction_details = []
    closed_transaction_details = []

    for category_credicard in report.category_creditcards:
        category_credicards.append(category_creditcard_schema.dump(category_credicard))

        for closed_statement in category_credicard.closed_statements:
            closed_statements.append(closed_statement_schema.dump(closed_statement))

            for transaction_detail in closed_statement.transaction_details:
                closed_transaction_details.append(transaction_detail_schema.dump(transaction_detail))

       # open_statements.append(open_statement_schema.dump(category_credicard.open_statement))
       # for transaction_detail in category_credicard.open_statement["transaction_details"]:
       #     open_transaction_details.append(transaction_detail_schema.dump(transaction_detail))

    data_frame_category_creditcard = pandas.DataFrame(category_credicards)
    data_frame_open_statement = pandas.DataFrame(open_statements)
    data_frame_closed_statements = pandas.DataFrame(closed_statements)
    data_frame_open_transaction_details = pandas.DataFrame(open_transaction_details)
    data_frame_closed_transaction_details = pandas.DataFrame(closed_transaction_details)

    data_frame_category_creditcard.to_excel(writer, sheet_name="Category Creditcard")
    data_frame_open_statement.to_excel(writer, sheet_name="Open Statement")
    data_frame_closed_statements.to_excel(writer, sheet_name="Open Statement")
    data_frame_open_transaction_details.to_excel(writer, sheet_name="Open Statement Transactions")
    data_frame_closed_transaction_details.to_excel(writer, sheet_name="Closed Statement Transactions")
