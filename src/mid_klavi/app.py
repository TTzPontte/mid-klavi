from http import HTTPStatus

from shared.helpers.handler_base import Handler, Result
from shared.helpers.hw_helper import helper_fn
from shared.parsers.event_logger import parse_payload_into_logger_object
from shared.models.event_logger import Logger

payload_example = {
    "code":200,
    "msg":"ok",
    "report_time":"2020-02-08 03:49:38",
    "data":{
        "enquiry_cpf":"12345678901",
        "user_consent":"Yes",
        "allow_autoupdate":"Yes",
        "connection_key":"pQuKXrCJU0kUDQO65J4k",
        "connection_id":"a71c899f-11eb-231f-97c4-4b2c16484587",
        "institution_id":"342",
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

class MidKlavi(Handler):

    def handler(self):
        # return {
        #     "statusCode": 200,
        #     "body": json.dumps({
        #         "message": "hello world",
        #         # "location": ip.text.replace("\n", "")
        #     }),
        # }
        event_logger_config = parse_payload_into_logger_object(payload_example)
        event_logger = Logger(**event_logger_config)
        event_logger.save()
        return Result(HTTPStatus.OK, {"message": "hello world from mid-klavi"})


def lambda_handler(event, context):
    helper_fn()
    return MidKlavi(event, context).run()
