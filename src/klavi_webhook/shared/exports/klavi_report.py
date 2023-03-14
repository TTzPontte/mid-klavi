import os
import json
from shared.models.klavi_report import KlaviReportExcelSchema
from shared.exports.category_checking import export_category_checkings_to_excel
from shared.exports.category_creditcard import export_category_creditcard_to_excel
from shared.exports.liabilities import export_liabilities_to_excel
from shared.exports.financial_insight import export_financial_insight_to_excel
from shared.helpers.pipefy.client import PipefyClient
from Pipefy.main import main as search_for_related_cards
from Pipefy.main import main_klavi as search_for_related_cards_klavi


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


def _insert_into_pipefy_database(report):
    database_id = os.getenv("PIPEFY_KLAVI_DATABASE_ID")
    bucket_name = os.getenv("KLAVI_REPORTS_BUCKET_NAME")
    excel_object_key = "{report_id}/{report_type}.xlsx".format(report_id=report.report_id,
                                                               report_type=report.report_type)
    json_object_key = "{report_id}/{report_type}.json".format(report_id=report.report_id,
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
        title = report.income[0].account_holder

    received_response = pipefy_client.insert_into_database(new_item, database_id, title)
    json_response = json.loads(received_response.text)
    record_id = json_response.get("data").get("createTableRecord").get("table_record").get("id")

    return record_id

def _get_related_cards(report):
    cpf_to_search = report.enquiry_cpf
    bacen_stage_he_id = os.getenv("PIPEFY_KLAVI_BACEN_STAGE_HE_ID")
    bacen_stage_fi_id = os.getenv("PIPEFY_KLAVI_BACEN_STAGE_FI_ID")
    klavi_stage = os.getenv("PIPEFY_KLAVI_STAGE_ID")
    related_he_cards = search_for_related_cards(bacen_stage_he_id, cpf_to_search)
    related_fi_cards = search_for_related_cards(bacen_stage_fi_id, cpf_to_search)
    klavi_cards = search_for_related_cards_klavi(klavi_stage, cpf_to_search)

    he_cards = []
    fi_cards = []
    if related_he_cards is not None:
        he_cards = [related_he_cards.id]
    if related_fi_cards is not None:
        fi_cards = [related_fi_cards.id]

    return {
        "he_cards": he_cards,
        "fi_cards": fi_cards,
        "klavi_cards": klavi_cards
    }

def _create_new_card_into_pipefy(report, he_cards, fi_cards, record_id):
    pipefy_client = PipefyClient()
    pipe_id = os.getenv("PIPEFY_KLAVI_PIPE_ID")
    title = "unknow"
    if report.report_type == "category_checking":
        title = report.category_checkings[0].holder_name
    if report.report_type == "income":
        title = report.income[0].account_holder

    card_data = [
        {"field_id": 'cpf_cnpj', "field_value": report.enquiry_cpf},
        {"field_id": "nome", "field_value": title},
        {"field_id": "esteira_he_dev", "field_value": he_cards},
        {"field_id": "esteira_fi_dev", "field_value": fi_cards}
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
    pipefy_client.create_card_into_pipe(card_data, pipe_id)

def _update_card_into_pipefy(report, klavi_card, record_id):
    pipefy_client = PipefyClient()
    card_id = klavi_card.id
    field_id = ""
    value = record_id

    if report.report_type == "category_checking":
        field_id = "category_checking"
    if report.report_type == "income":
        field_id = "income"
    pipefy_client.update_card_field(card_id, field_id, value)

def export_klavi_report_to_pipefy_database(report):
    record_id = _insert_into_pipefy_database(report)
    related_cards = _get_related_cards(report)

    if related_cards.get("klavi_cards")  is not None:
        _update_card_into_pipefy(report, related_cards.get("klavi_cards"), record_id)
    else:
        _create_new_card_into_pipefy(report, related_cards.get("he_cards"), related_cards.get("fi_cards"), record_id)

