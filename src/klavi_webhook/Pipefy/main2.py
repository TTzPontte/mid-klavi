from dataclasses import dataclass, field

import requests

from src.klavi_webhook.Pipefy.graphql.GqlClient import PipefyClient
from src.klavi_webhook.Pipefy.graphql.schemas.queries import get_cards_from_phase
from src.klavi_webhook.Pipefy.secrets import API_KEY




@dataclass
class PipefyFacade:
    api_key: str
    result: dict = field(default_factory=dict)
    endpoint: str = "https://api.pipefy.com/graphql"
    all_cards_from_phase
    cards_without_tomador
    find_matching_cards
    def __post_init__(self):
        # client = GqlClient(api_key=self.api_key, url=self.endpoint)
        # self.result = client.post(get_cards_from_phase, {'phase_id': 312957677})
        client = PipefyClient()
        self.result = client.post(get_cards_from_phase, {'phase_id': 312957677})


if __name__ == '__main__':
    x = PipefyFacade(api_key=API_KEY)
    print(x.result)
