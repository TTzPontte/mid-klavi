from typing import Dict, List


def normalize_data(data):
    normalized_data = {}
    phase = data['data']['phase']
    normalized_data['phase'] = {}
    normalized_data['phase']['id'] = phase['id']
    normalized_data['phase']['name'] = phase['name']
    normalized_data['phase']['cards_count'] = phase['cards_count']
    normalized_data['phase']['cards'] = []
    for edge in phase['cards']['edges']:
        node = edge['node']
        card = {}
        card['id'] = node['id']
        card['fields'] = {}
        for field in node['fields']:
            if "array_value" in field:
                card['fields'][field['name']] = field['array_value']
            else:
                card['fields'][field['name']] = field['value']
        normalized_data['phase']['cards'].append(card)
    return normalized_data


def get_tomadores_do_emprestimo(card: Dict[str, any]) -> List[str]:
    fields = card.get("fields", {})
    tomadores_do_emprestimo_field = fields.get("tomadores_do_emprestimo", "")
    if isinstance(tomadores_do_emprestimo_field, list):
        tomadores_do_emprestimo = [str(v).strip() for v in tomadores_do_emprestimo_field]
    else:
        tomadores_do_emprestimo = [v.strip() for v in tomadores_do_emprestimo_field.split(",")]
    return tomadores_do_emprestimo


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
                                        "value": "[\"12345\"]"
                                    },
                                    {
                                        "field": {
                                            "id": "ok_para_seguir",
                                            "index_name": "field_63_string"
                                        },
                                        "name": "Ok para seguir?",
                                        "value": "Sim"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        }
    }

    normalized_data = normalize_data(input_data)
    print("normalized_data", normalized_data)

    cards = normalized_data.get("phase", {}).get("cards", [])
    print("cards", cards)

    for card in cards:
        tomadores = get_tomadores_do_emprestimo(card)
        print("tomadores", tomadores)
