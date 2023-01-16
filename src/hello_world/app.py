from http import HTTPStatus

from helpers.handler_base import Handler, Result
from helpers.hw_helper import helper_fn


class HelloWorld(Handler):

    def handler(self):
        # return {
        #     "statusCode": 200,
        #     "body": json.dumps({
        #         "message": "hello world",
        #         # "location": ip.text.replace("\n", "")
        #     }),
        # }
        return Result(HTTPStatus.OK, {"message": "hello world"})


def lambda_handler(event, context):
    helper_fn()
    return HelloWorld(event, context).run()
