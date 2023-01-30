from shared.exports.klavi_report import export_klavi_report_to_excel
from shared.factory.klavi_report import build_report_from_klavi_payload
from shared.repository.klavi_report import KlaviReportRepository
import pandas as pd
import io

payload_category_checking = {
    "code":200,
    "msg":"ok",
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

if __name__ == "__main__":
    report_repository = KlaviReportRepository()
    klavi_report = build_report_from_klavi_payload(payload_category_checking)
    report_from_database = report_repository.getByReportId('399eba11-059e-4286-a164-4383f7e20a0c', '12345678901')
    excel_file_buffer = io.BytesIO()
    excel_file = export_klavi_report_to_excel(klavi_report, excel_file_buffer)
    excel_file_buffer.close()


    print("OOOPA")