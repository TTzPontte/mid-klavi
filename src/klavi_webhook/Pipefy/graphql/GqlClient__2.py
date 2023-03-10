import json
from dataclasses import dataclass
from typing import Dict

import requests


@dataclass
class GqlClient:
    url: str
    api_key: str

    def __post_init__(self):
        self.headers = {"Accept": "application/json", "Content-Type": "application/json",
                        'authorization': f"Bearer {self.api_key}"}

    def post(self, query: str, variables: Dict = {}) -> requests.Response:
        payload = {'query': query, 'variables': json.dumps(variables)}
        response = requests.post(self.url, json=payload, headers=self.headers)

        # response.raise_for_status()
        return response.json()


class PipefyClientFacade:
    def __init__(self, api_key: str):
        self.client = GqlClient(url="https://api.pipefy.com/graphql", api_key=api_key)

    def get_cards_from_phase(self, phase_id: str) -> Dict:
        query = """
            query GetCardsFromPhase($phase_id: ID!) {
                phase(id: $phase_id) {
                    id
                    name
                    cards_count
                    cards {
                        edges {
                            node {
                                fields {
                                    field {
                                        id
                                        index_name
                                    }
                                    name
                                    value
                                }
                            }
                        }
                    }
                }
            }
        """

        variables = {"phase_id": phase_id}


if __name__ == '__main__':
    PipefyClientFacade()
