from .base_dao import DynamoDbORM
#from . import transaction_detail_dao
import os
env = os.getenv("ENV")


class CategoryCheckingDAO(DynamoDbORM):
    def __init__(self):
        env = os.getenv("ENV")
        table_name = "Klavi-CategoryChecking-{env}".format(env=env)
        super().__init__(env, table_name)

    def save(self, category_checking: dict):
        print("To be Saved")
        print(category_checking.to_json())
        self.put(category_checking.to_json())
        transaction_detail_dao = DynamoDbORM(env, "Klavi-TransactionDetail-{env}".format(env=env))

        for transaction_detail in category_checking.transaction_details:
            response = transaction_detail_dao.put(transaction_detail.to_json())
