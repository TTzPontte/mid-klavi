from dataclasses import dataclass, field
from typing import List, Dict


def normalize_data(data):
    normalized_data = {}
    phase = data['data']['phase']
    normalized_data['phase'] = {
        'id': phase['id'],
        'name': phase['name'],
        'cards_count': phase['cards_count'],
        'cards': []
    }
    for edge in phase['cards']['edges']:
        node = edge['node']
        card = {'id': node['id'], 'fields': {}}
        for field in node['fields']:
            if "array_value" in field:
                value = field['array_value']
                if value.__len__() == 0:
                    value = field['value']
                card['fields'][field['name']] = value
            else:
                card['fields'][field['name']] = field['value']
        normalized_data['phase']['cards'].append(card)
    return normalized_data


def get_tomadores_do_emprestimo(card: Dict[str, any]) -> List[str]:
    tomadores_do_emprestimo_field = card.get("fields", {}).get("tomadores_do_emprestimo", "")
    if isinstance(tomadores_do_emprestimo_field, list):
        tomadores_do_emprestimo = [str(v).strip() for v in tomadores_do_emprestimo_field]
    else:
        tomadores_do_emprestimo = [v.strip() for v in tomadores_do_emprestimo_field.split(",")]
    return tomadores_do_emprestimo



@dataclass
class Facade:
    phase_id: str
    enquiry_cpf: str
    cpf_list: List[Dict[str, List[str]]] = field(default_factory=list)
    cards: List[Dict[str, any]] = field(default_factory=list)
    phase: Dict[str, any] = field(default_factory=dict)

    def get_all_cards_from_phase(self, variables=None) -> None:
        response = input_data
        self.phase = normalize_data(response).get('phase')
        self.cards = self.phase.get("cards", [])

    def find_matching_cards(self) -> None:
        for card in self.phase.get("cards", []):
            if self.enquiry_cpf in get_tomadores_do_emprestimo(card):
                card_id = card.get("id")
                if card_id:
                    for item in self.cpf_list:
                        if self.enquiry_cpf in item:
                            item[self.enquiry_cpf].append(card_id)
                            break
                    else:
                        self.cpf_list.append({self.enquiry_cpf: [card_id]})

    def remove_card_without_tomador(self) -> None:
        self.cards = [card for card in self.cards if self.enquiry_cpf in get_tomadores_do_emprestimo(card)]


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
    print(f"Total cards: {len(facade.cards)}")
    facade.remove_card_without_tomador()
    print(f"Cards with tomador: {len(facade.cards)}")
    facade.find_matching_cards()
    print(f"Matching cards: {facade.cpf_list}")
