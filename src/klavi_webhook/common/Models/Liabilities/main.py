from dataclasses import dataclass, field
from typing import List, Optional

from Models.Bank import Creditcard
from app.Models import Income
from app.Models.Bank.BankAccount import BankAccount
from app.Models.Checking import Categorychecking
from app.Models.FinancialInsight import FinancialInsight


@dataclass
class Transaction:
    date: str
    amount: float
    description: str
    balance: Optional[float]
    category: Optional[str]


@dataclass
class Stream:
    bank: BankAccount
    last_30_days: float
    last_60_days: float
    last_90_days: float
    last_180_days: float
    days_covered: Optional[int]


@dataclass
class Liabilities:
    bank: BankAccount
    days_covered: int
    number_of_liability_streams: int
    total_liabilities: Stream
    liabilitystream: List[Transaction]

    @classmethod
    def from_payload(cls, payload):
        bank = BankAccount(
            holder_name=payload["account_holder"],
            number=payload["account_number"],
            branch=payload["agency_number"],
            bacen_id=payload["bacen_id"],
            bacen_name=payload["bacen_name"],
            bank_name=payload["bank_name"],
            cpf_verified=payload["cpf_verified"]
        )

        def map_liabilities(liabilities_payload):
            return Stream(
                bank=bank,
                last_30_days=liabilities_payload["total_liabilities_last_30_days"],
                last_60_days=liabilities_payload["total_liabilities_last_60_days"],
                last_90_days=liabilities_payload["total_liabilities_last_90_days"],
                last_180_days=liabilities_payload["total_liabilities_last_180_days"],
                days_covered=payload["days_covered"]
            )

        return cls(
            bank=bank,
            days_covered=payload["days_covered"],
            number_of_liability_streams=payload["number_of_liability_streams"],
            total_liabilities=map_liabilities(payload),
            liabilitystream=payload["liabilityStream"]
        )


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
        self.financial_insight = [FinancialInsight(**fi) for fi in self.data.get('financial_insight',{})]
        self.category_checking = [Categorychecking.from_dict(item) for item in self.data.get("Category_checking", [])]
        self.liabilities = [Liabilities.from_payload(fi) for fi in self.data.get('Liabilities')]


if __name__ == '__main__':
    payload_event = {
        "report_time": "2022-03-03 12:52:13",
        "data": {
            "enquiry_cpf": "12345678901",
            "user_consent": "Yes",
            "allow_autoupdate": "Yes",
            "connection_key": "gPuKXrCJU0kUDQO65J4k",
            "connection_id": "f45c899f-11eb-231f-97c4-4b2c16484587",
            "institution_id": "033",
            "report_type": "liabilities",
            "report_id": "4b2c1648-231f-11eb-97c4-f45c899f4592",
            "report_version": "V1.1",
            "Liabilities": [
                {
                    "account_holder": "JOHN DOE",
                    "account_number": "01.12345.4",
                    "agency_number": "1076",
                    "bacen_id": "033",
                    "bacen_name": "BANCO SANTANDER (BRASIL) S.A.",
                    "bank_name": "Santander",
                    "cpf_verified": "01234567890",
                    "days_covered": 180,
                    "number_of_liability_streams": 1,
                    "total_liabilities_last_180_days": 17.25,
                    "total_liabilities_last_30_days": 0,
                    "total_liabilities_last_60_days": 0,
                    "total_liabilities_last_90_days": 0,
                    "liabilityStream": [
                        {
                            "liability_stream_type": "Credit card",
                            "liabilityTransactions": [
                                {
                                    "trans_date": "2021-11-22",
                                    "trans_amount": -17.25,
                                    "trans_description": "CARTAO CX"
                                }
                            ]
                        }
                    ]
                },
                {
                    "account_holder": "JOHN DOE",
                    "account_number": "01.23456.2",
                    "agency_number": "1076",
                    "bacen_id": "033",
                    "bacen_name": "BANCO SANTANDER (BRASIL) S.A.",
                    "bank_name": "Santander",
                    "cpf_verified": "01234567890",
                    "days_covered": 180,
                    "number_of_liability_streams": 1,
                    "total_liabilities_last_180_days": 37.25,
                    "total_liabilities_last_30_days": 0,
                    "total_liabilities_last_60_days": 0,
                    "total_liabilities_last_90_days": 37.25,
                    "liabilityStream": [
                        {
                            "liability_stream_type": "Credit card",
                            "liabilityTransactions": [
                                {
                                    "trans_date": "2021-12-22",
                                    "trans_amount": -37.25,
                                    "trans_description": "CARTAO CX"
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }
    p = Payload(**payload_event)
