import boto3

def create_table(table_name, partition_key):
    conn = boto3.resource("dynamodb", region_name="us-east-1")
    table_args = {
        "TableName": table_name,
        'KeySchema': [
            {'AttributeName': partition_key, 'KeyType': 'HASH'},
        ],
        'AttributeDefinitions': [
            {'AttributeName': partition_key, 'AttributeType': 'S'}
        ],
        'ProvisionedThroughput': {
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    }
    conn.create_table(**table_args)

def create_liabilities_tables(env="dev"):
    create_table("Klavi-LiabilityTransaction-{}".format(env), "category_id")
    create_table("Klavi-LiabilityStream-{}".format(env), "category_id")
    create_table("Klavi-Liabilities-{}".format(env), "report_id")

def create_financial_insight_tables(env="dev"):
    create_table("Klavi-FinancialInsight-{}".format(env), "report_id")
    create_table("Klavi-FinancialProfile-{}".format(env), "category_id")
    create_table("Klavi-CreditAnalysis-{}".format(env), "category_id")
    create_table("Klavi-CashflowAnalysis-{}".format(env), "category_id")
    create_table("Klavi-CreditcardSpending-{}".format(env), "category_id")

def create_category_checking_tables(env="dev"):
    create_table("Klavi-CategoryChecking-{}".format(env), "report_id")

def create_transaction_detail_table(env="dev"):
    create_table("Klavi-TransactionDetail-{}".format(env), "category_id")

def create_category_credit_card_tables(env="dev"):
    create_table("Klavi-CategoryCreditCard-{}".format(env), "report_id")
    create_table("Klavi-ClosedStatement-{}".format(env), "category_id")
    create_table("Klavi-OpenStatement-{}".format(env), "category_id")

def create_income_tables(env="dev"):
    create_table("Klavi-IncomeTransaction-{}".format(env), "category_id")
    create_table("Klavi-IncomeStream-{}".format(env), "category_id")
    create_table("Klavi-Income-{}".format(env), "report_id")

def create_score_k1_tables(env="dev"):
    create_table("Klavi-ScoreK1-{}".format(env), "report_id")

def create_balance_tables(env="dev"):
    create_table("Klavi-Balance-{}".format(env), "report_id")

def create_identity_tables(env="dev"):
    create_table("Klavi-Identity-{}".format(env), "report_id")

def create_risk_label_tables(env="dev"):
    create_table("Klavi-RiskLabel-{}".format(env), "report_id")
    create_table("Klavi-LabelDetail-{}".format(env), "category_id")

def create_all_klavi_tables(env="dev"):
    create_table("Klavi-KlaviReport-{}".format(env), "id")
    create_transaction_detail_table(env)
    create_category_checking_tables(env)
    create_liabilities_tables(env)
    create_financial_insight_tables(env)
    create_category_credit_card_tables(env)
    create_income_tables(env)
    create_score_k1_tables(env)
    create_balance_tables(env)
    create_identity_tables(env)
    create_risk_label_tables(env)


