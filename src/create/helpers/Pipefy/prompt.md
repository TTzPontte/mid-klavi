# create.py

```python
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

```

# search.py

```python
from dataclasses import dataclass, field

from .GqlClient import PipefyClient
from .query import get_cards_from_phase

TOMADORES_DO_EMPRESTIMO_FIELD_ID = "tomadores_do_emprestimo"


def has_tomadores_do_emprestimo(card_fields):
    for field in card_fields:
        if field["field"]["id"] == TOMADORES_DO_EMPRESTIMO_FIELD_ID and field["array_value"]:
            return True
    return False


def normalize_card_data(card):
    card_fields = card["node"]["fields"]
    card_data = {"id": card["node"]["id"]}
    for field in card_fields:
        field_id = field["field"]["id"]
        field_name = field["name"]
        field_value = field["value"]

        card_data[field_id] = {"name": field_name, "value": field_value}

    return card_data


def filter_cards(cards, field_id, field_value):
    filtered_cards = []

    for card in cards:
        if card.get(field_id) and field_value in card[field_id]['value']:
            print(card)
            obj = dict(id=card['id'], tomadores_do_emprestimo_id=card.get(field_id))
            filtered_cards.append(obj)

    return filtered_cards


@dataclass
class PipefyDataFacade:
    fi_phase_id: str
    he_phase_id: str
    document_number: str
    fi_data: dict = field(default_factory=dict)
    he_data: dict = field(default_factory=dict)
    normalized_fi_data: list = field(default_factory=list)
    normalized_he_data: list = field(default_factory=list)
    filtered_fi: list = field(default_factory=list)
    filtered_he: list = field(default_factory=list)
    related_cards_he: list = field(default_factory=list)
    related_cards_fi: list = field(default_factory=list)
    related_cards: list = field(default_factory=list)

    def __post_init__(self):
        client = PipefyClient()
        self.fi_data = client.post(get_cards_from_phase, {'phase_id': self.fi_phase_id})
        self.he_data = client.post(get_cards_from_phase, {'phase_id': self.he_phase_id})

    def normalize_data(self):
        self.normalized_fi_data = [normalize_card_data(card) for card in
                                   self.fi_data["data"]["phase"]["cards"]["edges"]]
        self.normalized_he_data = [normalize_card_data(card) for card in
                                   self.he_data["data"]["phase"]["cards"]["edges"]]

    def find_by_doc_number(self):
        self.filtered_fi = filter_cards(self.normalized_fi_data, TOMADORES_DO_EMPRESTIMO_FIELD_ID, self.document_number)
        self.filtered_he = filter_cards(self.normalized_he_data, TOMADORES_DO_EMPRESTIMO_FIELD_ID, self.document_number)

    def trim_data(self):
        self.related_cards_he = [card.get("id") for card in self.filtered_fi]
        self.related_cards_fi = [card.get("id") for card in self.filtered_he]
        self.related_cards = [*self.related_cards_he, *self.related_cards_fi]

    def run(self):
        self.normalize_data()
        self.find_by_doc_number()
        self.trim_data()
        print(self.related_cards_he)
        print(self.related_cards_fi)

# if __name__ == '__main__':
#     he_bacem_phase_id = "319165329"
#     fi_bacem_phase_id = "319165324"
#
#     document_number = "48652804800"
#     facade = PipefyDataFacade(he_phase_id=he_bacem_phase_id, fi_phase_id=fi_bacem_phase_id, document_number=document_number)
#     facade.run()

```

# app.py

```python
import json
import os
from http import HTTPStatus

from common.handlerbase import Handler, Result

from helpers.Models.Payload import Parser
from helpers.Models.s3_helper import S3Helper
from helpers.ReportURLsDAO import ReportURLsDAO
from helpers.Pipefy.search import PipefyDataFacade
from helpers.Pipefy.create import make_variables, send_to_pipefy
from helpers.email_helper.validate_payload import validate_payload

ENV = os.getenv('ENV')


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


def make_files(xlsx_report_url, json_report_url):
    obj = {"xlsx_report_url": xlsx_report_url, "json_report_url": json_report_url}
    print("obj: %s" % obj)
    return obj


class OpenFinanceCreate(Handler):
    def pre_process(self):
        if isinstance(self.event["body"], str):
            self.event["body"] = json.loads(self.event["body"])
        if "query_param" in self.event["body"]:
            del self.event["body"]["query_param"]

    def validate(self) -> Result:
        error = validate_payload(self.event['body'])
        if error:
            return Result(HTTPStatus.BAD_REQUEST, error)

    def handler(self):
        body = self.event["body"]
        if "query_param" in body:
            del body["query_param"]

        data = body.get("data")
        enquiry_cpf = data.get("enquiry_cpf")
        report_type = data.get("report_type").lower()
        report_types = ["category_checking", "income"]
        if report_type in "category_checking":
            bucket_name = "openfinance-dev"
            json_report_url, xlsx_report_url = make_report_urls(enquiry_cpf, report_type)
            print("-----")
            print("-----")
            print("json_report_url, xlsx_report_url", json_report_url, xlsx_report_url)
            s3_helper = S3Helper()
            s3_helper.save_to_s3(json.dumps(body), bucket_name, json_report_url)

            parser = Parser(**body)
            other_report = None
            title = None

            if report_type == "income":
                other_report = "category_checking"
                parser.income_to_excel(xlsx_report_url)
                title = data.get('Income')[0].get("account_holder")
            elif report_type == "category_checking":
                other_report = "income"
                parser.category_checking_to_excel(xlsx_report_url)
                title = data.get("Category_checking")[0].get("holder_name")

            dao = ReportURLsDAO(ENV)
            base_obj = {"enquiry_cpf": enquiry_cpf, "title": title, "report_type": report_type}
            current_report = make_files(xlsx_report_url, json_report_url)
            dao.put_item({**base_obj, **current_report})

            file_counts = s3_helper.count_files_in_s3_bucket(enquiry_cpf, report_types)

            has_both_reports = all(value == 2 for value in file_counts.values())
            new_dict = {**base_obj, f'{report_type}': current_report}
            if has_both_reports:
                other_json_report_url, other_xlsx_report_url = make_report_urls(enquiry_cpf, other_report)
                print("other_json_report_url, other_xlsx_report_url", other_json_report_url, other_xlsx_report_url)
                facade = find_relation(enquiry_cpf)

                variables = make_variables(facade, title, report_type, other_report, other_json_report_url,
                                           json_report_url, enquiry_cpf, xlsx_report_url, other_xlsx_report_url)
                card = send_to_pipefy(variables)
                return Result(HTTPStatus.OK, card)

            return Result(HTTPStatus.OK, new_dict)
        return Result(HTTPStatus.OK, {"report_type": report_type})


def handler(event, context):
    print("Event: %s", event)
    return OpenFinanceCreate(event, context).run()

```

----
