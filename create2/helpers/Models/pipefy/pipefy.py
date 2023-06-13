from dataclasses import dataclass, field

from graphql.GqlClient import PipefyClient
from graphql.schemas.queries import get_cards_from_phase

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
        if card.get(field_id):
            if field_value in card[field_id]['value']:
                obj = dict(id=card['id'], tomadores_do_emprestimo_id=card.get(field_id))
                filtered_cards.append(obj)

    return filtered_cards


@dataclass
class DataFacade:
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


if __name__ == '__main__':
    he_bacem_phase_id = "312957677"
    fi_bacem_phase_id = "309857079"
    document_number = "48652804800"
    facade = DataFacade(he_phase_id=he_bacem_phase_id, fi_phase_id=fi_bacem_phase_id, document_number=document_number)
    facade.run()