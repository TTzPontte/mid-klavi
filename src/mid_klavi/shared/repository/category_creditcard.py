from dataclasses import dataclass
from shared.data_access_objects.category_checking import CategoryCheckingDAO
from shared.models.category_checking import CategoryCheckingSchema
from shared.data_access_objects.transaction_detail import TransactionDetailDAO
from shared.models.transaction_detail import TransactionDetailSchema

@dataclass
class CategoryCheckingRepository:
    def save(self, document):
        #category_dao = CategoryCheckingDAO('dev')
        #category_dao.save(document)
        print("LE DOCUMENT")
        #print(document)
        category_checking_schema = CategoryCheckingSchema()
        category_document = category_checking_schema.dump(document)
        print("************8")
        print(category_document)
        print("OOOOOOOOOOOOOOOOOOOOOPA")
        category_dao = CategoryCheckingDAO('dev')
        category_document['id'] = 'teste_id'
        category_document['report_id'] = 'report_id'
        category_dao.save(category_document)
        print("SAVED@@@@@@")

    def getReportById(self, report_id):
        pass

