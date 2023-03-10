from dataclasses import dataclass, field
from typing import List, Dict


def normalize_card_fields(fields: List[Dict[str, any]]) -> Dict[str, any]:
    normalized_fields = {}
    for field in fields:
        if "array_value" in field:
            value = field['array_value']
            if value.__len__() == 0:
                value = field['value']
            normalized_fields[field['name']] = value
        else:
            normalized_fields[field['name']] = field['value']
    return normalized_fields


@dataclass
class Card:
    id: str
    fields: Dict[str, any] = field(default_factory=dict)

    def get_tomadores_do_emprestimo(self) -> List[str]:
        tomadores_do_emprestimo_field = self.fields.get("tomadores_do_emprestimo", "")
        if isinstance(tomadores_do_emprestimo_field, list):
            tomadores_do_emprestimo = [str(v).strip() for v in tomadores_do_emprestimo_field]
        else:
            tomadores_do_emprestimo = [v.strip() for v in tomadores_do_emprestimo_field.split(",")]
        return tomadores_do_emprestimo


@dataclass
class Phase:
    id: str
    name: str
    cards_count: int
    cards: List[Card] = field(default_factory=list)


def normalize_data(data: Dict[str, any]) -> Phase:
    phase_data = data['data']['phase']
    normalized_cards = []
    for edge in phase_data['cards']['edges']:
        node = edge['node']
        card_fields = normalize_card_fields(node['fields'])
        card = Card(id=node['id'], fields=card_fields)
        normalized_cards.append(card)
    phase = Phase(
        id=phase_data['id'],
        name=phase_data['name'],
        cards_count=phase_data['cards_count'],
        cards=normalized_cards
    )
    return phase


@dataclass
class Facade:
    phase_id: str
    enquiry_cpf: str
    matching_cards: List[Dict[str, List[str]]] = field(default_factory=list)
    phase: Phase = field(default_factory=Phase)

    def get_all_cards_from_phase(self, variables=None) -> None:
        response = input_data
        self.phase = normalize_data(response)
        print(f"Total cards: {len(self.phase.cards)}")

    def find_matching_cards(self) -> None:
        for card in self.phase.cards:
            if self.enquiry_cpf in card.get_tomadores_do_emprestimo():
                card_id = card.id
                if card_id:
                    for item in self.matching_cards:
                        if self.enquiry_cpf in item:
                            item[self.enquiry_cpf].append(card_id)
                            break
                    else:
                        self.matching_cards.append({self.enquiry_cpf: [card_id]})

    def remove_card_without_tomador(self) -> None:
        self.phase.cards = [card for card in self.phase.cards if self.enquiry_cpf in card.get_tomadores_do_emprestimo()]


if __name__ == '__main__':
    input_data = {
        "data": {
            "phase": {
                "id": "312957677",
                "name": "Enviando Bacen",
                "cards_count": 1,
                "cards": {
                    "edges": [
                        {
                            "node": {
                                "id": "472787645",
                                "fields": [
                                    {
                                        "field": {
                                            "id": "tomadores_do_emprestimo",
                                            "index_name": "field_5_connector"
                                        },
                                        "name": "tomadores_do_emprestimo",
                                        "value": "[12345]",
                                        "array_value": [
                                            "472787644"
                                        ]
                                    },
                                    {
                                        "field": {
                                            "id": "ok_para_seguir",
                                            "index_name": "field_63_string"
                                        },
                                        "name": "Ok para seguir?",
                                        "value": "Sim",
                                        "array_value": []
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        }
    }

    phase_id = "312957677"  # Replace with the actual Pipefy phase ID
    enquiry_cpf = "12345"  # Replace with the actual CPF number to search for
    facade = Facade(phase_id=phase_id, enquiry_cpf=enquiry_cpf)
    facade.get_all_cards_from_phase(variables={"phase_id": phase_id})
    print(f"Total cards: {len(facade.phase.cards)}")
    facade.remove_card_without_tomador()
    print(f"Cards with tomador: {len(facade.phase.cards)}")
    facade.find_matching_cards()
    print(f"Matching cards: {facade.matching_cards}")
