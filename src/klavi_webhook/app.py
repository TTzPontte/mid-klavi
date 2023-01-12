import json
from event_logger.parser import parse_payload_into_logger_object
from event_logger.logger import Logger

# import requests

import os

os.environ['AWS_SERVER_PUBLIC_KEY'] = "AKIA4LFWKXXNQYMOWWSB"
os.environ['AWS_SERVER_SECRET_KEY'] = "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"
os.environ['AWS_DEFAULT_REGION'] = "us-east-1"

def lambda_handler(event, context):
    body = event.get('body')
    payload = json.loads(body) if isinstance(body, str) else body
    print(payload)
    print("Leru Leru")
    logger = parse_payload_into_logger_object(payload)
    print(logger)
  #  print(event)
  #  print(body)
  #  print(logger)
  #  print("_______")
    logger_obj = Logger(**logger)
    logger_obj.save()
  #  print("+___")
    print("*********")
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
           # "payload": logger
            # "location": ip.text.replace("\n", "")
        }),
    }

