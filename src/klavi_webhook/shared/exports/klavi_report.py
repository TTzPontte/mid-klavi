import os
import json
from shared.models.klavi_report import KlaviReportExcelSchema
from shared.exports.category_checking import export_category_checkings_to_excel
from shared.exports.category_creditcard import export_category_creditcard_to_excel
from shared.exports.liabilities import export_liabilities_to_excel
from shared.exports.financial_insight import export_financial_insight_to_excel
from shared.helpers.pipefy.client import PipefyClient

import pandas


def export_klavi_report_to_excel(report, output):
    report_schema = KlaviReportExcelSchema()
    pandas_excel_writter = pandas.ExcelWriter(output)
    data_frame = pandas.DataFrame(report_schema.dump(report), index=[0])
    data_frame.to_excel(pandas_excel_writter, sheet_name='Report')

    if report.report_type == 'category_checking':
        export_category_checkings_to_excel(report, writer=pandas_excel_writter)
    if report.report_type == 'category_creditcard':
        export_category_creditcard_to_excel(report, writer=pandas_excel_writter)
    if report.report_type == 'liabilities':
        export_liabilities_to_excel(report, writer=pandas_excel_writter)
    if report.report_type == 'financial_insight':
        export_financial_insight_to_excel(report, writer=pandas_excel_writter)

    pandas_excel_writter.close()

    return pandas_excel_writter

def export_klavi_report_to_pipefy_database(report):
    database_id = os.getenv("PIPEFY_KLAVI_DATABASE_ID")
    bucket_name = os.getenv("KLAVI_REPORTS_BUCKET_NAME")
    excel_object_key = "{report_id}/{report_type}.xlsx".format(report_id=report.report_id,
                                                         report_type=report.report_type)
    json_object_key = "{report_id}/{report_type}.xlsx".format(report_id=report.report_id,
                                                               report_type=report.report_type)
    excel_object_url = "https://{bucket_name}.s3.amazonaws.com/{object_key}".format(bucket_name=bucket_name,
                                                                              object_key=excel_object_key)
    json_object_url = "https://{bucket_name}.s3.amazonaws.com/{object_key}".format(bucket_name=bucket_name,
                                                                                    object_key=json_object_key)

    new_item = [
        {"field_id": "klavi_excel", "field_value": excel_object_url},
        {"field_id": "klavi_json", "field_value": json_object_url},
        {"field_id": "cpf_cnpj", "field_value": report.enquiry_cpf}
    ]
    pipefy_client = PipefyClient()
    title = "unknow"
    if report.report_type == "category_checking":
        title = report.category_checkings[0].holder_name
    if report.report_type == "income":
        title = report.income[0].holder_name
    received_response = pipefy_client.insert_into_database(new_item, database_id, title)
    print("Response From pipefy")
    print(received_response.text)
    json_response = json.loads(received_response.text)
    print("Le JSON Response")
    print(json_response)
    record_id = json_response.get("data").get("createTableRecord").get("table_record").get("id")
    print("Le Record ID")
    print(record_id)
    pipe_id = "303051849"
    card_data = [
        {"field_id": 'cpf_cnpj', "field_value": report.enquiry_cpf},
        {"field_id": "nome", "field_value": title}
    ]
    if report.report_type == "category_checking":
        card_data.append(
            {
                "field_id": "category_checking",
                "field_value": [record_id]
            }
        )
    if report.report_type == "income":
        card_data.append(
            {
                "field_id": "income",
                "field_value": [record_id]
            }
        )
    card_save_response = pipefy_client.create_card_into_pipe(card_data, pipe_id)
    print("Card Save Response")
    print(card_save_response.text)
