from dataclasses import dataclass, field
from typing import List, Optional, Dict

import pandas as pd

from src.open_finance_lambda.Models.BankAccount import BankAccount, Transaction
from src.open_finance_lambda.Models.IncomeStream import IncomeStream


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

    def to_excel(self, file_name: str):
        data = [
            {'Date': t.trans_date, 'Amount': t.trans_amount, 'Description': t.trans_description, 'Category': t.category,
             'Balance': t.balance} for t in self.transactions]
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)


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

    def to_excel(self, file_name: str):
        income_streams_data = []
        for stream in self.income_stream:
            for trans in stream.income_transactions:
                income_streams_data.append({"income_day": stream.income_day,
                                            "income_stream_type": stream.income_stream_type,
                                            **trans})
        df = pd.DataFrame(income_streams_data)
        df.to_excel(file_name, index=False)


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
    category_checking: List[CategoryChecking] = field(default_factory=list)
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
        self.income = [Income.from_dict(item) for item in data.get("Income", [])]

    def to_dict(self):
        return {"report_time": self.report_time,
                "data": {"enquiry_cpf": self.enquiry_cpf, "user_consent": self.user_consent,
                         "allow_autoupdate": self.allow_autoupdate, "connection_key": self.connection_key,
                         "connection_id": self.connection_id, "institution_id": self.institution_id,
                         "report_type": self.report_type, "report_id": self.report_id,
                         "report_version": self.report_version, }, "code": self.code, "msg": self.msg}

    def category_checking_to_excel(self, file_name: str):
        if not self.category_checking:
            print("No CategoryChecking data to export.")
            return

        with pd.ExcelWriter(file_name) as writer:
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
            account_data = []
            for cc in self.category_checking:
                account_data.append(cc.bank_account.to_dict())
                account_data[-1].update({"operation_code": cc.operation_code})

            account_df = pd.DataFrame(account_data)
            account_df.to_excel(writer, sheet_name="Accounts", index=False)

            # Write transaction data to "Transactions" sheet
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
            transaction_df.to_excel(writer, sheet_name="Transactions", index=False)

    def income_to_excel(self, file_name: str):
        if self.income:
            with pd.ExcelWriter(file_name) as writer:
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
                        stream_dict.update(stream.income_day)
                        for trans in stream.income_transactions:
                            trans_dict = {**stream_dict, **trans}
                            income_stream_data.append(trans_dict)

                if income_stream_data:
                    stream_trans_df = pd.DataFrame(income_stream_data)
                    stream_trans_df.to_excel(writer, sheet_name="IncomeStream_Transactions", index=False)
        else:
            print("No Income data to export.")


if __name__ == '__main__':
    checking_event = {"code": 200, "msg": "ok", "report_time": "2019-12-23 06:10:43",
                      "data": {"enquiry_cpf": "12345678901", "user_consent": "Yes", "allow_autoupdate": "Yes",
                               "connection_key": "gPuKXrCJU0kUDQO65J4k",
                               "connection_id": "f45c899f-11eb-231f-97c4-4b2c16484587", "institution_id": "033",
                               "report_type": "category_checking", "report_id": "4b2c1648-231f-11eb-97c4-f45c899f4587",
                               "report_version": "V1", "Category_checking": [
                              {"bank_name": "Santander", "bacen_name": "BANCO SANTANDER (BRASIL) S.A.",
                               "bacen_id": "033", "bank_branch": "1234", "account": "12.345678.9",
                               "operation_code": "001", "cpf_verified": "12345678901", "holder_name": "Usuaro anonimo",
                               "balance": 18.75, "TransactionDetail": [
                                  {"trans_date": "2019-12-23", "trans_amount": -150.05,
                                   "trans_description": "PREST EMPRESTIMOS/FINANCIAMENTOS AYMORE", "balance": 18.75,
                                   "category": "Empréstimo"}, {"trans_date": "2019-12-20", "trans_amount": 150,
                                                               "trans_description": "TED MESMA TITULARIDADE CIP 237-3750-0000001234567",
                                                               "balance": 168.8, "category": "Transferência"}]}]}}

    c = Parser(**checking_event)
    print(c.category_checking)
    print(c.to_dict())
    c.category_checking_to_excel('./category_checking.xlsx')

    income_event = {"code": 200, "msg": "ok", "report_time": "2022-03-03 10:18:41",
                    "data": {"enquiry_cpf": "01234567890", "user_consent": "Yes", "allow_autoupdate": "Yes",
                             "connection_key": "a37286b568e543caa4ab6ca8d7867cee",
                             "connection_id": "lrgekhgNXao8yPXgdjlMbrYgb9kxrKAo", "institution_id": "341",
                             "report_type": "income", "report_id": "71f2f906-9af4-11ec-be80-0aac1b96a2d0",
                             "report_version": "V1.1", "Income": [
                            {"account_holder": "JOHN DOE", "account_number": "12345-8", "agency_number": "8341",
                             "bacen_id": "341", "bacen_name": "ITAÚ UNIBANCO S.A.", "bank_name": "Itaú",
                             "cpf_verified": "01234567890", "days_covered": 180, "number_of_income_streams": 1,
                             "total_income_last_180_days": 30113, "total_income_last_30_days": 5115,
                             "total_income_last_60_days": 11609, "total_income_last_90_days": 13671, "incomeStream": [
                                {"incomeDay": {"1st_income_day": "3", "2nd_income_day": "20"}, "incomeTransactions": [
                                    {"trans_amount": 1016, "trans_date": "2022-02-18",
                                     "trans_description": "PAGTO SALARIO           "}],
                                 "income_stream_type": "Regular salary"}]},
                            {"account_holder": "JOHN DOE", "account_number": "23456-3", "agency_number": "8341",
                             "bacen_id": "341", "bacen_name": "ITAÚ UNIBANCO S.A.", "bank_name": "Itaú",
                             "cpf_verified": "01234567890", "days_covered": 180, "number_of_income_streams": 1,
                             "total_income_last_180_days": 30113, "total_income_last_30_days": 5115,
                             "total_income_last_60_days": 11609, "total_income_last_90_days": 13671, "incomeStream": [
                                {"incomeDay": {"1st_income_day": "10", "2nd_income_day": ""}, "incomeTransactions": [
                                    {"trans_amount": 1016, "trans_date": "2022-01-10",
                                     "trans_description": "PAGTO SALARIO           "}],
                                 "income_stream_type": "Regular salary"}]}]}}
    i = Parser(**income_event)
    print(i.income)
    print(i.to_dict())
    i.income_to_excel('./income.xlsx')

# todo
#  save json to s3
#  save excel to s3
#  :