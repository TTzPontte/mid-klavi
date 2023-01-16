import json
import os
import sys

import pytest

sys.path.append(os.path.join("src", "hello_world"))
from src.hello_world import app
from tests.utils.apigw_event import apigw_event


@pytest.fixture()
def event():
    return apigw_event()


def test_lambda_handler(event):
    ret = app.lambda_handler(event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "hello world"
