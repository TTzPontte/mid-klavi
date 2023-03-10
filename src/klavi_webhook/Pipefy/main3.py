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


from dataclasses import dataclass
from typing import Dict, List


@dataclass
class DataFacade:
    data: Dict[str, any]

    def get_normalized_data(self) -> 'Phase':
        phase_data = self.data['data']['phase']
        normalized_cards = [Card(node['id'], phase_data['id'],
                                 {field['name']: self._extract_value(field['value'], field.get('array_value', [])) for
                                  field in node['fields']}) for edge in phase_data['cards']['edges'] for node in
                            [edge['node']]]
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
            if cpf in tomadores_do_emprestimo:
                return card
        return None

    def _extract_value(self, value: str, array_value: List[str]) -> any:
        if array_value:
            return [v.strip() for v in array_value if v.strip()]
        if value.startswith("[") and value.endswith("]"):
            return [v.strip() for v in value[1:-1].split(",") if v.strip()]
        return value.strip('"')


def main(input_data):
    data_facade = DataFacade(input_data)

    normalized_data = data_facade.get_normalized_data()
    print("normalized_data", normalized_data)

    fields = normalized_data.cards[0].fields
    print("fields", fields)

    tomadores = data_facade.get_tomadores_do_emprestimo(normalized_data.cards[0])
    print("tomadores", tomadores)

    related_card = data_facade.find_related_card_by_cpf('12345')
    print("related_card", related_card)


if __name__ == '__main__':
    input_data = {"data": {"phase": {"id": "312957677", "name": "Enviando Bacen", "cards_count": 1, "cards": {"edges": [
        {"node": {"id": "472787645", "fields": [
            {"field": {"id": "tomadores_do_emprestimo", "index_name": "field_5_connector"},
             "name": "tomadores_do_emprestimo", "value": "[\"12345\"]", "array_value": ["12345"]},
            {"field": {"id": "ok_para_seguir", "index_name": "field_63_string"}, "name": "Ok para seguir?",
             "value": "Sim", "array_value": []}]}}]}}}}
    main(input_data)
