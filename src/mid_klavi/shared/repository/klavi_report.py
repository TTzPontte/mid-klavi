from dataclasses import dataclass
from shared.data_access_objects.category_checking import CategoryCheckingDAO
from shared.data_access_objects.klavi_report import KlaviReportDAO
from shared.models.klavi_report import KlaviReportSchema, KlaviReport
from shared.models.category_checking import CategoryCheckingSchema, CategoryChecking
from shared.repository.category_checking import CategoryCheckingRepository
from shared.data_access_objects.transaction_detail import TransactionDetailDAO
from shared.models.transaction_detail import TransactionDetailSchema

@dataclass
class KlaviReportRepository:
    def save(self, klavi_report):
        klavi_report_schema = KlaviReportSchema()
        klavi_report_dao = KlaviReportDAO('dev')
        klavi_report_document = klavi_report_schema.dump(klavi_report)
        category_checkings_ids = []
        for category_checking in klavi_report.category_checkings:
            category_checkings_ids.append(str(category_checking.id))
        klavi_report_document['category_checkings'] = category_checkings_ids
        klavi_report_dao.put(klavi_report_document)

        if klavi_report.report_type == "category_checking":
            category_checking_repository = CategoryCheckingRepository()
            for category_checking in klavi_report.category_checkings:
                category_checking.report_id = klavi_report.id
                category_checking_repository.save(category_checking)

        print("SAVED@@@@@@")

    def getByReportId(self, report_id, enquiry_cpf):
        report_klavi_dao = KlaviReportDAO('dev')
        report = report_klavi_dao.get({'id': report_id, 'enquiry_cpf': enquiry_cpf})
        klavi_report = KlaviReport(**report)
        klavi_report.category_checkings = []
        category_checking_repository = CategoryCheckingRepository()


        if (klavi_report.report_type == 'category_checking'):
            for category_checking_id in report['category_checkings']:
                category_checking = category_checking_repository.getByReportId({'id': category_checking_id, 'report_id': report_id})
                klavi_report.category_checkings.append(category_checking)

        print("############")
        print(klavi_report)
        print("OOOPOA")

        return klavi_report

