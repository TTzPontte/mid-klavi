from dataclasses import dataclass
from shared.data_access_objects.category_checking import CategoryCheckingDAO
from shared.data_access_objects.klavi_report import KlaviReportDAO
from shared.models.klavi_report import KlaviReportSchema, KlaviReport
from shared.models.category_checking import CategoryCheckingSchema, CategoryChecking
from shared.repository.category_checking import CategoryCheckingRepository
from shared.repository.category_creditcard import CategoryCreditCardRepository
from shared.repository.liability import LiabilityRepository
from shared.repository.financial_insight import FinancialInsightRepository
from shared.repository.income import IncomeRepository
from shared.repository.balance import BalanceRepository
from shared.repository.identity import IdentityRepository
from shared.repository.score_k1 import ScoreK1Repository
from shared.repository.risk_label import RiskLabelRepository
#from shared.data_access_objects.category_checking import Category

from shared.data_access_objects.transaction_detail import TransactionDetailDAO
from shared.models.transaction_detail import TransactionDetailSchema
import os
@dataclass
class KlaviReportRepository:
    def save(self, klavi_report):
        klavi_report_schema = KlaviReportSchema()
        klavi_report_dao = KlaviReportDAO()
        klavi_report_document = klavi_report_schema.dump(klavi_report)
        bucket_name = "klavi-{env}".format(env=os.getenv("ENV"))
        object_key = "{report_id}/{report_type}.xlsx".format(report_id=klavi_report_document["report_id"], report_type=klavi_report_document["report_type"])
        object_url = "https://{bucket_name}.s3.amazonaws.com/{object_key}".format(bucket_name=bucket_name, object_key=object_key)

        klavi_report_document["json_object"] = {
            "bucket_name": bucket_name,
            "object_key": object_key,
            "object_url": object_url
        }

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

        income_ids = []
        for income in klavi_report.income:
            income_ids.append(str(income.id))
        klavi_report_document['income'] = income_ids

        balance_ids = []
        for balance in klavi_report.balance:
            balance_ids.append(str(balance.id))
        klavi_report_document['balance'] = balance_ids

        if klavi_report.report_type == "identity":
            klavi_report_document['identity'] = str(klavi_report.identity.id)

        if klavi_report.report_type == "score_k1":
            klavi_report_document['score_k1'] = str(klavi_report.score_k1.id)

        if klavi_report.report_type == "k_label":
            klavi_report_document['risk_label'] = str(klavi_report.risk_label.id)


        klavi_report_dao.put(klavi_report_document)

        if klavi_report.report_type == "category_checking":
            category_checking_dao = CategoryCheckingDAO()
            for category_checking in klavi_report.category_checkings:
                category_checking.report_id = klavi_report.id
                category_checking_dao.save(category_checking)

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

        if klavi_report.report_type == "income":
            income_repository = IncomeRepository()
            for income in klavi_report.income:
                income.report_id = klavi_report.id
                income_repository.save(income)

        if klavi_report.report_type == "balance":
            balance_repository = BalanceRepository()
            for balance in klavi_report.balance:
                balance.report_id = klavi_report.id
                balance_repository.save(balance)

        if klavi_report.report_type == "score_k1":
            score_k1_repository = ScoreK1Repository()
            score_k1 = klavi_report.score_k1
            score_k1.report_id = klavi_report.id
            score_k1_repository.save(score_k1)

        if klavi_report.report_type == "identity":
            identity_repository = IdentityRepository()
            identity = klavi_report.identity
            identity.report_id = klavi_report.id
            identity_repository.save(identity)

        if klavi_report.report_type == "k_label":
            risk_label_repository = RiskLabelRepository()
            risk_label = klavi_report.risk_label
            risk_label.report_id = klavi_report.id
            risk_label_repository.save(risk_label)

    def getByReportId(self, report_id, enquiry_cpf):
        report_klavi_dao = KlaviReportDAO()
        report = report_klavi_dao.get({'id': report_id, 'enquiry_cpf': enquiry_cpf})

        klavi_report = KlaviReport(**report)
        klavi_report.category_checkings = []
        klavi_report.category_creditcards = []
        klavi_report.category_liabilites = []
        klavi_report.category_financial_insights = []
        klavi_report.income = []
        klavi_report.balance = []
        category_checking_repository = CategoryCheckingRepository()
        category_creditcard_repository = CategoryCreditCardRepository()
        liabilities_repository = LiabilityRepository()
        financial_insight_repository = FinancialInsightRepository()
        income_repository = IncomeRepository()
        balance_repository = BalanceRepository()
        identity_repository = IdentityRepository()
        score_k1_repository = ScoreK1Repository()
        risk_label_repository = RiskLabelRepository()


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
                liability = liabilities_repository.getByReportId({'id': liability_id, 'report_id': report_id})
                klavi_report.liabilities.append(liability)

        if (klavi_report.report_type == 'financial_insight'):
            klavi_report.financial_insights = []
            for financial_insight_id in report['financial_insights']:
                financial_insight = financial_insight_repository.getByReportId({'id': financial_insight_id, 'report_id': report_id})
                klavi_report.financial_insights.append(financial_insight)
                
        if (klavi_report.report_type == 'income'):
            klavi_report.income = []
            for income_id in report['income']:
                income = income_repository.getByReportId({'id': income_id, 'report_id': report_id})
                klavi_report.income.append(income)

        if (klavi_report.report_type == 'balance'):
            klavi_report.balance = []
            for balance_id in report['balance']:
                balance = balance_repository.getByReportId({'id': balance_id, 'report_id': report_id})
                klavi_report.balance.append(balance)

        if (klavi_report.report_type == 'identity'):
            identity = identity_repository.getByReportId({'id': report.identity, 'report_id': report_id})
            report.identity = identity

        if (klavi_report.report_type == 'score_k1'):
            score_k1 = score_k1_repository.getByReportId({'id': report.score_k1, 'report_id': report_id})
            report.score_k1 = score_k1

        if (klavi_report.report_type == 'k_label'):
            risk_label = risk_label_repository.getByReportId({'id': report.risk_label, 'report_id': report_id})
            report.risk_label = risk_label

                

        return klavi_report
