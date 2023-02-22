from dataclasses import field
from typing import Optional, List

from marshmallow import Schema, fields
from marshmallow_dataclass import dataclass


@dataclass
class Bankaccount:
    id: str
    bank_name: str
    bacen_name: str
    branch: str
    bacen_id: str
    cpf_verified: str
    holder_name: str
    operation_code: str
    balance: float
    number: float
    bank_id: str
    report_id: str


@dataclass
class Transaction:
    date: str
    amount: float
    description: str
    balance: float
    category: str


@dataclass
class Creditcard:
    card_last4num: str
    holder_name: str
    card_type: str
    credit_limit: float
    available_limit: float
    agency_number: str
    bank_account: str
    is_active: bool
    is_vip: bool
    open_statements: int
    cpf_verified: str
    closed_statements: int
    bank: Optional[Bankaccount]


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


@dataclass
class Categorychecking:
    bank: Bankaccount
    transactions: Optional[list[Transaction]] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict):
        bank = Bankaccount(**data['bank_data'])
        transactions = [Transaction(**trans) for trans in data.get('transactiondetail', [])]
        return cls(bank=bank, transactions=transactions)


@dataclass
class Incomestream:
    first_income_day: str
    second_income_day: str
    income_transactions: list[Transaction]
    income_stream_type: str


@dataclass
class Income:
    bank: Bankaccount
    days_covered: int
    number_of_income_streams: int
    total_income_last_180_days: int
    total_income_last_30_days: int
    total_income_last_60_days: int
    total_income_last_90_days: int
    income_stream: list[Incomestream]


@dataclass
class LiabilityTransactions:
    liability_stream_type: str
    trans_date: str
    trans_amount: float
    trans_description: str


@dataclass
class Liabilities:
    bank: Bankaccount
    days_covered: int
    number_of_liability_streams: int
    total_liabilities_last_180_days: float
    total_liabilities_last_30_days: float
    total_liabilities_last_60_days: float
    total_liabilities_last_90_days: float
    liabilitystream: List[LiabilityTransactions]


@dataclass
class Payload:
    report_time: str
    data: dict
    enquiry_cpf: Optional[str] = None
    user_consent: Optional[str] = None
    allow_autoupdate: Optional[str] = None
    connection_key: Optional[str] = None
    connection_id: Optional[str] = None
    institution_id: Optional[str] = None
    report_type: Optional[str] = None
    report_id: Optional[str] = None
    report_version: Optional[str] = None
    category_checking: Optional[list[Categorychecking]] = field(default_factory=list)
    credit_cards: Optional[list[Creditcard]] = field(default_factory=list)
    income: Optional[list[Income]] = field(default_factory=list)
    financial_insight: Optional[list[FinancialInsight]] = field(default_factory=list)
    liabilities: Optional[list[Liabilities]] = field(default_factory=list)

    def __post_init__(self):
        data = self.data
        self.enquiry_cpf = data.get('enquiry_cpf')
        self.user_consent = data.get('user_consent')
        self.allow_autoupdate = data.get('allow_autoupdate')
        self.connection_key = data.get('connection_key')
        self.connection_id = data.get('connection_id')
        self.institution_id = data.get('institution_id')
        self.report_type = data.get('report_type')
        self.report_id = data.get('report_id')
        self.report_version = data.get('report_version')
        self.financial_insight = [FinancialInsight(**fi) for fi in self.data.get('financial_insight')]
        self.category_checking = [Categorychecking.from_dict(item) for item in self.data.get("Category_checking", [])]
        self.liabilities = [Liabilities(**fi) for fi in self.data.get('Liabilities')]
