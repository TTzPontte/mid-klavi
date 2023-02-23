import json
import os
import sys

import pytest

sys.path.append(os.path.join("src", "klavi_webhook"))
sys.path.append("/home/silvio/Workspacecs/Pontte/codebase/mid-klavi/src")
sys.path.append("/home/silvio/Workspacecs/Pontte/codebase/mid-klavi/src/klavi_webhook")
sys.path.append("/home/silvio/Workspacecs/Pontte/codebase/mid-klavi/src/klavi_webhook/shared")


from src.klavi_webhook import app
from src.klavi_webhook.shared.parsers.liabilities import parse_liabilities_payload_body


def test_lambda_handler():
    liability_payload = {
                "account_holder": "JOHN DOE",
                "account_number": "01.12345.4",
                "agency_number": "1076",
                "bacen_id": "033",
                "bacen_name": "BANCO SANTANDER (BRASIL) S.A.",
                "bank_name": "Santander",
                "cpf_verified": "01234567890",
                "days_covered": 180,
                "number_of_liability_streams": 1,
                "total_liabilities_last_180_days": 17.25,
                "total_liabilities_last_30_days": 0,
                "total_liabilities_last_60_days": 0,
                "total_liabilities_last_90_days": 0,
                "liabilityStream": [
                    {
                        "liability_stream_type": "Credit card",
                        "liabilityTransactions": [
                            {
                                "trans_date": "2021-11-22",
                                "trans_amount": -17.25,
                                "trans_description": "CARTAO CX"
                            }
                        ]
                    }
                ]
            }
    liability_parsed = parse_liabilities_payload_body(liability_payload)
    assert "account_holder" in liability_parsed


if __name__ == "__main__":
    print("Running Tests...")
    test_lambda_handler()
    print("Finished.")