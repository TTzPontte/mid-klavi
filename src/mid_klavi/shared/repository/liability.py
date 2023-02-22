from dataclasses import dataclass
from shared.data_access_objects.liabilities import LiabilitiesDAO
from shared.data_access_objects.liability_transaction import LiabilityTransactionDAO
from shared.data_access_objects.liability_stream import LiabilityStreamDAO

from shared.models.liabilities import LiabilitiesSchema, LiabilityStreamSchema, LiabilityTransactionSchema
from shared.models.liabilities import Liabilities, LiabilityStream, LiabilityTransaction


@dataclass
class LiabilityRepository:
    def save(self, document):
        liabilities_schema = LiabilitiesSchema()
        liability_stream_schema = LiabilityStreamSchema()
        liability_transaction_schema = LiabilityTransactionSchema()

        liabilities_document = liabilities_schema.dump(document)

        liability_stream_ids = []
        for liability_stream in document.liability_streams:
            liability_stream_ids.append(str(liability_stream.id))
        liabilities_document['liability_streams'] = liability_stream_ids

        liabilities_dao = LiabilitiesDAO('dev')
        liabilities_stream_dao = LiabilityStreamDAO('dev')
        liability_transaction_dao = LiabilityTransactionDAO('dev')
        liabilities_dao.put(liabilities_document)

        for liability_stream in document.liability_streams:
            liability_stream_document = liability_stream_schema.dump(liability_stream)
            liability_stream_document['category_id'] = str(document.id)

            transactions_ids = []
            for liability_transaction in liability_stream.liability_transactions:
                liability_transaction_document = liability_transaction_schema.dump(liability_transaction)
                liability_transaction_document['category_id'] = str(liability_stream.id)
                transactions_ids.append(str(liability_transaction.id))
                liability_transaction_dao.put(liability_transaction_document)

            liability_stream_document['liability_transactions'] = transactions_ids
            liabilities_stream_dao.put(liability_stream_document)



        print("SAVED LIABILITY")

    def getByReportId(self, report_id):
        liabilities_dao = LiabilitiesDAO('dev')
        liability_stream_dao = LiabilityStreamDAO('dev')
        liability_transaction_dao = LiabilityTransactionDAO('dev')



        liabilities_obj = liabilities_dao.get(report_id)
        liabilities = Liabilities(**liabilities_obj)
        liabilities.liability_streams = []

        for liability_stream_id in liabilities_obj['liability_streams']:
            liability_stream_obj = liability_stream_dao.get({'id': liability_stream_id, 'category_id': str(liabilities.id)})
            liability_stream = LiabilityStream(**liability_stream_obj)
            liability_stream.liability_transactions = []
            for liability_transaction_id in liability_stream_obj['liability_transactions']:
                liability_transaction_obj = liability_transaction_dao.get({'id': liability_transaction_id, 'category_id': str(liability_stream.id)})
                liability_transaction = LiabilityTransaction(**liability_transaction_obj)
                liability_stream.liability_transactions.append(liability_transaction)

        return liabilities

