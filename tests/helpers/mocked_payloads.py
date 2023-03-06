category_checking_payload = {
    "code":200,
    "msg":"ok",
    "action": "save",
    "report_time":"2019-12-23 06:10:43",
    "data":{
        "enquiry_cpf":"12345678901",
        "user_consent":"Yes",
        "allow_autoupdate":"Yes",
        "connection_key":"gPuKXrCJU0kUDQO65J4k",
        "connection_id":"f45c899f-11eb-231f-97c4-4b2c16484587",
        "institution_id":"033",
        "report_type":"category_checking",
        "report_id":"4b2c1648-231f-11eb-97c4-f45c899f4587",
        "report_version":"V1",
        "Category_checking":[
            {
                "bank_name":"Santander",
                "bacen_name":"BANCO SANTANDER (BRASIL) S.A.",
                "bacen_id":"033",
                "bank_branch":"1234",
                "account":"12.345678.9",
                "operation_code":"001",
                "cpf_verified":"12345678901",
                "holder_name":"Usuaro anonimo",
                "balance":18.75,
                "TransactionDetail":[
                    {
                        "trans_date":"2019-12-23",
                        "trans_amount":-150.05,
                        "trans_description":"PREST EMPRESTIMOS/FINANCIAMENTOS AYMORE",
                        "balance":18.75,
                        "category":"Empréstimo"
                    },
                    {
                        "trans_date":"2019-12-20",
                        "trans_amount":150,
                        "trans_description":"TED MESMA TITULARIDADE CIP 237-3750-0000001234567",
                        "balance":168.8,
                        "category":"Transferência"
                    }
                ]
            }
        ]
    }
}

credit_card_payload = {
    "code":200,
    "msg":"ok",
    "action": "save",
    "report_time":"2020-02-08 03:49:38",
    "data":{
        "enquiry_cpf":"12345678901",
        "user_consent":"Yes",
        "allow_autoupdate":"Yes",
        "connection_key":"gPuKXrCJU0kUDQO65J4k",
        "connection_id":"f45c899f-11eb-231f-97c4-4b2c16484587",
        "institution_id":"341",
        "report_type":"category_creditcard",
        "report_id":"4b2c1648-231f-11eb-97c4-f45c899f4590",
        "report_version":"V1",
        "Category_creditcard":[
            {
                "bank_name":"Itaú",
                "bacen_name":"ITAÚ UNIBANCO S.A.",
                "bacen_id":"341",
                "card_last4num":"1234",
                "cpf_verified":"12345678901",
                "holder_name":"Usuario anonimo",
                "card_type":"Itaucard Multiplo 2.0",
                "credit_limit":3300,
                "available_limit":3217.8,
                "agency_number":"1234",
                "bank_account":"12345-6",
                "is_active":1,
                "is_vip":0,
                "OpenStatement":{
                    "bill_amount":82.2,
                    "due_date":"2020-03-06",
                    "billing_date":"2020-02-24",
                    "bill_month":"mar/20",
                    "TransactionDetail":[
                        {
                            "trans_date":"2020-02-06",
                            "trans_amount":120.55,
                            "trans_currency":"BRL",
                            "trans_description":"PAGAMENTO EFETUADO",
                            "category":"Pagamento de cartão",
                            "payment_type":"A_VISTA",
                            "charge_identificator":"PARCELA_0",
                            "charge_number":0
                        },
                        {
                            "trans_date":"2020-02-02",
                            "trans_amount":-19.9,
                            "trans_currency":"BRL",
                            "trans_description":"Perfumaria Sunny",
                            "category":"Cuidados pessoais",
                            "payment_type":"A_VISTA",
                            "charge_identificator":"PARCELA_0",
                            "charge_number":0
                        },
                        {
                            "trans_date":"2020-01-25",
                            "trans_amount":-62.3,
                            "trans_currency":"BRL",
                            "trans_description":"Mc Donalds  Mac",
                            "category":"Bares / Restaurantes",
                            "payment_type":"A_VISTA",
                            "charge_identificator":"PARCELA_0",
                            "charge_number":0
                        }
                    ]
                },
                "ClosedStatement":[
                    {
                        "billing_date":"2020-01-27",
                        "bill_month":"fev/20",
                        "bill_amount":120.55,
                        "minimum_payment":12,
                        "payment_date":"2020-02-06",
                        "payment_amount":120.55,
                        "TransactionDetail":[
                            {
                                "trans_date":"2020-01-22",
                                "trans_amount":-34,
                                "trans_currency":"BRL",
                                "trans_description":"Comercial Pirituba",
                                "category":"Compras",
                                "payment_type":"A_VISTA",
                                "charge_identificator":"PARCELA_0",
                                "charge_number":0
                            },
                            {
                                "trans_date":"2020-01-22",
                                "trans_amount":-86.55,
                                "trans_currency":"BRL",
                                "trans_description":"OTICAS CAROL 01/10",
                                "category":"Compras",
                                "payment_type":"A_PRAZO",
                                "charge_identificator":"PARCELA_1",
                                "charge_number":10
                            }
                        ]
                    }
                ]
            },
            {
                "bank_name":"Itaú",
                "bacen_name":"ITAÚ UNIBANCO S.A.",
                "bacen_id":"341",
                "card_last_4_num":"5678",
                "cpf_verified":"12345678901",
                "holder_name":"Usuario anonimo",
                "card_type":"Itaucard Mastercard International",
                "credit_limit":2000,
                "available_limit":1886.55,
                "account":"12345-6",
                "is_active":1,
                "OpenStatement":{
                    "bill_amount":113.45,
                    "due_date":"2020-03-06",
                    "billing_date":"2020-02-27",
                    "bill_month":"mar/20",
                    "TransactionDetail":[
                        {
                            "trans_date":"2020-02-06",
                            "trans_amount":42.53,
                            "trans_currency":"BRL",
                            "trans_description":"PAGAMENTO EFETUADO",
                            "category":"Pagamento de cartão",
                            "payment_type":"A_VISTA",
                            "charge_identificator":"PARCELA_0",
                            "charge_number":0
                        },
                        {
                            "trans_date":"2020-02-04",
                            "trans_amount":-33.6,
                            "trans_currency":"BRL",
                            "trans_description":"Casa de paes",
                            "category":"Bares / Restaurantes",
                            "payment_type":"A_VISTA",
                            "charge_identificator":"PARCELA_0",
                            "charge_number":0
                        },
                        {
                            "trans_date":"2020-02-03",
                            "trans_amount":-72.9,
                            "trans_currency":"BRL",
                            "trans_description":"Mercadopago *natur",
                            "category":"Compras",
                            "payment_type":"A_VISTA",
                            "charge_identificator":"PARCELA_0",
                            "charge_number":0
                        },
                        {
                            "trans_date":"2020-01-30",
                            "trans_amount":-6.95,
                            "trans_currency":"BRL",
                            "trans_description":"Uberbr Uber Trip Help.",
                            "category":"Táxi / App",
                            "payment_type":"A_VISTA",
                            "charge_identificator":"PARCELA_0",
                            "charge_number":0
                        }
                    ]
                },
                "ClosedStatement":[
                    {
                        "billing_date":"2020-01-27",
                        "bill_month":"fev/20",
                        "bill_amount":42.53,
                        "minimum_payment":0,
                        "payment_date":"2020-02-06",
                        "payment_amount":42.53,
                        "TransactionDetail":[
                            {
                                "trans_date":"2020-01-27",
                                "trans_amount":-30.63,
                                "trans_currency":"BRL",
                                "trans_description":"Multa Por Atraso",
                                "category":"Outros serviços financeiros",
                                "payment_type":"A_VISTA",
                                "charge_identificator":"PARCELA_0",
                                "charge_number":0
                            },
                            {
                                "trans_date":"2019-12-28",
                                "trans_amount":-11.9,
                                "trans_currency":"BRL",
                                "trans_description":"Casa de paes",
                                "category":"Bares / Restaurantes",
                                "payment_type":"A_VISTA",
                                "charge_identificator":"PARCELA_0",
                                "charge_number":0
                            }
                        ]
                    }
                ]
            }
        ]
    }
}

event_payload = {
    "code":200,
    "msg":"ok",
    "action": "save",
    "report_time":"2019-12-23 06:10:43",
    "data":{
        "enquiry_cpf":"12345678901",
        "user_consent":"Yes",
        "allow_autoupdate":"Yes",
        "connection_key":"gPuKXrCJU0kUDQO65J4k",
        "connection_id":"f45c899f-11eb-231f-97c4-4b2c16484587",
        "institution_id":"033",
        "report_type":"category_checking",
        "report_id":"4b2c1648-231f-11eb-97c4-f45c899f4587",
        "report_version":"V1",
        "Category_checking":[
            {
                "bank_name":"Santander",
                "bacen_name":"BANCO SANTANDER (BRASIL) S.A.",
                "bacen_id":"033",
                "bank_branch":"1234",
                "account":"12.345678.9",
                "operation_code":"001",
                "cpf_verified":"12345678901",
                "holder_name":"Usuaro anonimo",
                "balance":18.75,
                "TransactionDetail":[
                    {
                        "trans_date":"2019-12-23",
                        "trans_amount":-150.05,
                        "trans_description":"PREST EMPRESTIMOS/FINANCIAMENTOS AYMORE",
                        "balance":18.75,
                        "category":"Empréstimo"
                    },
                    {
                        "trans_date":"2019-12-20",
                        "trans_amount":150,
                        "trans_description":"TED MESMA TITULARIDADE CIP 237-3750-0000001234567",
                        "balance":168.8,
                        "category":"Transferência"
                    }
                ]
            }
        ]
    }
}

financial_insight_payload = {
    "code": 200,
    "msg": "ok",
    "action": "save",
    "report_time": "2022-03-03 09:45:54",
    "data": {
        "enquiry_cpf":"12345678901",
        "user_consent":"Yes",
        "allow_autoupdate":"No",
        "connection_key":"gPuKXrCJU0kUDQO65J4k",
        "connection_id":"f45c899f-11eb-231f-97c4-4b2c16484587",
        "institution_id":"341",
        "report_type":"financial_insight",
        "report_id":"4b2c1648-231f-11eb-97c4-f45c899f4593",
        "report_version": "V1.1",
        "financial_insight": [
            {
                "bacen_id": "033",
                "bacen_name": "BANCO SANTANDER (BRASIL) S.A.",
                "bank_name": "Santander",
                "agency_number": "1076",
                "account_number": "01.01234.4",
                "cpf_verified": "01234567890",
                "account_holder": "JOHN DOE",
                "days_covered": 0,
                "cashflowAnalysis": [
                    {
                        "checking_account_balance": 0,
                        "avg_daily_balance_last_180_days": -1,
                        "avg_daily_balance_last_30_days": -1,
                        "avg_daily_balance_last_60_days": -1,
                        "avg_daily_balance_last_90_days": -1,
                        "inflow_last_180_days": -1,
                        "inflow_last_30_days": -1,
                        "inflow_last_60_days": -1,
                        "inflow_last_90_days": -1,
                        "outflow_last_180_days": -1,
                        "outflow_last_30_days": -1,
                        "outflow_last_60_days": -1,
                        "outflow_last_90_days": -1,
                        "saving_account_balance": -1
                    }
                ],
                "creditAnalysis": [
                    {
                        "overdraft_limit": 0,
                        "preapproved_loan": 0
                    }
                ],
                "creditcardSpending": [
                    {
                        "card_holder": "JOHN DOE",
                        "card_last_4_digit": "1096",
                        "card_type": "SANTANDER SX MASTER",
                        "credit_limit": 0.01,
                        "closed_bills_covered": 6,
                        "open_bill_balance": 0,
                        "last_closed_bill": -205.48,
                        "avg_last_3_closed_bills": -205.48,
                        "days_covered": 180,
                        "has_late_payment": "No",
                        "pay_bills_in_installment": "No"
                    }
                ],
                "financialProfile": [
                    {
                        "additional_overdraft_interest": 0,
                        "atm_withdrawal": 0,
                        "has_inss": "No",
                        "has_iptu_payment": "No",
                        "has_ipva_payment": "No",
                        "has_returned_cheque": "No",
                        "has_severance": "No",
                        "iof": 0,
                        "overdraft_interest": 0
                    }
                ]
            },
            {
                "bacen_id": "033",
                "bacen_name": "BANCO SANTANDER (BRASIL) S.A.",
                "bank_name": "Santander",
                "agency_number": "1076",
                "account_number": "01.12345.2",
                "cpf_verified": "01234567890",
                "account_holder": "JOHN DOE",
                "days_covered": 0,
                "cashflowAnalysis": [
                    {
                        "checking_account_balance": 0,
                        "avg_daily_balance_last_180_days": -1,
                        "avg_daily_balance_last_30_days": -1,
                        "avg_daily_balance_last_60_days": -1,
                        "avg_daily_balance_last_90_days": -1,
                        "inflow_last_180_days": -1,
                        "inflow_last_30_days": -1,
                        "inflow_last_60_days": -1,
                        "inflow_last_90_days": -1,
                        "outflow_last_180_days": -1,
                        "outflow_last_30_days": -1,
                        "outflow_last_60_days": -1,
                        "outflow_last_90_days": -1,
                        "saving_account_balance": -1
                    }
                ],
                "creditAnalysis": [
                    {
                        "overdraft_limit": 0,
                        "preapproved_loan": 0
                    }
                ],
                "creditcardSpending": None,
                "financialProfile": [
                    {
                        "additional_overdraft_interest": 0,
                        "atm_withdrawal": 0,
                        "has_inss": "No",
                        "has_iptu_payment": "No",
                        "has_ipva_payment": "No",
                        "has_returned_cheque": "No",
                        "has_severance": "No",
                        "iof": 0,
                        "overdraft_interest": 0
                    }
                ]
            }
        ]
    }
}

klavi_report_payload = {
    "code":200,
    "msg":"ok",
    "action": "save",
    "report_time":"2019-12-23 06:10:43",
    "data":{
        "enquiry_cpf":"12345678901",
        "user_consent":"Yes",
        "allow_autoupdate":"Yes",
        "connection_key":"gPuKXrCJU0kUDQO65J4k",
        "connection_id":"f45c899f-11eb-231f-97c4-4b2c16484587",
        "institution_id":"033",
        "report_type":"category_checking",
        "report_id":"4b2c1648-231f-11eb-97c4-f45c899f4587",
        "report_version":"V1",
        "Category_checking":[
            {
                "bank_name":"Santander",
                "bacen_name":"BANCO SANTANDER (BRASIL) S.A.",
                "bacen_id":"033",
                "bank_branch":"1234",
                "account":"12.345678.9",
                "operation_code":"001",
                "cpf_verified":"12345678901",
                "holder_name":"Usuaro anonimo",
                "balance":18.75,
                "TransactionDetail":[
                    {
                        "trans_date":"2019-12-23",
                        "trans_amount":-150.05,
                        "trans_description":"PREST EMPRESTIMOS/FINANCIAMENTOS AYMORE",
                        "balance":18.75,
                        "category":"Empréstimo"
                    },
                    {
                        "trans_date":"2019-12-20",
                        "trans_amount":150,
                        "trans_description":"TED MESMA TITULARIDADE CIP 237-3750-0000001234567",
                        "balance":168.8,
                        "category":"Transferência"
                    }
                ]
            }
        ]
    }
}

liabilities_payload = {
    "code": 200,
    "msg": "ok",
    "action": "save",
    "report_time": "2022-03-03 12:52:13",
    "data": {
        "enquiry_cpf":"12345678901",
        "user_consent":"Yes",
        "allow_autoupdate":"Yes",
        "connection_key":"gPuKXrCJU0kUDQO65J4k",
        "connection_id":"f45c899f-11eb-231f-97c4-4b2c16484587",
        "institution_id":"033",
        "report_type":"liabilities",
        "report_id":"4b2c1648-231f-11eb-97c4-f45c899f4592",
        "report_version":"V1.1",
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

income_payload = {
    "code": 200,
    "msg": "ok",
    "report_time": "2022-03-03 10:18:41",
    "data": {
        "enquiry_cpf": "01234567890",
        "user_consent": "Yes",
        "allow_autoupdate": "Yes",
        "connection_key": "a37286b568e543caa4ab6ca8d7867cee",
        "connection_id": "lrgekhgNXao8yPXgdjlMbrYgb9kxrKAo",
        "institution_id": "341",
        "report_type": "income",
        "report_id": "71f2f906-9af4-11ec-be80-0aac1b96a2d0",
        "report_version": "V1.1",
        "Income": [
            {
                "account_holder": "JOHN DOE",
                "account_number": "12345-8",
                "agency_number": "8341",
                "bacen_id": "341",
                "bacen_name": "ITAÚ UNIBANCO S.A.",
                "bank_name": "Itaú",
                "cpf_verified": "01234567890",
                "days_covered": 180,
                "number_of_income_streams": 1,
                "total_income_last_180_days": 30113,
                "total_income_last_30_days": 5115,
                "total_income_last_60_days": 11609,
                "total_income_last_90_days": 13671,
                "incomeStream": [
                    {
                        "incomeDay": {
                            "1st_income_day": "3",
                            "2nd_income_day": "20"
                        },
                        "incomeTransactions": [
                            {
                                "trans_amount": 1016,
                                "trans_date": "2022-02-18",
                                "trans_description": "PAGTO SALARIO           "
                            }
                        ],
                        "income_stream_type": "Regular salary"
                    }
                ]
            },
            {
                "account_holder": "JOHN DOE",
                "account_number": "23456-3",
                "agency_number": "8341",
                "bacen_id": "341",
                "bacen_name": "ITAÚ UNIBANCO S.A.",
                "bank_name": "Itaú",
                "cpf_verified": "01234567890",
                "days_covered": 180,
                "number_of_income_streams": 1,
                "total_income_last_180_days": 30113,
                "total_income_last_30_days": 5115,
                "total_income_last_60_days": 11609,
                "total_income_last_90_days": 13671,
                "incomeStream": [
                    {
                        "incomeDay": {
                            "1st_income_day": "10",
                            "2nd_income_day": ""
                        },
                        "incomeTransactions": [
                            {
                                "trans_amount": 1016,
                                "trans_date": "2022-01-10",
                                "trans_description": "PAGTO SALARIO           "
                            }
                        ],
                        "income_stream_type": "Regular salary"
                    }
                ]
            }
        ]
    }
}

score_k1_payload = {
    "code":200,
    "msg":"ok",
    "report_time":"2020-07-03 22:21:51",
    "report_id":"4b2c1648-231f-11eb-97c4-f45c899f4596",
    "data":{
        "enquiry_cpf":"12345678901",
        "user_consent":"Yes",
        "allow_autoupdate":"No",
        "connection_key":"gPuKXrCJU0kUDQO65J4k",
        "connection_id":"f45c899f-11eb-231f-97c4-4b2c16484587",
        "institution_id":"341",
        "report_type":"score_k1",
        "report_id":"4b2c1648-231f-11eb-97c4-f45c899f4593",
        "report_version": "V1",
        "score_info": {
            "account_info": {
                "bank_name": "Itaú",
                "bacen_name":"ITAÚ UNIBANCO S.A.",
                "bacen_id":"341",
                "agency_number": "1234",
                "holder_name": "Usuario anonimo",
                "cpf_verified": "12345678901",
                "account_number": "1234-5"
            },
            "score_detail": {
                "score_k1": 615,
                "version": "v1.0"
            }
        }
    }
}

balance_payload = {
    "code":200,
    "msg":"ok",
    "report_time":"2020-07-03 22:21:51",
    "data":{
        "enquiry_cpf":"12345678901",
        "user_consent":"Yes",
        "allow_autoupdate":"No",
        "connection_key":"gPuKXrCJU0kUDQO65J4k",
        "connection_id":"f45c899f-11eb-231f-97c4-4b2c16484587",
        "institution_id":"237",
        "report_type":"balance",
        "report_id":"4b2c1648-231f-11eb-97c4-f45c899f4597",
        "report_version":"V1",
        "accountBalance":[
            {
                "bank_name":"Bradesco",
                "bacen_name":"Banco Bradesco S.A.",
                "bacen_id":"237",
                "agency_number":"1234",
                "account_type":"checking",
                "account_number":"1234-5",
                "cpf_verified":"12345678901",
                "account_holder":"Usuario anonimo",
                "current_balance":100,
                "available_limit":-1,
                "total_limit":-1
            },
            {
                "bank_name":"Bradesco",
                "bacen_name":"Banco Bradesco S.A.",
                "bacen_id":"237",
                "agency_number":"1234",
                "account_type":"creditcard",
                "account_number":"1234",
                "cpf_verified":"12345678901",
                "account_holder":"Usuario anonimo",
                "current_balance":3512.46,
                "available_limit":2987.55,
                "total_limit":6500
            },
            {
                "bank_name":"Bradesco",
                "bacen_name":"Banco Bradesco S.A.",
                "bacen_id":"237",
                "agency_number":"1234",
                "account_type":"savings",
                "account_number":"5432-1",
                "cpf_verified":"12345678901",
                "account_holder":"Usuario anonimo",
                "current_balance":7659.47,
                "available_limit":-1,
                "total_limit":-1
            }
        ]
    }
}

identity_payload = {
    "code":200,
    "msg":"ok",
    "report_time":"2020-07-03 22:21:51",
    "data":{
        "enquiry_cpf":"12345678901",
        "user_consent":"Yes",
        "allow_autoupdate":"No",
        "connection_key":"gPuKXrCJU0kUDQO65J4k",
        "connection_id":"f45c899f-11eb-231f-97c4-4b2c16484587",
        "institution_id":"237",
        "report_type":"identity",
        "report_id":"4b2c1648-231f-11eb-97c4-f45c899f4596",
        "report_version":"V1",
        "identity":{
            "bank_name":"Bradesco",
            "bacen_name":"Banco Bradesco S.A.",
            "bacen_id":"237",
            "agency_number":"1234",
            "account_number":"1234-5",
            "cpf_verified":"12345678901",
            "name":"Usuario anonimo",
            "cellphone":"11987654321",
            "email":"tester@test.com",
            "correspondenceAddress":{
                "postcode":"00000000",
                "address":"Rua Brasil",
                "address_number":"66",
                "neighborhood":"Neighborhood",
                "complement":"n/a",
                "city":"SAO PAULO",
                "state":"SAO PAULO",
                "country":"BRASIL"
            }
        }
    }
}

risk_label_payload = {
    "code":200,
    "msg":"ok",
    "query_param":{},
    "report_time":"2022-06-08 17:04:13",
    "data":{
        "allow_autoupdate":"Yes",
        "connection_id":"dxnFOVjiN1KBbnGPgrjHu0zSUPNht",
        "connection_key":"4e722aab49544419840995316f80f",
        "enquiry_cpf":"12345678901",
        "institution_id":"001",
        "report_id":"f7757d5a-e709-11ec-97fc-064bb0845",
        "report_type":"k_label",
        "report_version":"V1",
        "user_consent":"Yes",
        "Risk_label":{
            "accountInfo":{
                "account_number":"1234-0",
                "agency_number":"2345-2",
                "bacen_id":"001",
                "bacen_name":"Banco do Brasil S.A.",
                "bank_name":"Banco do Brasil",
                "cpf_verified":"12345678901",
                "holder_name":"Usuario anonimo"
            },
            "labelDetail":[
                {
                    "label_code": "K00001",
                    "label_name": "klavi.transactions.transaction_age_of_checking_account.max.full_record_period",
                    "label_value": 2
                },
                {
                    "label_code": "K00002",
                    "label_name": "klavi.transactions.transaction_age_of_checking_account.min.full_record_period",
                    "label_value": 2
                },
                {
                    "label_code": "K00003",
                    "label_name": "klavi.transactions.transaction_age_of_checking_account.avg.full_record_period",
                    "label_value": 2
                },
                {
                    "label_code": "K00004",
                    "label_name": "klavi.transactions.transaction_age_of_checking_account.med.full_record_period",
                    "label_value": 2
                },
                {
                    "label_code": "K00005",
                    "label_name": "klavi.transactions.transaction_age_of_checking_account.std.full_record_period",
                    "label_value": 0
                },
                {
                    "label_code": "K00006",
                    "label_name": "klavi.transactions.transaction_age_of_checking_account.cv.full_record_period",
                    "label_value": 0
                },
                {
                    "label_code": "K00007",
                    "label_name": "klavi.transactions.account_age_of_checking_account.max.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00008",
                    "label_name": "klavi.transactions.account_age_of_checking_account.min.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00009",
                    "label_name": "klavi.transactions.account_age_of_checking_account.avg.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00010",
                    "label_name": "klavi.transactions.account_age_of_checking_account.med.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00011",
                    "label_name": "klavi.transactions.account_age_of_checking_account.std.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00012",
                    "label_name": "klavi.transactions.account_age_of_checking_account.cv.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00013",
                    "label_name": "klavi.transactions.transaction_age_of_creditcard.max.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00014",
                    "label_name": "klavi.transactions.transaction_age_of_creditcard.min.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00015",
                    "label_name": "klavi.transactions.transaction_age_of_creditcard.avg.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00016",
                    "label_name": "klavi.transactions.transaction_age_of_creditcard.med.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00017",
                    "label_name": "klavi.transactions.transaction_age_of_creditcard.std.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00018",
                    "label_name": "klavi.transactions.transaction_age_of_creditcard.cv.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00019",
                    "label_name": "klavi.transactions.account_age_of_creditcard.max.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00020",
                    "label_name": "klavi.transactions.account_age_of_creditcard.min.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00021",
                    "label_name": "klavi.transactions.account_age_of_creditcard.avg.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00022",
                    "label_name": "klavi.transactions.account_age_of_creditcard.med.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00023",
                    "label_name": "klavi.transactions.account_age_of_creditcard.std.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00024",
                    "label_name": "klavi.transactions.account_age_of_creditcard.cv.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00025",
                    "label_name": "klavi.transactions.is_premium_bank.pct.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00026",
                    "label_name": "klavi.transactions.count_of_checking_account.tot.full_record_period",
                    "label_value": 1
                },
                {
                    "label_code": "K00027",
                    "label_name": "klavi.transactions.count_of_creditcard.tot.full_record_period",
                    "label_value": 0
                },
                {
                    "label_code": "K00028",
                    "label_name": "klavi.transactions.creditcard_ranking.max.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00029",
                    "label_name": "klavi.transactions.creditcard_limit.max.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00030",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.max.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00031",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.min.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00032",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.avg.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00033",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.med.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00034",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.std.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00035",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.cv.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00036",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.max.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00037",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.min.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00038",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.avg.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00039",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.med.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00040",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.std.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00041",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.cv.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00042",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.max.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00043",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.min.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00044",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.avg.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00045",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.med.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00046",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.std.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00047",
                    "label_name": "klavi.transactions.bill_amount_of_creditcard.cv.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00048",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.max.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00049",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.min.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00050",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.avg.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00051",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.med.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00052",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.std.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00053",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.cv.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00054",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.max.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00055",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.min.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00056",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.avg.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00057",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.med.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00058",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.std.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00059",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.cv.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00060",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.max.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00061",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.min.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00062",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.avg.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00063",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.med.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00064",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.std.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00065",
                    "label_name": "klavi.transactions.transaction_count_of_creditcard.cv.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00066",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.max.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00067",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.min.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00068",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.avg.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00069",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.med.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00070",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.std.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00071",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.cv.last_1_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00072",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.max.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00073",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.min.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00074",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.avg.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00075",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.med.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00076",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.std.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00077",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.cv.last_2_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00078",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.max.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00079",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.min.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00080",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.avg.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00081",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.med.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00082",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.std.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00083",
                    "label_name": "klavi.transactions.highest_amount_transaction_of_creditcard.cv.last_3_bill_month",
                    "label_value": -999999
                },
                {
                    "label_code": "K00084",
                    "label_name": "klavi.transactions.checking_account_balance.full_record_period",
                    "label_value": 0
                },
                {
                    "label_code": "K00085",
                    "label_name": "klavi.transactions.daily_balance_of_checking_account.avg.last_30_days",
                    "label_value": 23.22
                },
                {
                    "label_code": "K00086",
                    "label_name": "klavi.transactions.daily_balance_of_checking_account.avg.last_60_days",
                    "label_value": 101.71
                },
                {
                    "label_code": "K00087",
                    "label_name": "klavi.transactions.daily_balance_of_checking_account.avg.last_90_days",
                    "label_value": 101.71
                },
                {
                    "label_code": "K00088",
                    "label_name": "klavi.transactions.salary_payday_1.last_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00089",
                    "label_name": "klavi.transactions.salary_payday_2.last_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00090",
                    "label_name": "klavi.transactions.salary_payday_3.last_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00091",
                    "label_name": "klavi.transactions.salary_payday_4.last_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00092",
                    "label_name": "klavi.transactions.cash_inflow_of_checking_account.tot.last_30_days",
                    "label_value": 2.85
                },
                {
                    "label_code": "K00093",
                    "label_name": "klavi.transactions.cash_inflow_of_checking_account.tot.last_60_days",
                    "label_value": 512.85
                },
                {
                    "label_code": "K00094",
                    "label_name": "klavi.transactions.cash_inflow_of_checking_account.tot.last_90_days",
                    "label_value": 512.85
                },
                {
                    "label_code": "K00095",
                    "label_name": "klavi.transactions.inflow_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00096",
                    "label_name": "klavi.transactions.inflow_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 3
                },
                {
                    "label_code": "K00097",
                    "label_name": "klavi.transactions.inflow_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 3
                },
                {
                    "label_code": "K00098",
                    "label_name": "klavi.transactions.cash_outflow_of_checking_account.tot.last_30_days",
                    "label_value": 131.33
                },
                {
                    "label_code": "K00099",
                    "label_name": "klavi.transactions.cash_outflow_of_checking_account.tot.last_60_days",
                    "label_value": 512.85
                },
                {
                    "label_code": "K00100",
                    "label_name": "klavi.transactions.cash_outflow_of_checking_account.tot.last_90_days",
                    "label_value": 512.85
                },
                {
                    "label_code": "K00101",
                    "label_name": "klavi.transactions.outflow_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 5
                },
                {
                    "label_code": "K00102",
                    "label_name": "klavi.transactions.outflow_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 12
                },
                {
                    "label_code": "K00103",
                    "label_name": "klavi.transactions.outflow_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 12
                },
                {
                    "label_code": "K00104",
                    "label_name": "klavi.transactions.gross_inflow_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00105",
                    "label_name": "klavi.transactions.gross_inflow_of_checking_account.tot.last_60_days",
                    "label_value": 510
                },
                {
                    "label_code": "K00106",
                    "label_name": "klavi.transactions.gross_inflow_of_checking_account.tot.last_90_days",
                    "label_value": 510
                },
                {
                    "label_code": "K00107",
                    "label_name": "klavi.transactions.gross_inflow_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00108",
                    "label_name": "klavi.transactions.gross_inflow_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00109",
                    "label_name": "klavi.transactions.gross_inflow_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00110",
                    "label_name": "klavi.transactions.gross_outflow_of_checking_account.tot.last_30_days",
                    "label_value": 131.33
                },
                {
                    "label_code": "K00111",
                    "label_name": "klavi.transactions.gross_outflow_of_checking_account.tot.last_60_days",
                    "label_value": 509.85
                },
                {
                    "label_code": "K00112",
                    "label_name": "klavi.transactions.gross_outflow_of_checking_account.tot.last_90_days",
                    "label_value": 509.85
                },
                {
                    "label_code": "K00113",
                    "label_name": "klavi.transactions.gross_outflow_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 5
                },
                {
                    "label_code": "K00114",
                    "label_name": "klavi.transactions.gross_outflow_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 10
                },
                {
                    "label_code": "K00115",
                    "label_name": "klavi.transactions.gross_outflow_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 10
                },
                {
                    "label_code": "K00116",
                    "label_name": "klavi.transactions.real_inflow_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00117",
                    "label_name": "klavi.transactions.real_inflow_of_checking_account.tot.last_60_days",
                    "label_value": 510
                },
                {
                    "label_code": "K00118",
                    "label_name": "klavi.transactions.real_inflow_of_checking_account.tot.last_90_days",
                    "label_value": 510
                },
                {
                    "label_code": "K00119",
                    "label_name": "klavi.transactions.real_inflow_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00120",
                    "label_name": "klavi.transactions.real_inflow_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00121",
                    "label_name": "klavi.transactions.real_inflow_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00122",
                    "label_name": "klavi.transactions.real_outflow_of_checking_account.tot.last_30_days",
                    "label_value": 131.33
                },
                {
                    "label_code": "K00123",
                    "label_name": "klavi.transactions.real_outflow_of_checking_account.tot.last_60_days",
                    "label_value": 509.85
                },
                {
                    "label_code": "K00124",
                    "label_name": "klavi.transactions.real_outflow_of_checking_account.tot.last_90_days",
                    "label_value": 509.85
                },
                {
                    "label_code": "K00125",
                    "label_name": "klavi.transactions.real_outflow_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 5
                },
                {
                    "label_code": "K00126",
                    "label_name": "klavi.transactions.real_outflow_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 10
                },
                {
                    "label_code": "K00127",
                    "label_name": "klavi.transactions.real_outflow_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 10
                },
                {
                    "label_code": "K00128",
                    "label_name": "klavi.transactions.loan_inflow_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00129",
                    "label_name": "klavi.transactions.loan_inflow_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00130",
                    "label_name": "klavi.transactions.loan_inflow_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00131",
                    "label_name": "klavi.transactions.loan_inflow_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00132",
                    "label_name": "klavi.transactions.loan_inflow_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00133",
                    "label_name": "klavi.transactions.loan_inflow_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00134",
                    "label_name": "klavi.transactions.loan_outflow_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00135",
                    "label_name": "klavi.transactions.loan_outflow_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00136",
                    "label_name": "klavi.transactions.loan_outflow_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00137",
                    "label_name": "klavi.transactions.loan_outflow_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00138",
                    "label_name": "klavi.transactions.loan_outflow_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00139",
                    "label_name": "klavi.transactions.loan_outflow_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00140",
                    "label_name": "klavi.transactions.net_cash_flow_of_checking_account.tot.last_30_days",
                    "label_value": -128.48
                },
                {
                    "label_code": "K00141",
                    "label_name": "klavi.transactions.net_cash_flow_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00142",
                    "label_name": "klavi.transactions.net_cash_flow_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00143",
                    "label_name": "klavi.transactions.investment_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00144",
                    "label_name": "klavi.transactions.investment_of_checking_account.tot.last_60_days",
                    "label_value": 3
                },
                {
                    "label_code": "K00145",
                    "label_name": "klavi.transactions.investment_of_checking_account.tot.last_90_days",
                    "label_value": 3
                },
                {
                    "label_code": "K00146",
                    "label_name": "klavi.transactions.investment_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00147",
                    "label_name": "klavi.transactions.investment_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00148",
                    "label_name": "klavi.transactions.investment_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00149",
                    "label_name": "klavi.transactions.atm_withdrawal_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00150",
                    "label_name": "klavi.transactions.atm_withdrawal_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00151",
                    "label_name": "klavi.transactions.atm_withdrawal_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00152",
                    "label_name": "klavi.transactions.atm_withdrawal_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00153",
                    "label_name": "klavi.transactions.atm_withdrawal_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00154",
                    "label_name": "klavi.transactions.atm_withdrawal_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00155",
                    "label_name": "klavi.transactions.real_transfer_in_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00156",
                    "label_name": "klavi.transactions.real_transfer_in_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00157",
                    "label_name": "klavi.transactions.real_transfer_in_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00158",
                    "label_name": "klavi.transactions.real_transfer_in_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00159",
                    "label_name": "klavi.transactions.real_transfer_in_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00160",
                    "label_name": "klavi.transactions.real_transfer_in_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00161",
                    "label_name": "klavi.transactions.real_transfer_out_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00162",
                    "label_name": "klavi.transactions.real_transfer_out_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00163",
                    "label_name": "klavi.transactions.real_transfer_out_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00164",
                    "label_name": "klavi.transactions.real_transfer_out_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00165",
                    "label_name": "klavi.transactions.real_transfer_out_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00166",
                    "label_name": "klavi.transactions.real_transfer_out_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00167",
                    "label_name": "klavi.transactions.creditcard_repayment_of_checking_account.tot.last_30_days",
                    "label_value": 18.65
                },
                {
                    "label_code": "K00168",
                    "label_name": "klavi.transactions.creditcard_repayment_of_checking_account.tot.last_60_days",
                    "label_value": 23.65
                },
                {
                    "label_code": "K00169",
                    "label_name": "klavi.transactions.creditcard_repayment_of_checking_account.tot.last_90_days",
                    "label_value": 23.65
                },
                {
                    "label_code": "K00170",
                    "label_name": "klavi.transactions.creditcard_repayment_transaction_of_checking_account.tot.last_30_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00171",
                    "label_name": "klavi.transactions.creditcard_repayment_transaction_of_checking_account.tot.last_60_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00172",
                    "label_name": "klavi.transactions.creditcard_repayment_transaction_of_checking_account.tot.last_90_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00173",
                    "label_name": "klavi.transactions.financial_expenses_of_checking_account.tot.last_30_days",
                    "label_value": 17.79
                },
                {
                    "label_code": "K00174",
                    "label_name": "klavi.transactions.financial_expenses_of_checking_account.tot.last_60_days",
                    "label_value": 17.79
                },
                {
                    "label_code": "K00175",
                    "label_name": "klavi.transactions.financial_expenses_of_checking_account.tot.last_90_days",
                    "label_value": 17.79
                },
                {
                    "label_code": "K00176",
                    "label_name": "klavi.transactions.financial_expenses_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00177",
                    "label_name": "klavi.transactions.financial_expenses_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00178",
                    "label_name": "klavi.transactions.financial_expenses_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00179",
                    "label_name": "klavi.transactions.non_financial_expenses_of_checking_account.tot.last_30_days",
                    "label_value": 112.68
                },
                {
                    "label_code": "K00180",
                    "label_name": "klavi.transactions.non_financial_expenses_of_checking_account.tot.last_60_days",
                    "label_value": 486.2
                },
                {
                    "label_code": "K00181",
                    "label_name": "klavi.transactions.non_financial_expenses_of_checking_account.tot.last_90_days",
                    "label_value": 486.2
                },
                {
                    "label_code": "K00182",
                    "label_name": "klavi.transactions.non_financial_expenses_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 4
                },
                {
                    "label_code": "K00183",
                    "label_name": "klavi.transactions.non_financial_expenses_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 8
                },
                {
                    "label_code": "K00184",
                    "label_name": "klavi.transactions.non_financial_expenses_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 8
                },
                {
                    "label_code": "K00185",
                    "label_name": "klavi.transactions.insurance_inflow_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00186",
                    "label_name": "klavi.transactions.insurance_inflow_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00187",
                    "label_name": "klavi.transactions.insurance_inflow_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00188",
                    "label_name": "klavi.transactions.insurance_inflow_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00189",
                    "label_name": "klavi.transactions.insurance_inflow_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00190",
                    "label_name": "klavi.transactions.insurance_inflow_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00191",
                    "label_name": "klavi.transactions.insurance_outflow_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00192",
                    "label_name": "klavi.transactions.insurance_outflow_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00193",
                    "label_name": "klavi.transactions.insurance_outflow_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00194",
                    "label_name": "klavi.transactions.insurance_outflow_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00195",
                    "label_name": "klavi.transactions.insurance_outflow_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00196",
                    "label_name": "klavi.transactions.insurance_outflow_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00197",
                    "label_name": "klavi.transactions.independent_brokers_investment_application_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00198",
                    "label_name": "klavi.transactions.independent_brokers_investment_application_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00199",
                    "label_name": "klavi.transactions.independent_brokers_investment_application_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00200",
                    "label_name": "klavi.transactions.independent_brokers_investment_application_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00201",
                    "label_name": "klavi.transactions.independent_brokers_investment_application_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00202",
                    "label_name": "klavi.transactions.independent_brokers_investment_application_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00203",
                    "label_name": "klavi.transactions.independent_brokers_investment_redemption_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00204",
                    "label_name": "klavi.transactions.independent_brokers_investment_redemption_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00205",
                    "label_name": "klavi.transactions.independent_brokers_investment_redemption_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00206",
                    "label_name": "klavi.transactions.independent_brokers_investment_redemption_transaction_count_of_checking_account.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00207",
                    "label_name": "klavi.transactions.independent_brokers_investment_redemption_transaction_count_of_checking_account.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00208",
                    "label_name": "klavi.transactions.independent_brokers_investment_redemption_transaction_count_of_checking_account.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00209",
                    "label_name": "klavi.transactions.savings_account_balance.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00210",
                    "label_name": "klavi.transactions.overdraft_limit.max.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00211",
                    "label_name": "klavi.transactions.preapproved_loan.max.full_record_period",
                    "label_value": -999999
                },
                {
                    "label_code": "K00212",
                    "label_name": "klavi.transactions.creditcard_late_payment_fines.tot.last_30_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00213",
                    "label_name": "klavi.transactions.creditcard_late_payment_fines.tot.last_60_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00214",
                    "label_name": "klavi.transactions.creditcard_late_payment_fines.tot.last_90_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00215",
                    "label_name": "klavi.transactions.creditcard_late_payment_fines_transaction_count.tot.last_30_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00216",
                    "label_name": "klavi.transactions.creditcard_late_payment_fines_transaction_count.tot.last_60_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00217",
                    "label_name": "klavi.transactions.creditcard_late_payment_fines_transaction_count.tot.last_90_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00218",
                    "label_name": "klavi.transactions.longest_periods_of_creditcard_installment_payment.max.last_30_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00219",
                    "label_name": "klavi.transactions.longest_periods_of_creditcard_installment_payment.max.last_60_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00220",
                    "label_name": "klavi.transactions.longest_periods_of_creditcard_installment_payment.max.last_90_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00221",
                    "label_name": "klavi.transactions.serverance_transaction.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00222",
                    "label_name": "klavi.transactions.serverance_transaction.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00223",
                    "label_name": "klavi.transactions.serverance_transaction.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00224",
                    "label_name": "klavi.transactions.serverance_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00225",
                    "label_name": "klavi.transactions.serverance_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00226",
                    "label_name": "klavi.transactions.serverance_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00227",
                    "label_name": "klavi.transactions.inss_transaction.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00228",
                    "label_name": "klavi.transactions.inss_transaction.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00229",
                    "label_name": "klavi.transactions.inss_transaction.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00230",
                    "label_name": "klavi.transactions.inss_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00231",
                    "label_name": "klavi.transactions.inss_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00232",
                    "label_name": "klavi.transactions.inss_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00233",
                    "label_name": "klavi.transactions.returned_cheque_transaction.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00234",
                    "label_name": "klavi.transactions.returned_cheque_transaction.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00235",
                    "label_name": "klavi.transactions.returned_cheque_transaction.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00236",
                    "label_name": "klavi.transactions.returned_cheque_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00237",
                    "label_name": "klavi.transactions.returned_cheque_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00238",
                    "label_name": "klavi.transactions.returned_cheque_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00239",
                    "label_name": "klavi.transactions.overdraft_interest_transaction.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00240",
                    "label_name": "klavi.transactions.overdraft_interest_transaction.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00241",
                    "label_name": "klavi.transactions.overdraft_interest_transaction.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00242",
                    "label_name": "klavi.transactions.overdraft_interest_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00243",
                    "label_name": "klavi.transactions.overdraft_interest_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00244",
                    "label_name": "klavi.transactions.overdraft_interest_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00245",
                    "label_name": "klavi.transactions.additional_overdraft_interest_transaction.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00246",
                    "label_name": "klavi.transactions.additional_overdraft_interest_transaction.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00247",
                    "label_name": "klavi.transactions.additional_overdraft_interest_transaction.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00248",
                    "label_name": "klavi.transactions.additional_overdraft_interest_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00249",
                    "label_name": "klavi.transactions.additional_overdraft_interest_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00250",
                    "label_name": "klavi.transactions.additional_overdraft_interest_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00251",
                    "label_name": "klavi.transactions.debt_renegotiation_transaction.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00252",
                    "label_name": "klavi.transactions.debt_renegotiation_transaction.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00253",
                    "label_name": "klavi.transactions.debt_renegotiation_transaction.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00254",
                    "label_name": "klavi.transactions.debt_renegotiation_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00255",
                    "label_name": "klavi.transactions.debt_renegotiation_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00256",
                    "label_name": "klavi.transactions.debt_renegotiation_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00257",
                    "label_name": "klavi.transactions.medical_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00258",
                    "label_name": "klavi.transactions.medical_expenses.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00259",
                    "label_name": "klavi.transactions.medical_expenses.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00260",
                    "label_name": "klavi.transactions.medical_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00261",
                    "label_name": "klavi.transactions.medical_expenses_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00262",
                    "label_name": "klavi.transactions.medical_expenses_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00263",
                    "label_name": "klavi.transactions.iof_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00264",
                    "label_name": "klavi.transactions.iof_expenses.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00265",
                    "label_name": "klavi.transactions.iof_expenses.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00266",
                    "label_name": "klavi.transactions.iof_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00267",
                    "label_name": "klavi.transactions.iof_expenses_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00268",
                    "label_name": "klavi.transactions.iof_expenses_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00269",
                    "label_name": "klavi.transactions.ipva_payment.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00270",
                    "label_name": "klavi.transactions.ipva_payment.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00271",
                    "label_name": "klavi.transactions.ipva_payment.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00272",
                    "label_name": "klavi.transactions.ipva_payment_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00273",
                    "label_name": "klavi.transactions.ipva_payment_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00274",
                    "label_name": "klavi.transactions.ipva_payment_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00275",
                    "label_name": "klavi.transactions.iptu_payment.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00276",
                    "label_name": "klavi.transactions.iptu_payment.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00277",
                    "label_name": "klavi.transactions.iptu_payment.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00278",
                    "label_name": "klavi.transactions.iptu_payment_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00279",
                    "label_name": "klavi.transactions.iptu_payment_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00280",
                    "label_name": "klavi.transactions.iptu_payment_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00281",
                    "label_name": "klavi.transactions.total_income.tot.last_30_days",
                    "label_value": 2.85
                },
                {
                    "label_code": "K00282",
                    "label_name": "klavi.transactions.total_income.tot.last_60_days",
                    "label_value": 512.85
                },
                {
                    "label_code": "K00283",
                    "label_name": "klavi.transactions.total_income.tot.last_90_days",
                    "label_value": 512.85
                },
                {
                    "label_code": "K00284",
                    "label_name": "klavi.transactions.total_income_transaction_count.tot.last_30_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00285",
                    "label_name": "klavi.transactions.total_income_transaction_count.tot.last_60_days",
                    "label_value": 3
                },
                {
                    "label_code": "K00286",
                    "label_name": "klavi.transactions.total_income_transaction_count.tot.last_90_days",
                    "label_value": 3
                },
                {
                    "label_code": "K00287",
                    "label_name": "klavi.transactions.number_of_income_streams.tot.last_30_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00288",
                    "label_name": "klavi.transactions.number_of_income_streams.tot.last_60_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00289",
                    "label_name": "klavi.transactions.number_of_income_streams.tot.last_90_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00290",
                    "label_name": "klavi.transactions.regular_salary.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00291",
                    "label_name": "klavi.transactions.regular_salary.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00292",
                    "label_name": "klavi.transactions.regular_salary.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00293",
                    "label_name": "klavi.transactions.regular_salary_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00294",
                    "label_name": "klavi.transactions.regular_salary_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00295",
                    "label_name": "klavi.transactions.regular_salary_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00296",
                    "label_name": "klavi.transactions.period_with_regular_salary.tot.last_90_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00297",
                    "label_name": "klavi.avg_period_regular_salary.avg.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00298",
                    "label_name": "klavi.transactions.business_income.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00299",
                    "label_name": "klavi.transactions.business_income.tot.last_60_days",
                    "label_value": 510
                },
                {
                    "label_code": "K00300",
                    "label_name": "klavi.transactions.business_income.tot.last_90_days",
                    "label_value": 510
                },
                {
                    "label_code": "K00301",
                    "label_name": "klavi.transactions.business_income_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00302",
                    "label_name": "klavi.transactions.business_income_transaction_count.tot.last_60_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00303",
                    "label_name": "klavi.transactions.business_income_transaction_count.tot.last_90_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00304",
                    "label_name": "klavi.transactions.period_with_business_income.tot.last_90_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00305",
                    "label_name": "klavi.avg_period_business_income.avg.last_90_days",
                    "label_value": 510
                },
                {
                    "label_code": "K00306",
                    "label_name": "klavi.transactions.other_recurrent_income.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00307",
                    "label_name": "klavi.transactions.other_recurrent_income.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00308",
                    "label_name": "klavi.transactions.other_recurrent_income.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00309",
                    "label_name": "klavi.transactions.other_recurrent_income_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00310",
                    "label_name": "klavi.transactions.other_recurrent_income_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00311",
                    "label_name": "klavi.transactions.other_recurrent_income_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00312",
                    "label_name": "klavi.transactions.period_with_other_recurrent_income.tot.last_90_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00313",
                    "label_name": "klavi.avg_period_other_recurrent_income.avg.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00314",
                    "label_name": "klavi.transactions.bonus_income.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00315",
                    "label_name": "klavi.transactions.bonus_income.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00316",
                    "label_name": "klavi.transactions.bonus_income.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00317",
                    "label_name": "klavi.transactions.bonus_income_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00318",
                    "label_name": "klavi.transactions.bonus_income_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00319",
                    "label_name": "klavi.transactions.bonus_income_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00320",
                    "label_name": "klavi.transactions.period_with_bonus_income.tot.last_90_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00321",
                    "label_name": "klavi.avg_period_bonus_income.avg.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00322",
                    "label_name": "klavi.transactions.retirement_pension.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00323",
                    "label_name": "klavi.transactions.retirement_pension.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00324",
                    "label_name": "klavi.transactions.retirement_pension.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00325",
                    "label_name": "klavi.transactions.retirement_pension_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00326",
                    "label_name": "klavi.transactions.retirement_pension_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00327",
                    "label_name": "klavi.transactions.retirement_pension_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00328",
                    "label_name": "klavi.transactions.period_with_retirement_pension.tot.last_90_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00329",
                    "label_name": "klavi.avg_period_retirement_pension.avg.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00330",
                    "label_name": "klavi.transactions.sponsorship_pension.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00331",
                    "label_name": "klavi.transactions.sponsorship_pension.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00332",
                    "label_name": "klavi.transactions.sponsorship_pension.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00333",
                    "label_name": "klavi.transactions.sponsorship_pension_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00334",
                    "label_name": "klavi.transactions.sponsorship_pension_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00335",
                    "label_name": "klavi.transactions.sponsorship_pension_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00336",
                    "label_name": "klavi.transactions.period_with_sponsorship_pension.tot.last_90_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00337",
                    "label_name": "klavi.avg_period_sponsorship_pension.avg.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00338",
                    "label_name": "klavi.transactions.government_support.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00339",
                    "label_name": "klavi.transactions.government_support.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00340",
                    "label_name": "klavi.transactions.government_support.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00341",
                    "label_name": "klavi.transactions.government_support_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00342",
                    "label_name": "klavi.transactions.government_support_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00343",
                    "label_name": "klavi.transactions.government_support_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00344",
                    "label_name": "klavi.transactions.period_with_government_support.tot.last_90_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00345",
                    "label_name": "klavi.avg_period_government_support.avg.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00346",
                    "label_name": "klavi.transactions.other_remuneration.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00347",
                    "label_name": "klavi.transactions.other_remuneration.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00348",
                    "label_name": "klavi.transactions.other_remuneration.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00349",
                    "label_name": "klavi.transactions.other_remuneration_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00350",
                    "label_name": "klavi.transactions.other_remuneration_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00351",
                    "label_name": "klavi.transactions.other_remuneration_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00352",
                    "label_name": "klavi.transactions.period_with_other_remuneration.tot.last_90_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00353",
                    "label_name": "klavi.avg_period_other_remuneration.avg.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00354",
                    "label_name": "klavi.transactions.investment_redemption.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00355",
                    "label_name": "klavi.transactions.investment_redemption.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00356",
                    "label_name": "klavi.transactions.investment_redemption.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00357",
                    "label_name": "klavi.transactions.investment_redemption_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00358",
                    "label_name": "klavi.transactions.investment_redemption_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00359",
                    "label_name": "klavi.transactions.investment_redemption_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00360",
                    "label_name": "klavi.transactions.period_with_investment_redemption.tot.last_90_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00361",
                    "label_name": "klavi.avg_period_investment_redemption.avg.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00362",
                    "label_name": "klavi.transactions.investment_dividend.tot.last_30_days",
                    "label_value": 2.85
                },
                {
                    "label_code": "K00363",
                    "label_name": "klavi.transactions.investment_dividend.tot.last_60_days",
                    "label_value": 2.85
                },
                {
                    "label_code": "K00364",
                    "label_name": "klavi.transactions.investment_dividend.tot.last_90_days",
                    "label_value": 2.85
                },
                {
                    "label_code": "K00365",
                    "label_name": "klavi.transactions.investment_dividend_transaction_count.tot.last_30_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00366",
                    "label_name": "klavi.transactions.investment_dividend_transaction_count.tot.last_60_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00367",
                    "label_name": "klavi.transactions.investment_dividend_transaction_count.tot.last_90_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00368",
                    "label_name": "klavi.transactions.period_with_investment_dividend.tot.last_90_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00369",
                    "label_name": "klavi.avg_period_investment_dividend.avg.last_90_days",
                    "label_value": 2.85
                },
                {
                    "label_code": "K00370",
                    "label_name": "klavi.transactions.house_rental_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00371",
                    "label_name": "klavi.transactions.house_rental_expenses.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00372",
                    "label_name": "klavi.transactions.house_rental_expenses.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00373",
                    "label_name": "klavi.transactions.house_rental_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00374",
                    "label_name": "klavi.transactions.house_rental_expenses_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00375",
                    "label_name": "klavi.transactions.house_rental_expenses_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00376",
                    "label_name": "klavi.transactions.water_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00377",
                    "label_name": "klavi.transactions.water_expenses.tot.last_60_days",
                    "label_value": 67.93
                },
                {
                    "label_code": "K00378",
                    "label_name": "klavi.transactions.water_expenses.tot.last_90_days",
                    "label_value": 67.93
                },
                {
                    "label_code": "K00379",
                    "label_name": "klavi.transactions.water_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00380",
                    "label_name": "klavi.transactions.water_expenses_transaction_count.tot.last_60_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00381",
                    "label_name": "klavi.transactions.water_expenses_transaction_count.tot.last_90_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00382",
                    "label_name": "klavi.transactions.eletricity_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00383",
                    "label_name": "klavi.transactions.eletricity_expenses.tot.last_60_days",
                    "label_value": 146.53
                },
                {
                    "label_code": "K00384",
                    "label_name": "klavi.transactions.eletricity_expenses.tot.last_90_days",
                    "label_value": 146.53
                },
                {
                    "label_code": "K00385",
                    "label_name": "klavi.transactions.eletricity_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00386",
                    "label_name": "klavi.transactions.eletricity_expenses_transaction_count.tot.last_60_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00387",
                    "label_name": "klavi.transactions.eletricity_expenses_transaction_count.tot.last_90_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00388",
                    "label_name": "klavi.transactions.gas_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00389",
                    "label_name": "klavi.transactions.gas_expenses.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00390",
                    "label_name": "klavi.transactions.gas_expenses.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00391",
                    "label_name": "klavi.transactions.gas_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00392",
                    "label_name": "klavi.transactions.gas_expenses_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00393",
                    "label_name": "klavi.transactions.gas_expenses_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00394",
                    "label_name": "klavi.transactions.telecom_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00395",
                    "label_name": "klavi.transactions.telecom_expenses.tot.last_60_days",
                    "label_value": 159.06
                },
                {
                    "label_code": "K00396",
                    "label_name": "klavi.transactions.telecom_expenses.tot.last_90_days",
                    "label_value": 159.06
                },
                {
                    "label_code": "K00397",
                    "label_name": "klavi.transactions.telecom_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00398",
                    "label_name": "klavi.transactions.telecom_expenses_transaction_count.tot.last_60_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00399",
                    "label_name": "klavi.transactions.telecom_expenses_transaction_count.tot.last_90_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00400",
                    "label_name": "klavi.transactions.pubic_transportation_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00401",
                    "label_name": "klavi.transactions.pubic_transportation_expenses.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00402",
                    "label_name": "klavi.transactions.pubic_transportation_expenses.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00403",
                    "label_name": "klavi.transactions.pubic_transportation_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00404",
                    "label_name": "klavi.transactions.pubic_transportation_expenses_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00405",
                    "label_name": "klavi.transactions.pubic_transportation_expenses_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00406",
                    "label_name": "klavi.transactions.taxi_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00407",
                    "label_name": "klavi.transactions.taxi_expenses.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00408",
                    "label_name": "klavi.transactions.taxi_expenses.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00409",
                    "label_name": "klavi.transactions.taxi_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00410",
                    "label_name": "klavi.transactions.taxi_expenses_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00411",
                    "label_name": "klavi.transactions.taxi_expenses_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00412",
                    "label_name": "klavi.transactions.pets_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00413",
                    "label_name": "klavi.transactions.pets_expenses.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00414",
                    "label_name": "klavi.transactions.pets_expenses.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00415",
                    "label_name": "klavi.transactions.pets_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00416",
                    "label_name": "klavi.transactions.pets_expenses_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00417",
                    "label_name": "klavi.transactions.pets_expenses_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00418",
                    "label_name": "klavi.transactions.gambling_betting_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00419",
                    "label_name": "klavi.transactions.gambling_betting_expenses.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00420",
                    "label_name": "klavi.transactions.gambling_betting_expenses.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00421",
                    "label_name": "klavi.transactions.gambling_betting_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00422",
                    "label_name": "klavi.transactions.gambling_betting_expenses_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00423",
                    "label_name": "klavi.transactions.gambling_betting_expenses_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00424",
                    "label_name": "klavi.transactions.luxury_product_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00425",
                    "label_name": "klavi.transactions.luxury_product_expenses.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00426",
                    "label_name": "klavi.transactions.luxury_product_expenses.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00427",
                    "label_name": "klavi.transactions.luxury_product_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00428",
                    "label_name": "klavi.transactions.luxury_product_expenses_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00429",
                    "label_name": "klavi.transactions.luxury_product_expenses_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00430",
                    "label_name": "klavi.transactions.professional_membership_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00431",
                    "label_name": "klavi.transactions.professional_membership_expenses.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00432",
                    "label_name": "klavi.transactions.professional_membership_expenses.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00433",
                    "label_name": "klavi.transactions.professional_membership_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00434",
                    "label_name": "klavi.transactions.professional_membership_expenses_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00435",
                    "label_name": "klavi.transactions.professional_membership_expenses_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00436",
                    "label_name": "klavi.transactions.education_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00437",
                    "label_name": "klavi.transactions.education_expenses.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00438",
                    "label_name": "klavi.transactions.education_expenses.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00439",
                    "label_name": "klavi.transactions.education_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00440",
                    "label_name": "klavi.transactions.education_expenses_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00441",
                    "label_name": "klavi.transactions.education_expenses_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00442",
                    "label_name": "klavi.transactions.travel_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00443",
                    "label_name": "klavi.transactions.travel_expenses.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00444",
                    "label_name": "klavi.transactions.travel_expenses.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00445",
                    "label_name": "klavi.transactions.travel_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00446",
                    "label_name": "klavi.transactions.travel_expenses_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00447",
                    "label_name": "klavi.transactions.travel_expenses_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00448",
                    "label_name": "klavi.transactions.childcare_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00449",
                    "label_name": "klavi.transactions.childcare_expenses.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00450",
                    "label_name": "klavi.transactions.childcare_expenses.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00451",
                    "label_name": "klavi.transactions.childcare_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00452",
                    "label_name": "klavi.transactions.childcare_expenses_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00453",
                    "label_name": "klavi.transactions.childcare_expenses_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00454",
                    "label_name": "klavi.transactions.dining_drinks_expenses.tot.last_30_days",
                    "label_value": 74.74
                },
                {
                    "label_code": "K00455",
                    "label_name": "klavi.transactions.dining_drinks_expenses.tot.last_60_days",
                    "label_value": 74.74
                },
                {
                    "label_code": "K00456",
                    "label_name": "klavi.transactions.dining_drinks_expenses.tot.last_90_days",
                    "label_value": 74.74
                },
                {
                    "label_code": "K00457",
                    "label_name": "klavi.transactions.dining_drinks_expenses_transaction_count.tot.last_30_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00458",
                    "label_name": "klavi.transactions.dining_drinks_expenses_transaction_count.tot.last_60_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00459",
                    "label_name": "klavi.transactions.dining_drinks_expenses_transaction_count.tot.last_90_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00460",
                    "label_name": "klavi.transactions.mortgage_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00461",
                    "label_name": "klavi.transactions.mortgage_expenses.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00462",
                    "label_name": "klavi.transactions.mortgage_expenses.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00463",
                    "label_name": "klavi.transactions.mortgage_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00464",
                    "label_name": "klavi.transactions.mortgage_expenses_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00465",
                    "label_name": "klavi.transactions.mortgage_expenses_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00466",
                    "label_name": "klavi.transactions.health_insurance_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00467",
                    "label_name": "klavi.transactions.health_insurance_expenses.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00468",
                    "label_name": "klavi.transactions.health_insurance_expenses.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00469",
                    "label_name": "klavi.transactions.health_insurance_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00470",
                    "label_name": "klavi.transactions.health_insurance_expenses_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00471",
                    "label_name": "klavi.transactions.health_insurance_expenses_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00472",
                    "label_name": "klavi.transactions.car_insurance_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00473",
                    "label_name": "klavi.transactions.car_insurance_expenses.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00474",
                    "label_name": "klavi.transactions.car_insurance_expenses.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00475",
                    "label_name": "klavi.transactions.car_insurance_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00476",
                    "label_name": "klavi.transactions.car_insurance_expenses_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00477",
                    "label_name": "klavi.transactions.car_insurance_expenses_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00478",
                    "label_name": "klavi.transactions.other_insurance_expenses.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00479",
                    "label_name": "klavi.transactions.other_insurance_expenses.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00480",
                    "label_name": "klavi.transactions.other_insurance_expenses.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00481",
                    "label_name": "klavi.transactions.other_insurance_expenses_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00482",
                    "label_name": "klavi.transactions.other_insurance_expenses_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00483",
                    "label_name": "klavi.transactions.other_insurance_expenses_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00484",
                    "label_name": "klavi.transactions.total_liabilities.tot.last_30_days",
                    "label_value": 18.65
                },
                {
                    "label_code": "K00485",
                    "label_name": "klavi.transactions.total_liabilities.tot.last_60_days",
                    "label_value": 397.17
                },
                {
                    "label_code": "K00486",
                    "label_name": "klavi.transactions.total_liabilities.tot.last_90_days",
                    "label_value": 397.17
                },
                {
                    "label_code": "K00487",
                    "label_name": "klavi.transactions.total_liabilities_transaction_count.tot.last_30_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00488",
                    "label_name": "klavi.transactions.total_liabilities_transaction_count.tot.last_60_days",
                    "label_value": 6
                },
                {
                    "label_code": "K00489",
                    "label_name": "klavi.transactions.total_liabilities_transaction_count.tot.last_90_days",
                    "label_value": 6
                },
                {
                    "label_code": "K00490",
                    "label_name": "klavi.transactions.number_of_liabilities_streams.tot.last_30_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00491",
                    "label_name": "klavi.transactions.number_of_liabilities_streams.tot.last_60_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00492",
                    "label_name": "klavi.transactions.number_of_liabilities_streams.tot.last_90_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00493",
                    "label_name": "klavi.transactions.creditcard_liabilities.tot.last_30_days",
                    "label_value": 18.65
                },
                {
                    "label_code": "K00494",
                    "label_name": "klavi.transactions.creditcard_liabilities.tot.last_60_days",
                    "label_value": 23.65
                },
                {
                    "label_code": "K00495",
                    "label_name": "klavi.transactions.creditcard_liabilities.tot.last_90_days",
                    "label_value": 23.65
                },
                {
                    "label_code": "K00496",
                    "label_name": "klavi.transactions.creditcard_liabilities_transaction_count.tot.last_30_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00497",
                    "label_name": "klavi.transactions.creditcard_liabilities_transaction_count.tot.last_60_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00498",
                    "label_name": "klavi.transactions.creditcard_liabilities_transaction_count.tot.last_90_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00499",
                    "label_name": "klavi.transactions.period_with_creditcard_liabilities.tot.last_90_days",
                    "label_value": 2
                },
                {
                    "label_code": "K00500",
                    "label_name": "klavi.avg_period_creditcard_liabilities.avg.last_90_days",
                    "label_value": 11.83
                },
                {
                    "label_code": "K00501",
                    "label_name": "klavi.transactions.mortgage_liabilities.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00502",
                    "label_name": "klavi.transactions.mortgage_liabilities.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00503",
                    "label_name": "klavi.transactions.mortgage_liabilities.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00504",
                    "label_name": "klavi.transactions.mortgage_liabilities_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00505",
                    "label_name": "klavi.transactions.mortgage_liabilities_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00506",
                    "label_name": "klavi.transactions.mortgage_liabilities_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00507",
                    "label_name": "klavi.transactions.period_with_mortgage_liabilities.tot.last_90_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00508",
                    "label_name": "klavi.avg_period_mortgage_liabilities.avg.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00509",
                    "label_name": "klavi.transactions.student_loan_liabilities.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00510",
                    "label_name": "klavi.transactions.student_loan_liabilities.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00511",
                    "label_name": "klavi.transactions.student_loan_liabilities.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00512",
                    "label_name": "klavi.transactions.student_loan_liabilities_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00513",
                    "label_name": "klavi.transactions.student_loan_liabilities_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00514",
                    "label_name": "klavi.transactions.student_loan_liabilities_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00515",
                    "label_name": "klavi.transactions.period_with_student_loan_liabilities.tot.last_90_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00516",
                    "label_name": "klavi.avg_period_student_loan_liabilities.avg.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00517",
                    "label_name": "klavi.transactions.bank_loan_liabilities.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00518",
                    "label_name": "klavi.transactions.bank_loan_liabilities.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00519",
                    "label_name": "klavi.transactions.bank_loan_liabilities.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00520",
                    "label_name": "klavi.transactions.bank_loan_liabilities_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00521",
                    "label_name": "klavi.transactions.bank_loan_liabilities_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00522",
                    "label_name": "klavi.transactions.bank_loan_liabilities_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00523",
                    "label_name": "klavi.transactions.period_with_bank_loan_liabilities.tot.last_90_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00524",
                    "label_name": "klavi.avg_period_bank_loan_liabilities.avg.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00525",
                    "label_name": "klavi.transactions.other_recurrent_liabilities.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00526",
                    "label_name": "klavi.transactions.other_recurrent_liabilities.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00527",
                    "label_name": "klavi.transactions.other_recurrent_liabilities.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00528",
                    "label_name": "klavi.transactions.other_recurrent_liabilities_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00529",
                    "label_name": "klavi.transactions.other_recurrent_liabilities_transaction_count.tot.last_60_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00530",
                    "label_name": "klavi.transactions.other_recurrent_liabilities_transaction_count.tot.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00531",
                    "label_name": "klavi.transactions.period_with_other_recurrent_liabilities.tot.last_90_days",
                    "label_value": -999999
                },
                {
                    "label_code": "K00532",
                    "label_name": "klavi.avg_period_other_recurrent_liabilities.avg.last_90_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00533",
                    "label_name": "klavi.transactions.utilities&rental_liabilities.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00534",
                    "label_name": "klavi.transactions.utilities&rental_liabilities.tot.last_60_days",
                    "label_value": 373.52
                },
                {
                    "label_code": "K00535",
                    "label_name": "klavi.transactions.utilities&rental_liabilities.tot.last_90_days",
                    "label_value": 373.52
                },
                {
                    "label_code": "K00536",
                    "label_name": "klavi.transactions.utilities&rental_liabilities_transaction_count.tot.last_30_days",
                    "label_value": 0
                },
                {
                    "label_code": "K00537",
                    "label_name": "klavi.transactions.utilities&rental_liabilities_transaction_count.tot.last_60_days",
                    "label_value": 4
                },
                {
                    "label_code": "K00538",
                    "label_name": "klavi.transactions.utilities&rental_liabilities_transaction_count.tot.last_90_days",
                    "label_value": 4
                },
                {
                    "label_code": "K00539",
                    "label_name": "klavi.transactions.period_with_utilities&rental_liabilities.tot.last_90_days",
                    "label_value": 1
                },
                {
                    "label_code": "K00540",
                    "label_name": "klavi.avg_period_utilities&rental_liabilities.avg.last_90_days",
                    "label_value": 373.52
                }
            ]
        }
    }
}

