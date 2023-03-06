from shared.models.balance import BalanceSchema

import pandas


def export_balance_to_excel(report, writer):
    balance_schema = BalanceSchema()

    balance_list = []
    for balance in report.balance:
        balance_list.append(balance_schema.dump(balance))
    data_frame_balance = pandas.DataFrame(balance_list)
    data_frame_balance.to_excel(writer, sheet_name="Balance")
