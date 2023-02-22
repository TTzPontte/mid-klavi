from dataclasses import dataclass
from shared.data_access_objects.financial_insights import FinancialInsightsDAO
from shared.data_access_objects.financial_profile import FinancialProfileDAO
from shared.data_access_objects.credit_analysis import CreditAnalisysDAO
from shared.data_access_objects.creditcard_spending import CreditCardSpendingDAO
from shared.data_access_objects.cashflow_analysis import CashflowAnalysisDAO

from shared.models.financial_insight import FinancialInsightSchema, FinancialCashflowAnalisysSchema, FinancialCreditAnalisysSchema, FinancialCreditCardSpendingSchema, FinancialProfileSchema
from shared.models.financial_insight import FinancialInsight, FinancialProfile, FinancialCreditAnalisys, FinancialCreditCardSpending, FinancialCashflowAnalysis


@dataclass
class FinancialInsightRepository:
    def save(self, document):
        financial_insight_schema = FinancialInsightSchema()
        cashflow_analysis_schema = FinancialCashflowAnalisysSchema()
        credit_analysis_schema = FinancialCreditAnalisysSchema()
        creditcard_spending_schema = FinancialCreditCardSpendingSchema()
        financial_profile_schema = FinancialProfileSchema()

        financial_insight_document = financial_insight_schema.dump(document)

        cashflow_analysis_ids = []
        for cashflow_analysis in document.cashflow_analysis:
            cashflow_analysis_ids.append(str(cashflow_analysis.id))
        financial_insight_document['cashflow_analysis'] = cashflow_analysis_ids

        credit_analysis_ids = []
        for credit_analysis in document.credit_analysis:
            credit_analysis_ids.append(str(credit_analysis.id))
        financial_insight_document['credit_analysis'] = credit_analysis_ids

        creditcard_spendings_ids = []
        for creditcard_spending in document.creditcard_spendings:
            creditcard_spendings_ids.append(str(creditcard_spending.id))
        financial_insight_document['creditcard_spendings'] = creditcard_spendings_ids

        financial_profile_ids = []
        for financial_profile in document.financial_profiles:
            financial_profile_ids.append(str(financial_profile.id))
        financial_insight_document['financial_profiles'] = financial_profile_ids


        financial_insight_dao = FinancialInsightsDAO('dev')
        financial_insight_dao.save(financial_insight_document)

        cashflow_analisy_dao = CashflowAnalysisDAO('dev')
        for cashflow_analisy in document.cashflow_analysis:
            cashflow_analisy_data = cashflow_analysis_schema.dump(cashflow_analisy)
            cashflow_analisy_data['category_id'] = str(document.id)
            cashflow_analisy_dao.save(cashflow_analisy_data)

        credit_analysis_dao = CreditAnalisysDAO('dev')
        for credit_analisy in document.credit_analysis:
            credit_analisy_data = credit_analysis_schema.dump(credit_analisy)
            credit_analisy_data['category_id'] = str(document.id)
            credit_analysis_dao.save(credit_analisy_data)

        creditcard_spending_dao = CreditCardSpendingDAO('dev')
        for credicard_spending in document.creditcard_spendings:
            credicard_spending_data = creditcard_spending_schema.dump(credicard_spending)
            credicard_spending_data['category_id'] = str(document.id)
            creditcard_spending_dao.save(credicard_spending_data)

        financial_profile_dao = FinancialProfileDAO('dev')
        for financial_profile in document.financial_profiles:
            financial_profile_data = financial_profile_schema.dump(financial_profile)
            financial_profile_data['category_id'] = str(document.id)
            financial_profile_dao.save(financial_profile_data)


        print("SAVED@@@@@@")

    def getByReportId(self, report_id):
        financial_insight_dao = FinancialInsightsDAO('dev')
        cashflow_analisy_dao = CashflowAnalysisDAO('dev')
        credit_analysis_dao = CreditAnalisysDAO('dev')
        creditcard_spending_dao = CreditCardSpendingDAO('dev')
        financial_profile_dao = FinancialProfileDAO('dev')


        financial_insight_obj = financial_insight_dao.get(report_id)
        financial_insight = FinancialInsight(**financial_insight_obj)
        financial_insight.cashflow_analysis = []
        financial_insight.credit_analysis = []
        financial_insight.creditcard_spendings = []
        financial_insight.financial_profiles = []

        for cashflow_analysis_id in financial_insight_obj['cashflow_analysis']:
            print("CASHFOID")
            print({'id': cashflow_analysis_id, 'category_id': str(financial_insight.id)})
            cashflow_analysis_obj = cashflow_analisy_dao.get({'id': cashflow_analysis_id, 'category_id': str(financial_insight.id)})
            financial_insight.cashflow_analysis.append(FinancialCashflowAnalysis(**cashflow_analysis_obj))

        for credit_analysis_id in financial_insight_obj['credit_analysis']:
            credit_analysis_obj = credit_analysis_dao.get({'id': credit_analysis_id, 'category_id': str(financial_insight.id)})
            financial_insight.credit_analysis.append(FinancialCreditAnalisys(**credit_analysis_obj))

        for creditcard_spending_id in financial_insight_obj['creditcard_spendings']:
            creditcard_spending_obj = creditcard_spending_dao.get({'id': creditcard_spending_id, 'category_id': str(financial_insight.id)})
            financial_insight.creditcard_spendings.append(FinancialCreditCardSpending(**creditcard_spending_obj))

        for financial_profile_id in financial_insight_obj['financial_profiles']:
            financial_profile_obj = financial_profile_dao.get({'id': financial_profile_id, 'category_id': str(financial_insight.id)})
            financial_insight.financial_profiles.append(FinancialProfile(**financial_profile_obj))


        return financial_insight

#[{"S":"d639e95b-065b-4ada-928c-691f590a57b1"}]