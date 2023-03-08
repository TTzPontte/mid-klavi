from .base_dao import DynamoDbORM
#from .category_checking import CategoryCheckingDAO
import os
env = os.getenv("ENV")

#transaction_detail_dao = DynamoDbORM(env, "Klavi-TransactionDetail-{env}".format(env=env))
bank_account_dao = DynamoDbORM(env, "Klavi-BankAccount-{env}".format(env=env))
#category_checking_dao = CategoryCheckingDAO()
