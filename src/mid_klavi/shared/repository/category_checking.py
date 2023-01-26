from dataclasses import dataclass
from shared.data_access_objects.category_checking import CategoryCheckingDAO
from shared.models.category_checking import CategoryCheckingSchema
from shared.data_access_objects.transaction_detail import TransactionDetailDAO
from shared.models.transaction_detail import TransactionDetailSchema

@dataclass
class CategoryCheckingRepository:
    def save(self, document):
        category_checking_schema = CategoryCheckingSchema()
        transaction_detail_schema = TransactionDetailSchema()
        category_document = category_checking_schema.dump(document)
        category_dao = CategoryCheckingDAO('dev')
        transaction_detail_dao = TransactionDetailDAO('dev')
        category_document['id'] = 'teste_id'
        category_document['report_id'] = 'report_id'
        category_dao.save(category_document)
        transactions = document.TransactionDetail
        print("LE Transactions")
        print(transactions)
        for transaction_detail in transactions:
            transaction_detail_data = transaction_detail_schema.dump(transaction_detail)
            transaction_detail_data['id'] = "transaction_id"
            transaction_detail_data['category_id'] = "category_id"
            transaction_detail_dao.save(transaction_detail_data)
        print("SAVED@@@@@@")

    def getReportById(self, report_id):
        pass

