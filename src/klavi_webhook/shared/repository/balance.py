from dataclasses import dataclass
from shared.data_access_objects.balance import BalanceDAO
from shared.models.balance import BalanceSchema
from shared.models.balance import Balance


@dataclass
class BalanceRepository:
    def save(self, document):
        balance_schema = BalanceSchema()
        balance_document = balance_schema.dump(document)
        balance_dao = BalanceDAO()
        balance_dao.put(balance_document)

    def getByReportId(self, report_id):
        balance_dao = BalanceDAO()
        balance_obj = balance_dao.get(report_id)
        balance = Balance(**balance_obj)

        return balance
