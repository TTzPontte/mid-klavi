from shared.models.financial_insight import FinancialInsightSchema, FinancialCashflowAnalisysSchema, FinancialCreditAnalisysSchema, FinancialCreditCardSpendingSchema, FinancialProfileSchema


import pandas


def export_financial_insight_to_excel(report, writer):
    financial_insight_schema = FinancialInsightSchema()
    cashflow_analysis_schema = FinancialCashflowAnalisysSchema()
    credit_analysis_schema = FinancialCreditAnalisysSchema()
    creditcard_spending_schema = FinancialCreditCardSpendingSchema()
    financial_profile_schema = FinancialProfileSchema()

    financial_insights = []
    cashflow_analysis  = []
    credit_analysis = []
    creditcard_spendings = []
    financial_profiles = []


    for financial_insight in report.financial_insights:
        financial_insights.append(financial_insight_schema.dump(financial_insight))
        for cashflow_analysi in financial_insight.cashflow_analysis:
            cashflow_analysis.append(cashflow_analysis_schema.dump(cashflow_analysi))
        for credit_analysi in financial_insight.credit_analysis:
            credit_analysis.append(credit_analysis_schema.dump(credit_analysi))
        for creditcard_spending in financial_insight.creditcard_spendings:
            creditcard_spendings.append(creditcard_spending_schema.dump(creditcard_spending))
        for financial_profile in financial_insight.financial_profiles:
            financial_profiles.append(financial_profile_schema.dump(financial_profile))



    data_frame_financial_insight = pandas.DataFrame(financial_insights)
    data_frame_cashflow_analysis = pandas.DataFrame(cashflow_analysis)
    data_frame_credit_analysis = pandas.DataFrame(credit_analysis)
    data_frame_creditcard_spendings = pandas.DataFrame(creditcard_spendings)
    data_frame_financial_profiles = pandas.DataFrame(financial_profiles)

    data_frame_financial_insight.to_excel(writer, sheet_name="Financial Insights")
    data_frame_cashflow_analysis.to_excel(writer, sheet_name="Cashflow Analysis")
    data_frame_credit_analysis.to_excel(writer, sheet_name="Credit Analysis")
    data_frame_creditcard_spendings.to_excel(writer, sheet_name="Creditcard Spendings")
    data_frame_financial_profiles.to_excel(writer, sheet_name="Financial Profiles")

