from dataclasses import dataclass, field
from io import BytesIO
from typing import List, Optional, Dict

import pandas as pd

from .BankAccount import BankAccount, Transaction
from .IncomeStream import IncomeStream
from .s3_helper import S3Helper


@dataclass
class CategoryChecking:
    bank_account: BankAccount
    operation_code: str
    transactions: List[Transaction] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, str]):
        bank_account = BankAccount.from_dict(data)
        transactions = [Transaction(**t) for t in data.get('TransactionDetail', [])]
        return cls(bank_account=bank_account, operation_code=data['operation_code'], transactions=transactions)


@dataclass
class Income:
    bank: BankAccount
    days_covered: int
    number_of_income_streams: int
    total_income_last_180_days: int
    total_income_last_30_days: int
    total_income_last_60_days: int
    total_income_last_90_days: int
    income_stream: List[IncomeStream]

    @classmethod
    def from_dict(cls, data: dict):
        bank = BankAccount(holder_name=data["account_holder"], account=data["account_number"],
                           bank_branch=data["agency_number"], bacen_id=data["bacen_id"], bacen_name=data["bacen_name"],
                           bank_name=data["bank_name"], cpf_verified=data["cpf_verified"])
        income_streams = [IncomeStream.from_dict(stream_data) for stream_data in data.get("incomeStream", [])]
        return cls(bank=bank, days_covered=data["days_covered"],
                   number_of_income_streams=data["number_of_income_streams"],
                   total_income_last_180_days=data["total_income_last_180_days"],
                   total_income_last_30_days=data["total_income_last_30_days"],
                   total_income_last_60_days=data["total_income_last_60_days"],
                   total_income_last_90_days=data["total_income_last_90_days"], income_stream=income_streams)

    def to_dict(self):
        return {"bank": self.bank.to_dict(), "days_covered": self.days_covered,
                "number_of_income_streams": self.number_of_income_streams,
                "total_income_last_180_days": self.total_income_last_180_days,
                "total_income_last_30_days": self.total_income_last_30_days,
                "total_income_last_60_days": self.total_income_last_60_days,
                "total_income_last_90_days": self.total_income_last_90_days,
                "income_stream": [stream.to_dict() for stream in self.income_stream]}


@dataclass
class Parser:
    report_time: str
    data: Dict[str, str]
    code: Optional[int] = None
    msg: Optional[str] = None
    enquiry_cpf: Optional[str] = None
    user_consent: Optional[str] = None
    allow_autoupdate: Optional[str] = None
    connection_key: Optional[str] = None
    connection_id: Optional[str] = None
    institution_id: Optional[str] = None
    report_type: Optional[str] = None
    report_id: Optional[str] = None
    report_version: Optional[str] = None
    category_checking: Optional[List[CategoryChecking]] = field(default_factory=list)
    income: Optional[List[Income]] = field(default_factory=list)

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
        self.category_checking = [CategoryChecking.from_dict(item) for item in data.get("Category_checking", [])]
        self.income = [Income.from_dict(item) for item in data.get("Income", []) or []]

    def to_dict(self):
        return {"report_time": self.report_time,
                "data": {"enquiry_cpf": self.enquiry_cpf, "user_consent": self.user_consent,
                         "allow_autoupdate": self.allow_autoupdate, "connection_key": self.connection_key,
                         "connection_id": self.connection_id, "institution_id": self.institution_id,
                         "report_type": self.report_type, "report_id": self.report_id,
                         "report_version": self.report_version, }, "code": self.code, "msg": self.msg}

    def create_category_checking_excel(self) -> BytesIO:
        # Create dataframe for accounts sheet
        accounts_data = []
        for cc in self.category_checking:
            account_data = cc.bank_account.to_dict()
            account_data.update({"operation_code": cc.operation_code})
            accounts_data.append(account_data)
        accounts_df = pd.DataFrame(accounts_data)

        # Create dataframe for transactions sheet
        transaction_data = []
        for cc in self.category_checking:
            for t in cc.transactions:
                transaction_data.append({"bank_name": cc.bank_account.bank_name,
                                         "bacen_name": cc.bank_account.bacen_name,
                                         "bacen_id": cc.bank_account.bacen_id,
                                         "bank_branch": cc.bank_account.bank_branch,
                                         "account": cc.bank_account.account,
                                         "operation_code": cc.operation_code,
                                         "cpf_verified": cc.bank_account.cpf_verified,
                                         "holder_name": cc.bank_account.holder_name,
                                         "balance": t.balance,
                                         "trans_date": t.trans_date,
                                         "trans_amount": t.trans_amount,
                                         "trans_description": t.trans_description,
                                         "category": t.category})
        transaction_df = pd.DataFrame(transaction_data)

        # Create excel buffer
        excel_buffer = BytesIO()
        with pd.ExcelWriter(excel_buffer) as writer:
            # Write payload data to "Payload" sheet
            payload_data = {"enquiry_cpf": self.enquiry_cpf,
                            "user_consent": self.user_consent,
                            "allow_autoupdate": self.allow_autoupdate,
                            "connection_key": self.connection_key,
                            "connection_id": self.connection_id,
                            "institution_id": self.institution_id,
                            "report_type": self.report_type,
                            "report_id": self.report_id,
                            "report_version": self.report_version}
            payload_df = pd.DataFrame([payload_data])
            payload_df.to_excel(writer, sheet_name="Payload", index=False)

            # Write account data to "Accounts" sheet
            accounts_df.to_excel(writer, sheet_name="Accounts", index=False)

            # Write transaction data to "Transactions" sheet
            transaction_df.to_excel(writer, sheet_name="Transactions", index=False)

        # Reset buffer position and return it
        excel_buffer.seek(0)
        return excel_buffer

    def category_checking_to_excel(self, file_name: str):
        if not self.category_checking:
            print("No CategoryChecking data to export.")
            return

        # Create Excel buffer
        excel_buffer = self.create_category_checking_excel()

        # Upload to S3
        s3_helper = S3Helper()
        s3_helper.save_to_s3(excel_buffer.getvalue(), "openfinance-dev", file_name)

    def income_to_excel(self, file_name: str):
        if self.income:
            # Create Excel buffer
            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer) as writer:
                payload_data = {"enquiry_cpf": self.enquiry_cpf,
                                "user_consent": self.user_consent,
                                "allow_autoupdate": self.allow_autoupdate,
                                "connection_key": self.connection_key,
                                "connection_id": self.connection_id,
                                "institution_id": self.institution_id,
                                "report_type": self.report_type,
                                "report_id": self.report_id,
                                "report_version": self.report_version}
                payload_df = pd.DataFrame([payload_data])
                payload_df.to_excel(writer, sheet_name="Payload", index=False)

                income_data = []
                for inc in self.income:
                    income_data.append(inc.bank.to_dict())
                    income_data[-1].update({"days_covered": inc.days_covered,
                                            "number_of_income_streams": inc.number_of_income_streams,
                                            "total_income_last_180_days": inc.total_income_last_180_days,
                                            "total_income_last_30_days": inc.total_income_last_30_days,
                                            "total_income_last_60_days": inc.total_income_last_60_days,
                                            "total_income_last_90_days": inc.total_income_last_90_days})

                income_df = pd.DataFrame(income_data)
                income_df.to_excel(writer, sheet_name="Income", index=False)

                income_stream_data = []
                for inc in self.income:
                    for stream in inc.income_stream:
                        stream_dict = {"income_stream_type": stream.income_stream_type}
                        if stream.income_day is not None:
                            stream_dict.update(stream.income_day)
                        for trans in stream.income_transactions:
                            trans_dict = {**stream_dict, **trans}
                            income_stream_data.append(trans_dict)

                if income_stream_data:
                    stream_trans_df = pd.DataFrame(income_stream_data)
                    stream_trans_df.to_excel(writer, sheet_name="IncomeStream_Transactions", index=False)

            # Upload to S3
            s3_helper = S3Helper()
            s3_helper.save_to_s3(excel_buffer.getvalue(), "openfinance-dev", file_name)
        else:
            print("No Income data to export.")
