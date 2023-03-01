from dataclasses import dataclass
from shared.data_access_objects.income import IncomeDAO
from shared.data_access_objects.income_transaction import IncomeTransactionDAO
from shared.data_access_objects.income_stream import IncomeStreamDAO
from shared.models.income import IncomeSchema, IncomeStreamSchema, IncomeTransactionSchema
from shared.models.income import Income, IncomeStream, IncomeTransaction


@dataclass
class IncomeRepository:
    def save(self, document):
        income_schema = IncomeSchema()
        income_stream_schema = IncomeStreamSchema()
        income_transaction_schema = IncomeTransactionSchema()
        income_document = income_schema.dump(document)
        income_stream_ids = []

        for income_stream in document.income_streams:
            income_stream_ids.append(str(income_stream.id))
        income_document['income_streams'] = income_stream_ids
        income_dao = IncomeDAO()
        income_stream_dao = IncomeStreamDAO()
        income_transaction_dao = IncomeTransactionDAO()
        income_dao.put(income_document)

        for income_stream in document.income_streams:
            income_stream_document = income_stream_schema.dump(income_stream)
            income_stream_document['category_id'] = str(document.id)
            transactions_ids = []

            for income_transaction in income_stream.income_transactions:
                income_transaction_document = income_transaction_schema.dump(income_transaction)
                income_transaction_document['category_id'] = str(income_stream.id)
                transactions_ids.append(str(income_transaction.id))
                income_transaction_dao.put(income_transaction_document)
            income_stream_document['income_transactions'] = transactions_ids
            income_stream_dao.put(income_stream_document)


    def getByReportId(self, report_id):
        income_dao = IncomeDAO()
        income_stream_dao = IncomeStreamDAO()
        income_transaction_dao = IncomeTransactionDAO()
        income_obj = income_dao.get(report_id)
        income = Income(**income_obj)
        income.income_streams = []

        for income_stream_id in income_obj['income_streams']:
            income_stream_obj = income_stream_dao.get({'id': income_stream_id, 'category_id': str(income.id)})
            income_stream = IncomeStream(**income_stream_obj)
            income_stream.income_transactions = []
            for income_transaction_id in income_stream_obj['income_transactions']:
                income_transaction_obj = income_transaction_dao.get({'id': income_transaction_id, 'category_id': str(income_stream.id)})
                income_transaction = IncomeTransaction(**income_transaction_obj)
                income_stream.income_transactions.append(income_transaction)

        return income
