from shared.models.liabilities import LiabilitiesSchema, LiabilityStreamSchema, LiabilityTransactionSchema

import pandas


def export_liabilities_to_excel(report, writer):
    liabilities_schema = LiabilitiesSchema()
    liability_stream_schema = LiabilityStreamSchema()
    liability_transaction_schema = LiabilityTransactionSchema()

    liabilities = []
    liability_steams = []
    liability_transactions = []
    for liability in report.liabilities:
        liabilities.append(liabilities_schema.dump(liability))
        for liability_stream in liability.liability_streams:
            liability_steams.append(liability_stream_schema.dump(liability_stream))
            for liability_transaction in liability_steams.transactions:
                liability_transactions.append(liability_transaction_schema.dump(liability_transaction))
    data_frame_liabilities = pandas.DataFrame(liabilities)
    data_frame_liability_stream = pandas.DataFrame(liability_steams)
    data_frame_liability_transactions = pandas.DataFrame(liability_transactions)

    data_frame_liabilities.to_excel(writer, sheet_name="Liabilities")
    data_frame_liability_stream.to_excel(writer, sheet_name="Liabilities Streams")
    data_frame_liability_transactions.to_excel(writer, sheet_name="Liabilities Transactions")

