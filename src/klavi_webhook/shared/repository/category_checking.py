from dataclasses import dataclass
from shared.data_access_objects.category_checking import CategoryCheckingDAO
from shared.models.category_checking import CategoryCheckingSchema, CategoryChecking
from shared.models.transaction_detail import TransactionDetail
from shared.data_access_objects.transaction_detail import TransactionDetailDAO
from shared.models.transaction_detail import TransactionDetailSchema

@dataclass
class CategoryCheckingRepository:
    def save(self, document):
        #category_checking_schema = CategoryCheckingSchema()
        #transaction_detail_schema = TransactionDetailSchema()
        #category_document = category_checking_schema.dump(document)

        #transaction_detail_ids = []
        #for transaction_detail in document.transaction_details:
        #    transaction_detail_ids.append(str(transaction_detail.id))
        #category_document['transaction_details'] = transaction_detail_ids
        category_dao = CategoryCheckingDAO()
        #transaction_detail_dao = TransactionDetailDAO()
        category_dao.save(document)
        #transactions = document.transaction_details

        #for transaction_detail in transactions:
        #    transaction_detail_data = transaction_detail_schema.dump(transaction_detail)
        #    transaction_detail_data['category_id'] = str(document.id)
        #    transaction_detail_dao.save(transaction_detail_data)

    def getByReportId(self, report_id):
        category_checking_dao = CategoryCheckingDAO()
        transaction_detail_dao = TransactionDetailDAO()
        category_checking_obj = category_checking_dao.get(report_id)
        category_checking = CategoryChecking(**category_checking_obj)
        category_checking.transaction_details = []

        for transaction_detail_id in category_checking_obj['transaction_details']:
            transaction_detail_obj = transaction_detail_dao.get({'id': transaction_detail_id, 'category_id': str(category_checking.id)})
            category_checking.transaction_details.append(TransactionDetail(**transaction_detail_obj))

        return category_checking
