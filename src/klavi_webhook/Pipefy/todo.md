Main goal is to find all the cards in the phase `Analise Bacem` that has the field `tomadores_do_emprestimo` and the
field `tomadores_do_emprestimo`  contains the `enquiry_cpf_cnpj`
considering the pipefy api write the step by step to acomplish our main goal

# todo:

1. get phase field id
2. get all card from phase
3. instanciate new cpf_list = []
4. get the tomadores_do_emprestimo FIeld from every card
5. iterate through cards
6. iterate through tomadores_do_emprestimo for each card
7. if tomadores_do_emprestimo is same as enquiry_cpf add card id to cpf_list = [{'554.325.420-21': [472733907]}]

refactor the code below using DRY, clean code, PEP8, and the Facade design pattern.

```python

from dataclasses import dataclass
from typing import Dict, List


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


def normalize_data(data: Dict[str, any]) -> Phase:
    phase_data = data['data']['phase']
    normalized_cards = [Card(node['id'], phase_data['id'],
                             {field['name']: extract_value(field['value'], field.get('array_value', [])) for field in
                              node['fields']}) for edge in phase_data['cards']['edges'] for node in [edge['node']]]
    phase = Phase(phase_data['id'], phase_data['name'], phase_data['cards_count'], normalized_cards)
    return phase


def extract_value(value: str, array_value: List[str]) -> any:
    if array_value:
        return [v.strip() for v in array_value if v.strip()]
    if value.startswith("[") and value.endswith("]"):
        return [v.strip() for v in value[1:-1].split(",") if v.strip()]
    return value.strip('"')


def get_tomadores_do_emprestimo(card: Card) -> List[str]:
    tomadores_do_emprestimo_field = card.fields.get("tomadores_do_emprestimo", "")
    tomadores_do_emprestimo = []
    if isinstance(tomadores_do_emprestimo_field, list):
        tomadores_do_emprestimo.extend([v for v in tomadores_do_emprestimo_field if v])
    else:
        tomadores_do_emprestimo = [v for v in tomadores_do_emprestimo_field.split(",") if v.strip()]
    return tomadores_do_emprestimo


def find_related_card_by_cpf(phase: Phase, cpf: str) -> Card:
    for card in phase.cards:
        tomadores_do_emprestimo = get_tomadores_do_emprestimo(card)
        if cpf in tomadores_do_emprestimo:
            return card
    return None


def main(input_data):
    normalized_data = normalize_data(input_data)
    print("normalized_data", normalized_data)

    fields = normalized_data.cards[0].fields
    print("fields", fields)

    tomadores = get_tomadores_do_emprestimo(normalized_data.cards[0])
    print("tomadores", tomadores)
    related_card = find_related_card_by_cpf(normalized_data, '12345')
    print("related_card", related_card)


if __name__ == '__main__':
    input_data = {"data": {"phase": {"id": "312957677", "name": "Enviando Bacen", "cards_count": 1, "cards": {"edges": [
        {"node": {"id": "472787645", "fields": [
            {"field": {"id": "tomadores_do_emprestimo", "index_name": "field_5_connector"},
             "name": "tomadores_do_emprestimo", "value": "[\"12345\"]", "array_value": ["12345"]},
            {"field": {"id": "ok_para_seguir", "index_name": "field_63_string"}, "name": "Ok para seguir?",
             "value": "Sim", "array_value": []}]}}]}}}}
    main(input_data)

```




the code bellow is my current implementation of a Facade that gets a Phase json from pipefy and finds relations by their tomadores cpf information.

