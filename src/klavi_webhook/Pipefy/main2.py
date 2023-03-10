import requests
from dataclasses import dataclass, field
from typing import Dict, Optional

from src.klavi_webhook.Pipefy.graphql.GqlClient import PipefyClient
from src.klavi_webhook.Pipefy.graphql.GqlClient__2 import GqlClient
from src.klavi_webhook.Pipefy.graphql.schemas.queries import get_cards_from_phase
from src.klavi_webhook.Pipefy.secrets import API_KEY
# from src.klavi_webhook.shared.helpers.pipefy.client import PipefyClient


@dataclass
class PipefyFacade:
    api_key: str
    result: dict = field(default_factory=dict)
    endpoint: str = "https://api.pipefy.com/graphql"

    def __post_init__(self):
        # client = GqlClient(api_key=self.api_key, url=self.endpoint)
        # self.result = client.post(get_cards_from_phase, {'phase_id': 312957677})
        client = PipefyClient()
        self.result = client.post(get_cards_from_phase,  {'phase_id': 312957677})

if __name__ == '__main__':
    x = PipefyFacade(api_key=API_KEY)
    print(x.result)