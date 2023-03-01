from dataclasses import dataclass
from shared.data_access_objects.category_creditcard import CategoryCreditCardDAO
from shared.data_access_objects.open_statement import OpenStatementDAO
from shared.data_access_objects.closed_statement import ClosedStatementDAO
from shared.data_access_objects.transaction_detail import TransactionDetailDAO
from shared.models.category_creditcard import CategoryCreditCardSchema, OpenStatementSchema, ClosedStatementSchema
from shared.models.category_creditcard import CategoryCreditCard, OpenStatement, ClosedStatement
from shared.models.transaction_detail import TransactionDetail, TransactionDetailSchema


@dataclass
class CategoryCreditCardRepository:
    def save(self, document):
        category_creditcard_schema = CategoryCreditCardSchema()
        open_statement_schema = OpenStatementSchema()
        closed_statement_schema = ClosedStatementSchema()
        transaction_detail_schema = TransactionDetailSchema()
        category_document = category_creditcard_schema.dump(document)
        category_document['open_statement'] = str(document.open_statement.id)

        closed_statement_ids = []
        for closed_statement in document.closed_statements:
            closed_statement_ids.append(str(closed_statement.id))
        category_document['closed_statements'] = closed_statement_ids

        category_dao = CategoryCreditCardDAO()
        open_statement_dao = OpenStatementDAO()
        closed_statement_dao = ClosedStatementDAO()
        transaction_detail_dao = TransactionDetailDAO()
        category_dao.put(category_document)

        open_statement_data = open_statement_schema.dump(document.open_statement)
        open_statement_transaction_details_ids = []
        for transaction_detail in document.open_statement.transaction_details:
            transaction_detail_data = transaction_detail_schema.dump(transaction_detail)
            transaction_detail_data['category_id'] = str(document.open_statement.id)
            transaction_detail_dao.put(transaction_detail_data)
            open_statement_transaction_details_ids.append(str(transaction_detail.id))
        open_statement_data['category_id'] = str(document.id)
        open_statement_data['transaction_details'] = open_statement_transaction_details_ids
        open_statement_dao.put(open_statement_data)

        for closed_statement in document.closed_statements:
            closed_statement_data = closed_statement_schema.dump(closed_statement)
            closed_statement_data['category_id'] = str(document.id)
            transaction_detail_ids = []
            for transaction_detail in closed_statement.transaction_details:
                transaction_detail_data = transaction_detail_schema.dump(transaction_detail)
                transaction_detail_data['category_id'] = str(closed_statement.id)
                transaction_detail_dao.put(transaction_detail_data)
                transaction_detail_ids.append( str(transaction_detail.id) )

            closed_statement_data['transaction_details'] = transaction_detail_ids
            closed_statement_dao.put(closed_statement_data)

    def getByReportId(self, report_id):
        category_creditcard_dao = CategoryCreditCardDAO()
        open_statement_dao = OpenStatementDAO()
        closed_statement_dao = ClosedStatementDAO()
        transaction_detail_dao = TransactionDetailDAO()

        category_creditcard_obj = category_creditcard_dao.get(report_id)
        category_creditcard = CategoryCreditCard(**category_creditcard_obj)
        category_creditcard.closed_statements = []
        category_creditcard.closed_statements = []

        for closed_statement_id in category_creditcard_obj['closed_statements']:
            closed_statement_obj = closed_statement_dao.get(
                {'id': closed_statement_id, 'category_id': str(category_creditcard.id)})
            closed_statement = ClosedStatement(**closed_statement_obj)

            for transaction_detail_id in closed_statement_obj['transaction_details']:
                if isinstance(transaction_detail_id, str):
                    transaction_detail_obj = transaction_detail_dao.get(
                        {'id': transaction_detail_id, 'category_id': str(closed_statement.id)})
                    closed_statement.transaction_details.append(TransactionDetail(**transaction_detail_obj))
            category_creditcard.closed_statements.append(closed_statement)

        open_statement_obj = open_statement_dao.get({"id": category_creditcard_obj['open_statement'], "category_id": category_creditcard.id})
        print("OOOOPA MALUCO")
        print(open_statement_obj)
        open_statement = OpenStatement(**open_statement_obj)
        open_statement.transaction_details = []

        for transaction_detail_id in open_statement_obj['transaction_details']:
            transaction_detail_obj = transaction_detail_dao.get(
                {'id': transaction_detail_id, 'category_id': str(open_statement.id)})
            open_statement.transaction_details.append(TransactionDetail(**transaction_detail_obj))
        category_creditcard.open_statement = open_statement

        return category_creditcard
