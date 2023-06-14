from gql_client import PipefyClient

from query import createCard
from search import PipefyDataFacade


def make_variables(facade, title, report_type, other_report, other_json_report_url, json_report_url, enquiry_cpf,
                   xlsx_report_url, other_xlsx_report_url):
    fields = [
        {"field_id": "nome", "field_value": title},
        {"field_id": "cpf_cnpj", "field_value": enquiry_cpf},
        {"field_id": f'{report_type}_xlsx', "field_value": xlsx_report_url},
        {"field_id": f'{other_report}_xlsx', "field_value": other_xlsx_report_url},
        {"field_id": f'{report_type}_json', "field_value": json_report_url},
        {"field_id": f'{other_report}_json', "field_value": other_json_report_url}
    ]
    return {"input": {"pipe_id": "303111869", "parent_ids": facade.related_cards, "fields_attributes": fields}}


def send_to_pipefy(variables):
    client = PipefyClient()
    return client.post(createCard, variables)


def find_relation(enquiry_cpf):
    he_bacem_phase_id = "319165329"
    fi_bacem_phase_id = "319165324"
    facade = PipefyDataFacade(he_phase_id=he_bacem_phase_id, fi_phase_id=fi_bacem_phase_id, document_number=enquiry_cpf)
    facade.run()
    return facade


def make_report_urls(enquiry_cpf, report_type):
    json_key = f"{enquiry_cpf}/{report_type}.json"
    xlsx_key = f"{enquiry_cpf}/{report_type}.xlsx"
    json_report_url = f"https://s3.amazonaws.com/openfinance-dev/{json_key}"
    xlsx_report_url = f"https://s3.amazonaws.com/openfinance-dev/{xlsx_key}"
    return json_report_url, xlsx_report_url


def main():
    json_report_url, xlsx_report_url = make_report_urls(enquiry_cpf, report_type)
    other_json_report_url, other_xlsx_report_url = make_report_urls(enquiry_cpf, other_report)

    facade = find_relation(enquiry_cpf)
    variables = make_variables(facade, title, report_type, other_report, other_json_report_url,
                               json_report_url, enquiry_cpf, xlsx_report_url, other_xlsx_report_url)

    card = send_to_pipefy(variables)
    return card


if __name__ == "__main__":
    enquiry_cpf = "..."
    title = "..."
    report_type = "..."
    other_report = "..."

    main()
