from dataclasses import dataclass, field
import marshmallow_dataclass
from shared.data_access_objects.cashflow_analisys import CashflowAnalisysDAO
from shared.data_access_objects.financial_insight import FinancialInsightDAO
from shared.data_access_objects.credit_analisys import CreditAnalisysDAO
from shared.data_access_objects.financial_profile import FinancialProfileDAO
from shared.data_access_objects.creditcard_spending import CreditCardSpendingDAO


@dataclass
class FinancialInsight:
    id: str = ""
    bacen_id: str = ""
    bacen_name: str = ""
    bank_name: str = ""
    agency_number: str = ""
    account_number: str = ""
    cpf_verified: str = ""
    account_holder: str = ""
    days_covered: str = ""
    cashflow_analysis: list = field(default_factory=list)
    credit_analysis: list = field(default_factory=list)
    creditcard_spending: list = field(default_factory=list)
    financial_profile: list = field(default_factory=list)


FinancialInsightSchema = marshmallow_dataclass.class_schema(FinancialInsight)

@dataclass
class FinancialCashflowAnalisys:
    id: str = ""
    checking_account_balance: str = ""
    avg_daily_balance_last_180_days: str = ""
    avg_daily_balance_last_30_days: str = ""
    avg_daily_balance_last_60_days: str = ""
    avg_daily_balance_last_90_days: str = ""
    inflow_last_180_days: str = ""
    inflow_last_30_days: str = ""
    inflow_last_60_days: str = ""
    inflow_last_90_days: str = ""
    outflow_last_180_days: str = ""
    outflow_last_30_days: str = ""
    outflow_last_60_days: str = ""
    outflow_last_90_days: str = ""
    saving_account_balance: str = ""


FinancialCashflowAnalisysSchema = marshmallow_dataclass.class_schema(FinancialCashflowAnalisys)


@dataclass
class FinancialCreditAnalisys:
    id: str = ""
    overdraft_limit: str = ""
    preapproved_loan: str = ""


FinancialCreditAnalisysSchema = marshmallow_dataclass.class_schema(FinancialCreditAnalisys)


@dataclass
class FinancialCreditCardSpending:
    id: str = ""
    card_holder: str = ""
    card_last_4_digit: str = ""
    card_type: str = ""
    credit_limit: str = ""
    closed_bills_covered: str = ""
    open_bill_balance: str = ""
    last_closed_bill: str = ""
    avg_last_3_closed_bills: str = ""
    days_covered: str = ""
    has_late_payment: str = ""
    pay_bills_in_installment: str = ""


FinancialCreditCardSpendingSchema = marshmallow_dataclass.class_schema(FinancialCreditCardSpending)


@dataclass
class FinancialProfile:
    id: str = ""
    additional_overdraft_interest: str = ""
    atm_withdrawal: str = ""
    has_iptu_payment: str = ""
    has_ipva_payment: str = ""
    has_returned_cheque: str = ""
    has_severance: str = ""
    iof: str = ""
    overdraft_interest: str = ""


FinancialProfileSchema = marshmallow_dataclass.class_schema(FinancialProfile)
