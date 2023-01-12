"""Configurações
"""

import logging
import os

LOGGING_LEVEL = os.getenv("LOGGING_LEVEL") or logging.NOTSET

AWS_SAM_LOCAL = os.getenv("AWS_SAM_LOCAL") == "true"

API_ENDPOINT = os.getenv("API_ENDPOINT")

DYNAMODB_ENDPOINT = os.getenv("DYNAMODB_ENDPOINT")

ENV = os.getenv("ENV") or "prod"

ES_ENDPOINT = os.getenv("ES_ENDPOINT")

MANDRILL_API_KEY = os.getenv("MANDRILL_API_KEY")