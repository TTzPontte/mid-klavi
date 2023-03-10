import requests

from dataclasses import dataclass

from src.klavi_webhook.Pipefy.secrets import API_KEY
from .mutations import create_table_record_mutation


@dataclass
class PipefyClient:
    API_KEY: str = API_KEY
    def post(self, query, variables):

        url = "https://api.pipefy.com/graphql"
        headers = {
            'authorization': f"Bearer {API_KEY}",
            'content-type': "application/json"
        }

        return requests.request("POST", url, json={"query": query, "variables": variables}, headers=headers)


if __name__ == "__main__":
    pipefy_client = PipefyClient()
    document_test = [
        {
            "field_id": "klavi_excel",
            "field_value": "klavi_xls_from_klavi_script_test"
        },
        {
            "field_id": "klavi_json",
            "field_value": "klavi_json_from_klavi_script_test"
        }
    ]
    pipefy_client.insert_into_database(document_test, "303051866")