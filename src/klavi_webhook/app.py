import json
from pprint import PrettyPrinter

from src.klavi_webhook.common.Parser.main import Parser

pp = PrettyPrinter(indent=4)
ppp = pp.pprint


def read_json(file_path: str):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def lambda_handler(event, context):
    ppp(data)
    p = Parser(**data)
    # p = Test(**data)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": p
            # "location": ip.text.replace("\n", "")
        }),
    }

# file_path = '/Users/Mr-i-me/PycharmProjects/klavi/app/events/liabilities.json'
#    data = read_json(file_path)
#    xx = handler(data)
