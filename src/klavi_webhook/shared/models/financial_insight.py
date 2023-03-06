from dataclasses import dataclass, field
from marshmallow import Schema
import marshmallow_dataclass
import uuid

@dataclass
class FinancialInsight:
    id: str = ""
    report_id: str = ""
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
    creditcard_spendings: list = field(default_factory=list)
    financial_profiles: list = field(default_factory=list)

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()

class BaseFinancialInsightSchema(Schema):
    class Meta:
        exclude = ('financial_profiles', 'cashflow_analysis', 'credit_analysis', 'creditcard_spendings')

FinancialInsightSchema = marshmallow_dataclass.class_schema(FinancialInsight, base_schema=BaseFinancialInsightSchema)

@dataclass
class FinancialCashflowAnalysis:
    id: str = ""
    category_id: str = ""
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

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()


FinancialCashflowAnalisysSchema = marshmallow_dataclass.class_schema(FinancialCashflowAnalysis)


@dataclass
class FinancialCreditAnalisys:
    id: str = ""
    category_id: str = ""
    overdraft_limit: str = ""
    preapproved_loan: str = ""

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()


FinancialCreditAnalisysSchema = marshmallow_dataclass.class_schema(FinancialCreditAnalisys)


@dataclass
class FinancialCreditCardSpending:
    id: str = ""
    category_id: str = ""
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

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()


FinancialCreditCardSpendingSchema = marshmallow_dataclass.class_schema(FinancialCreditCardSpending)


@dataclass
class FinancialProfile:
    id: str = ""
    category_id: str = ""
    additional_overdraft_interest: str = ""
    atm_withdrawal: str = ""
    has_iptu_payment: str = ""
    has_ipva_payment: str = ""
    has_returned_cheque: str = ""
    has_severance: str = ""
    has_inss: str = ""
    iof: str = ""
    overdraft_interest: str = ""

    def __post_init__(self):
        if self.id == "":
            self.id = uuid.uuid4()


FinancialProfileSchema = marshmallow_dataclass.class_schema(FinancialProfile)
