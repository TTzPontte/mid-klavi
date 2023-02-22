from dataclasses import dataclass, field
from typing import Optional, List

from marshmallow_dataclass import dataclass

from Models.Bank import Creditcard


@dataclass
class FinancialProfile:
    additional_overdraft_interest: float
    atm_withdrawal: float
    has_inss: str
    has_iptu_payment: str
    has_ipva_payment: str
    has_returned_cheque: str
    has_severance: str
    iof: float
    overdraft_interest: float


@dataclass
class CashflowAnalysis:
    checking_account_balance: float
    avg_daily_balance_last_180_days: float
    avg_daily_balance_last_30_days: float
    avg_daily_balance_last_60_days: float
    avg_daily_balance_last_90_days: float
    inflow_last_180_days: float
    inflow_last_30_days: float
    inflow_last_60_days: float
    inflow_last_90_days: float
    outflow_last_180_days: float
    outflow_last_30_days: float
    outflow_last_60_days: float
    outflow_last_90_days: float
    saving_account_balance: float


@dataclass
class CreditAnalysis:
    overdraft_limit: float
    preapproved_loan: float

@dataclass
class CreditcardSpending:
    creditcard: Creditcard
    closed_bills_covered: int
    open_bill_balance: float
    last_closed_bill: float
    avg_last_3_closed_bills: float
    days_covered: int
    has_late_payment: str
    pay_bills_in_installment: str


@dataclass
class FinancialInsight:
    bacen_id: str
    bacen_name: str
    bank_name: str
    agency_number: str
    account_number: str
    cpf_verified: str
    account_holder: str
    days_covered: int
    cashflow_analysis: CashflowAnalysis
    credit_analysis: list[CreditAnalysis]
    creditcard_spending: CreditcardSpending
    financial_profile: FinancialProfile
