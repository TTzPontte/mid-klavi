from dataclasses import dataclass, field

import requests

API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozMDEyNjA0NzYsImVtYWlsIjoiZGV2QHBvbnR0ZS5jb20uYnIiLCJhcHBsaWNhdGlvbiI6MzAwMjEyMzk2fX0.iGh6T7W-nvhk-wA3JwH24HUAUHoGBxAVn_vfnx_nmy7XMGrK9_PZpfc9UBv4oU0B29756zGshKqyWRc921zJZg"


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
