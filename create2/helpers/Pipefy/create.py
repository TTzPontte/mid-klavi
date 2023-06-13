from common.graphql.GqlClient import PipefyClient
from .query import createCard


def send_to_pipefy(variables):
    client = PipefyClient()
    return client.post(createCard, variables)


def make_variables(facade, title, report_type, other_report, other_json_report_url, json_report_url, enquiry_cpf,
                   xlsx_report_url, other_xlsx_report_url):
    return {"input": {

        "pipe_id": "303111869", "parent_ids": facade.related_cards,
        "fields_attributes": [{"field_id": "nome", "field_value": title},
                              {"field_id": "cpf_cnpj", "field_value": enquiry_cpf},
                              {"field_id": f'{report_type}_xlsx', "field_value": xlsx_report_url},
                              {"field_id": f'{other_report}_xlsx', "field_value": other_xlsx_report_url},
                              {"field_id": f'{report_type}_json', "field_value": json_report_url},
                              {"field_id": f'{other_report}_json', "field_value": other_json_report_url}]}}
