import requests

from dataclasses import dataclass
from .mutations import create_table_record_mutation

API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozMDEyNjA0NzYsImVtYWlsIjoiZGV2QHBvbnR0ZS5jb20uYnIiLCJhcHBsaWNhdGlvbiI6MzAwMjEyMzk2fX0.iGh6T7W-nvhk-wA3JwH24HUAUHoGBxAVn_vfnx_nmy7XMGrK9_PZpfc9UBv4oU0B29756zGshKqyWRc921zJZg"

@dataclass
class PipefyClient:

    def insert_into_database(self, document, database_id):
        mutation_variables = {
            "table_id": database_id,
            "title": "test-silvio",
            "values": document
        }
        url = "https://api.pipefy.com/graphql"
        headers = {
            'authorization': f"Bearer {API_TOKEN}",
            'content-type': "application/json"
        }

        print("My Variales")
        print(mutation_variables)
        print("__OPA___")

        response = requests.request("POST", url, json={"query": create_table_record_mutation, "variables": mutation_variables}, headers=headers)
        print(response.text)


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