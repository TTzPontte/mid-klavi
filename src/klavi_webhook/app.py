import json
from src.event_logger.parser import parse_payload_into_logger_object
from src.event_logger.logger import Logger, LoggerSchema

# import requests


def lambda_handler(event, context):
    body = event.get('body')
    payload = json.loads(body) if isinstance(body, str) else body
    logger = parse_payload_into_logger_object(payload)
    print(event)
    print(body)
    print(logger)
    print("_______")
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world updated",
            "payload": logger
            # "location": ip.text.replace("\n", "")
        }),
    }


if __name__ == "__main__":
    payload = {
        "report_time": "nothing",
        "data": {
            "connection_id": "nothing",
            "connection_key": "nothing",
            "institution_id": "nothing",
            "enquire_cpf": "nothing"
        }
    }
    print("***")
    logger = parse_payload_into_logger_object(payload)
    logger_obj = Logger(**logger)
    schema = LoggerSchema()
    parsed = schema.dumps(logger_obj)
    print(logger_obj)
    print("+___")
    print(parsed)
    print("*********")


const entity = {id: '', 'name': ''}
const mother = {id: '', 'name': '', user_id: ''}
const friend = {id: 11, 'name': '', user_id: ''}
const friend_errado = {id: '', fist_name: ''}

user {
    id: '',
    friends: [
        {
            'id': '',
            'name: '''
        },
        entity
    ],
    mother: entity
}

mother