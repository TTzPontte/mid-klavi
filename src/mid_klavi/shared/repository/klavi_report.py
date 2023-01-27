from dataclasses import dataclass
from shared.data_access_objects.category_checking import CategoryCheckingDAO
from shared.data_access_objects.klavi_report import KlaviReportDAO
from shared.models.klavi_report import KlaviReportSchema, KlaviReport
from shared.models.category_checking import CategoryCheckingSchema, CategoryChecking
from shared.data_access_objects.transaction_detail import TransactionDetailDAO
from shared.models.transaction_detail import TransactionDetailSchema

@dataclass
class KlaviReportRepository:
    def save(self, document):
        klavi_report_data = parse_klavi_report_payload_body(payload)
        print(klavi_report_data)
        print("#########################################")
        klavi_report = KlaviReport(**klavi_report_data)
        category_checking_repository = CategoryCheckingRepository()
        if klavi_report_data.get('report_type') == "category_checking":
            category_checkings = []
            for category_checking_payload in payload.get('data').get("Category_checking"):
                category_checking = build_category_checking_from_kavli_payload(category_checking_payload)
                category_checkings.append(category_checking)
                category_checking_repository.save(category_checking)
        print("Le Klavi Report")
        print(klavi_report)
        print("Le Category Checkings")
        print(category_checkings)
        repository = KlaviReportRepository()
        repository.save(klavi_report)

    def getByReportId(self, report_id):
        report_klavi_dao = KlaviReportDAO('dev')
        report = report_klavi_dao.get(report_id)
        klavi_report = KlaviReport(**report)

        if (klavi_report.report_type == 'category_checking'):
            category_checking_dao = CategoryCheckingDAO('dev')
            #for category_checking_id in report.get('category_checking'):
            category_checking_obj = category_checking_dao.get({'id': 'teste_id', 'report_id': 'report_id'})
            print("PORRA JUVENAL")
            #print(category_checking_obj)
            category_checking = CategoryChecking(**category_checking_obj)
            klavi_report.category_checking.append(category_checking)


        print("############")
        print(klavi_report)
        print("OOOPOA")
        
        return klavi_report

