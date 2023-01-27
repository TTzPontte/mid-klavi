from shared.models.category_checking import CategoryCheckingSchema
from shared.models.transaction_detail import TransactionDetailSchema

import pandas


def export_category_checkings_to_excel(report, writer):
    category_checking_schema = CategoryCheckingSchema()
    transaction_detail_schema = TransactionDetailSchema()
    category_checkings = []
    transaction_details = []
    for category_checking in report.category_checking:
        category_checkings.append(category_checking_schema.dump(category_checking))
        for transaction_detail in category_checking.TransactionDetail:
            transaction_details.append(transaction_detail_schema.dump(transaction_detail))
    data_frame_category_checkings = pandas.DataFrame(category_checkings)
    print(transaction_details)
    data_frame_transaction_details = pandas.DataFrame(transaction_details)
    data_frame_category_checkings.to_excel(writer, sheet_name="Category Checking")
    data_frame_transaction_details.to_excel(writer, sheet_name="Transaction Detail")
