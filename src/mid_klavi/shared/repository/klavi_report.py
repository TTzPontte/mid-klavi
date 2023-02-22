from dataclasses import dataclass
from shared.data_access_objects.category_checking import CategoryCheckingDAO
from shared.data_access_objects.klavi_report import KlaviReportDAO
from shared.models.klavi_report import KlaviReportSchema, KlaviReport
from shared.models.category_checking import CategoryCheckingSchema, CategoryChecking
from shared.repository.category_checking import CategoryCheckingRepository
from shared.repository.category_creditcard import CategoryCreditCardRepository
from shared.repository.liability import LiabilityRepository
from shared.repository.financial_insight import FinancialInsightRepository

from shared.data_access_objects.transaction_detail import TransactionDetailDAO
from shared.models.transaction_detail import TransactionDetailSchema

@dataclass
class KlaviReportRepository:
    def save(self, klavi_report):
        print("KLAVI REPORT")
        print(klavi_report)
        print("++++++++++++++++++++++++++")
        klavi_report_schema = KlaviReportSchema()
        klavi_report_dao = KlaviReportDAO('dev')
        klavi_report_document = klavi_report_schema.dump(klavi_report)

        category_checkings_ids = []
        for category_checking in klavi_report.category_checkings:
            category_checkings_ids.append(str(category_checking.id))
        klavi_report_document['category_checkings'] = category_checkings_ids

        category_creditcard_ids = []
        for category_creditcard in klavi_report.category_creditcards:
            category_creditcard_ids.append(str(category_creditcard.id))
        klavi_report_document['category_creditcards'] = category_creditcard_ids

        liabilities_ids = []
        for liability in klavi_report.liabilities:
            liabilities_ids.append(str(liability.id))
        klavi_report_document['liabilities'] = liabilities_ids

        financial_insight_ids = []
        for financial_insight in klavi_report.financial_insights:
            financial_insight_ids.append(str(financial_insight.id))
        klavi_report_document['financial_insights'] = financial_insight_ids

        klavi_report_dao.put(klavi_report_document)

        if klavi_report.report_type == "category_checking":
            category_checking_repository = CategoryCheckingRepository()
            for category_checking in klavi_report.category_checkings:
                category_checking.report_id = klavi_report.id
                category_checking_repository.save(category_checking)

        if klavi_report.report_type == "category_creditcard":
            category_creditcard_repository = CategoryCreditCardRepository()
            for category_creditcard in klavi_report.category_creditcards:
                category_creditcard.report_id = klavi_report.id
                category_creditcard_repository.save(category_creditcard)

        if klavi_report.report_type == "liabilities":
            liability_repository = LiabilityRepository()
            for liability in klavi_report.liabilities:
                liability.report_id = klavi_report.id
                liability_repository.save(liability)

        if klavi_report.report_type == "financial_insight":
            financial_insight_repository = FinancialInsightRepository()
            for financial_insight in klavi_report.financial_insights:
                financial_insight.report_id = klavi_report.id
                financial_insight_repository.save(financial_insight)

        print("SAVED@@@@@@")

    def getByReportId(self, report_id, enquiry_cpf):
        report_klavi_dao = KlaviReportDAO('dev')
        report = report_klavi_dao.get({'id': report_id, 'enquiry_cpf': enquiry_cpf})

        print("O REPORT")
        print(report)
        print("____________________----")
        klavi_report = KlaviReport(**report)
        klavi_report.category_checkings = []
        klavi_report.category_creditcards = []
        klavi_report.category_liabilites = []
        klavi_report.category_financial_insights = []
        category_checking_repository = CategoryCheckingRepository()
        category_creditcard_repository = CategoryCreditCardRepository()
        liabilities_repository = LiabilityRepository()
        financial_insight_repository = FinancialInsightRepository()


        if (klavi_report.report_type == 'category_checking'):
            for category_checking_id in report['category_checkings']:
                category_checking = category_checking_repository.getByReportId({'id': category_checking_id, 'report_id': report_id})
                klavi_report.category_checkings.append(category_checking)

        if (klavi_report.report_type == 'category_creditcard'):
            for category_creditcard_id in report['category_creditcards']:
                category_creditcard = category_creditcard_repository.getByReportId({'id': category_creditcard_id, 'report_id': report_id})
                klavi_report.category_creditcards.append(category_creditcard)

        if (klavi_report.report_type == 'liabilities'):
            klavi_report.liabilities = []
            for liability_id in report['liabilities']:
                print("POCJA KRALHO")
                print(liability_id)
                liability = liabilities_repository.getByReportId({'id': liability_id, 'report_id': report_id})
                klavi_report.liabilities.append(liability)
                print("DIACOS")
                print(report['liabilities'])
                print("Droga")
                print(klavi_report.liabilities)
                print("-|-|-|-|-|-|-|-|-|-_|_|_|_|_|_|_|_|_|_||_")

        if (klavi_report.report_type == 'financial_insight'):
            klavi_report.financial_insights = []
            for financial_insight_id in report['financial_insights']:
                financial_insight = financial_insight_repository.getByReportId({'id': financial_insight_id, 'report_id': report_id})
                klavi_report.financial_insights.append(financial_insight)

        print("############")
        print(klavi_report)
        print("OOOPOA")

        return klavi_report

