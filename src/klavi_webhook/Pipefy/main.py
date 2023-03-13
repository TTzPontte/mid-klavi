from dataclasses import dataclass, field
from typing import Dict, List

from shared.helpers.graphql.GqlClient import PipefyClient
from shared.helpers.graphql.schemas.queries import get_cards_from_phase


@dataclass
class Card:
    id: str
    phase_id: str
    fields: Dict[str, any] = None


@dataclass
class Phase:
    id: str
    name: str
    cards_count: int
    cards: List[Card] = None


@dataclass
class DataFacade:
    phase_id: str
    data: dict = field(default_factory=dict)

    def __post_init__(self):
        client = PipefyClient()
        self.data = client.post(get_cards_from_phase, {'phase_id': self.phase_id})

    def get_normalized_data(self) -> 'Phase':
        phase_data = self.data['data']['phase']
        normalized_cards = []
        for edge in phase_data['cards']['edges']:
            node = edge['node']
            card_fields = {}
            for field in node['fields']:
                if 'value' in field:
                    card_fields[field['name']] = self._extract_value(field['value'])
            normalized_cards.append(Card(node['id'], phase_data['id'], card_fields))
        phase = Phase(phase_data['id'], phase_data['name'], phase_data['cards_count'], normalized_cards)
        return phase

    def get_tomadores_do_emprestimo(self, card: 'Card') -> List[str]:
        tomadores_do_emprestimo_field = card.fields.get("tomadores_do_emprestimo", "")
        tomadores_do_emprestimo = []
        if isinstance(tomadores_do_emprestimo_field, list):
            tomadores_do_emprestimo.extend([v for v in tomadores_do_emprestimo_field if v])
        else:
            tomadores_do_emprestimo = [v for v in tomadores_do_emprestimo_field.split(",") if v.strip()]
        return tomadores_do_emprestimo

    def find_related_card_by_cpf(self, cpf: str) -> 'Card':
        phase = self.get_normalized_data()
        for card in phase.cards:
            tomadores_do_emprestimo = self.get_tomadores_do_emprestimo(card)
            tomadores_do_emprestimo = [t.strip('"') for t in tomadores_do_emprestimo]  # remove quotation marks
            if cpf in tomadores_do_emprestimo:
                return card
        return None

    def _extract_value(self, value: str) -> any:
        if value.startswith("[") and value.endswith("]"):
            return [v.strip() for v in value[1:-1].split(",") if v.strip()]
        return value.strip('"')


def main(input_data, enquiry_cpf):
    data_facade = DataFacade(input_data)

    normalized_data = data_facade.get_normalized_data()
    print("normalized_data", normalized_data)

    if (len(normalized_data.cards) == 0):
        return None

    fields = normalized_data.cards[0].fields
    print("fields", fields)

    tomadores = data_facade.get_tomadores_do_emprestimo(normalized_data.cards[0])
    print("tomadores", tomadores)

    related_card = data_facade.find_related_card_by_cpf(enquiry_cpf)
    print("related_card", related_card)
    return related_card


if __name__ == '__main__':
    main("312957677", "12345")
