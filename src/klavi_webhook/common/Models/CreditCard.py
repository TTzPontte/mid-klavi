from dataclasses import dataclass
from typing import Optional

from Models.Bank import Bankaccount


@dataclass
class Creditcard:
    bank: Optional[Bankaccount]
    card_last4num: Optional[str] = None
    holder_name: Optional[str] = None
    card_type: Optional[str] = None
    credit_limit: Optional[float] = None
    available_limit: Optional[float] = None
    agency_number: Optional[str] = None
    bank_account: Optional[str] = None
    is_active: Optional[bool] = None
    is_vip: Optional[bool] = None
    open_statements: Optional[int] = None
    cpf_verified: Optional[str] = None
    closed_statements: Optional[int] = None

# class CreditcardSchema(Schema):
#     card_last4num = fields.Str()
#     holder_name = fields.Str()
#     card_type = fields.Str()
#     credit_limit = fields.Float()
#     available_limit = fields.Float()
#     agency_number = fields.Str()
#     bank_account = fields.Str()
#     is_active = fields.Bool()
#     is_vip = fields.Bool()
#     open_statements = fields.Int()
#     cpf_verified = fields.Str()
#     closed_statements = fields.Int()
#     bank = fields.Nested(BankAccountSchema, allow_none=True)
#
#     @post_load
#     def make_creditcard(self, data):
#         return Creditcard(**data)
