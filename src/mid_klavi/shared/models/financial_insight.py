from dataclasses import dataclass
from marshmallow import Schema, fields
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


    def __post_init__(self):
        print("ON POST INIT")
        self.schema = FinancialInsightSchema()

    def save(self):
        dao = FinancialInsightDAO('dev')
        dao.save(self.schema.dump(self))
        print("Object Saved")


class FinancialInsightSchema(Schema):
    id: fields.Str()
    bacen_id: fields.Str()
    bacen_name: fields.Str()
    bank_name: fields.Str()
    agency_number: fields.Str()
    account_number: fields.Str()
    cpf_verified: fields.Str()
    account_holder: fields.Str()
    days_covered: fields.Str()


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


    def __post_init__(self):
        print("ON POST INIT")
        self.schema = FinancialCashflowAnalisysSchema()

    def save(self):
        dao = CashflowAnalisysDAO('dev')
        dao.save(self.schema.dump(self))
        print("Object Saved")
        
        
class FinancialCashflowAnalisysSchema(Schema):
    id: fields.Str()
    checking_account_balance: fields.Str()
    avg_daily_balance_last_180_days: fields.Str()
    avg_daily_balance_last_30_days: fields.Str()
    avg_daily_balance_last_60_days: fields.Str()
    avg_daily_balance_last_90_days: fields.Str()
    inflow_last_180_days: fields.Str()
    inflow_last_30_days: fields.Str()
    inflow_last_60_days: fields.Str()
    inflow_last_90_days: fields.Str()
    outflow_last_180_days: fields.Str()
    outflow_last_30_days: fields.Str()
    outflow_last_60_days: fields.Str()
    outflow_last_90_days: fields.Str()
    saving_account_balance: fields.Str()


@dataclass
class FinancialCreditAnalisys:
    id: str = ""
    overdraft_limit: str = ""
    preapproved_loan: str = ""

    def __post_init__(self):
        print("ON POST INIT")
        self.schema = FinancialCreditAnalisysSchema()

    def save(self):
        dao = CreditAnalisysDAO('dev')
        dao.save(self.schema.dump(self))
        print("Object Saved")

class FinancialCreditAnalisysSchema(Schema):
    id: fields.Str()
    overdraft_limit: fields.Str()
    preapproved_loan: fields.Str()


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

    def __post_init__(self):
        print("ON POST INIT")
        self.schema = FinancialCreditCardSpendingSchema()

    def save(self):
        dao = CreditCardSpendingDAO('dev')
        dao.save(self.schema.dump(self))
        print("Object Saved")


class FinancialCreditCardSpendingSchema(Schema):
    id: fields.Str()
    card_holder: fields.Str()
    card_last_4_digit: fields.Str()
    card_type: fields.Str()
    credit_limit: fields.Str()
    closed_bills_covered: fields.Str()
    open_bill_balance: fields.Str()
    last_closed_bill: fields.Str()
    avg_last_3_closed_bills: fields.Str()
    days_covered: fields.Str()
    has_late_payment: fields.Str()
    pay_bills_in_installment: fields.Str()


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

    def __post_init__(self):
        print("ON POST INIT")
        self.schema = FinancialProfileSchema()

    def save(self):
        dao = FinancialProfileDAO('dev')
        dao.save(self.schema.dump(self))
        print("Object Saved")


class FinancialProfileSchema(Schema):
    id: fields.Str()
    additional_overdraft_interest: fields.Str()
    atm_withdrawal: fields.Str()
    has_iptu_payment: fields.Str()
    has_ipva_payment: fields.Str()
    has_returned_cheque: fields.Str()
    has_severance: fields.Str()
    iof: fields.Str()
    overdraft_interest: fields.Str()

