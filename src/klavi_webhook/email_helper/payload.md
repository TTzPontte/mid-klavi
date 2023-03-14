Estrutura comum em todos os relatórios de dados

```json
{
  "code": 200,
  "msg": "ok",
  "report_time": "2019-12-23 06:10:43",
  "data": {
    "enquiry_cpf": "12345678901",
    "user_consent": "Yes",
    "allow_autoupdate": "Yes",
    "connection_key": "gPuKXrCJU0kUDQO65J4k",
    "connection_id": "f45c899f-11eb-231f-97c4-4b2c16484587",
    "institution_id": "001",
    "report_type": "category_checking",
    "report_id": "4b2c1648-231f-11eb-97c4-f45c899f4587",
    "report_version": "V1",
    "report specification": []
  }
}
```

Category_checking

```json
{
  "code": 200,
  "msg": "ok",
  "report_time": "2019-12-23 06:10:43",
  "data": {
    "enquiry_cpf": "12345678901",
    "user_consent": "Yes",
    "allow_autoupdate": "Yes",
    "connection_key": "gPuKXrCJU0kUDQO65J4k",
    "connection_id": "f45c899f-11eb-231f-97c4-4b2c16484587",
    "institution_id": "033",
    "report_type": "category_checking",
    "report_id": "4b2c1648-231f-11eb-97c4-f45c899f4587",
    "report_version": "V1",
    "Category_checking": [
      {
        "bank_name": "Santander",
        "bacen_name": "BANCO SANTANDER (BRASIL) S.A.",
        "bacen_id": "033",
        "bank_branch": "1234",
        "account": "12.345678.9",
        "operation_code": "001",
        "cpf_verified": "12345678901",
        "holder_name": "Usuaro anonimo",
        "balance": 18.75,
        "TransactionDetail": [
          {
            "trans_date": "2019-12-23",
            "trans_amount": -150.05,
            "trans_description": "PREST EMPRESTIMOS/FINANCIAMENTOS AYMORE",
            "balance": 18.75,
            "category": "Empréstimo"
          },
          {
            "trans_date": "2019-12-20",
            "trans_amount": 150,
            "trans_description": "TED MESMA TITULARIDADE CIP 237-3750-0000001234567",
            "balance": 168.8,
            "category": "Transferência"
          }
        ]
      }
    ]
  }
}
```

Income

```json

{
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
```