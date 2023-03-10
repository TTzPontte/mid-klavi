from dataclasses import dataclass, field

import requests

from src.klavi_webhook.Pipefy.secrets import API_KEY


@dataclass
class PipefyClient:
    api_key: str = API_KEY
    base_url: str = "https://api.pipefy.com/graphql"
    headers: dict = field(default_factory=dict)

    def __post_init__(self):
        self.headers = {"authorization": f"Bearer {self.api_key}", "content-type": "application/json"}

    def post(self, query: str, variables: dict) -> dict:
        payload = {"query": query, "variables": variables}

        response = requests.post(self.base_url, json=payload, headers=self.headers)
        return response.json()
