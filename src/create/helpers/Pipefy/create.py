from .GqlClient import PipefyClient

from .query import createCard
from .search import PipefyDataFacade

HE_BACEM_PHASE_ID = "319165329"
FI_BACEM_PHASE_ID = "319165324"


def make_variables(facade, title, report_type, other_report, other_json_report_url, json_report_url, enquiry_cpf,
                   xlsx_report_url, other_xlsx_report_url):
    fields = [{"field_id": "nome", "field_value": title}, {"field_id": "cpf_cnpj", "field_value": enquiry_cpf},
              {"field_id": f'{report_type}_xlsx', "field_value": xlsx_report_url},
              {"field_id": f'{other_report}_xlsx', "field_value": other_xlsx_report_url},
              {"field_id": f'{report_type}_json', "field_value": json_report_url},
              {"field_id": f'{other_report}_json', "field_value": other_json_report_url}]
    return {"input": {"pipe_id": "303111869", "parent_ids": facade.related_cards, "fields_attributes": fields}}


def send_to_pipefy(variables):
    client = PipefyClient()
    return client.post(createCard, variables)


def find_relation(enquiry_cpf):
    he_bacem_phase_id = HE_BACEM_PHASE_ID
    fi_bacem_phase_id = FI_BACEM_PHASE_ID
    facade = PipefyDataFacade(he_phase_id=he_bacem_phase_id, fi_phase_id=fi_bacem_phase_id, document_number=enquiry_cpf)
    facade.run()
    return facade


def make_report_urls(enquiry_cpf, report_type):
    json_key = f"{enquiry_cpf}/{report_type}.json"
    xlsx_key = f"{enquiry_cpf}/{report_type}.xlsx"
    json_report_url = f"https://s3.amazonaws.com/openfinance-dev/{json_key}"
    xlsx_report_url = f"https://s3.amazonaws.com/openfinance-dev/{xlsx_key}"
    return json_report_url, xlsx_report_url


def create_pipefy_card(response):
    enquiry_cpf = response['enquiry_cpf']
    title = response['title']

    # Assuming report_type and other_report as 'category_checking' and 'income' respectively
    report_type = 'category_checking'
    other_report = 'income'

    json_report_url, xlsx_report_url = make_report_urls(enquiry_cpf, report_type)
    other_json_report_url, other_xlsx_report_url = make_report_urls(enquiry_cpf, other_report)

    facade = find_relation(enquiry_cpf)
    variables = make_variables(facade, title, report_type, other_report, other_json_report_url, json_report_url,
                               enquiry_cpf, xlsx_report_url, other_xlsx_report_url)

    card = send_to_pipefy(variables)
    print("card", card)
    return card['data']['createCard']['card']['id']

# if __name__ == "__main__":
#     response = {'category_checking': {
#         'json_report_url': 'https://s3.amazonaws.com/openfinance-dev/70079872140/category_checking.json',
#         'xlsx_report_url': 'https://s3.amazonaws.com/openfinance-dev/70079872140/category_checking.xlsx'},
#                 'enquiry_cpf': '70079872140', 'id': 'c3dfc94f-2644-4013-83f8-4b6f974e2e96',
#                 'income': {'json_report_url': 'https://s3.amazonaws.com/openfinance-dev/70079872140/income.json',
#                            'xlsx_report_url': 'https://s3.amazonaws.com/openfinance-dev/70079872140/income.xlsx'},
#                 'title': 'Usuaro anonimo'}
#
#     main(response)
