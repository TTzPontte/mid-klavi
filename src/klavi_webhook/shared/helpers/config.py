import logging
import os
from dataclasses import dataclass


@dataclass
class Config():
    AWS_SAM_LOCAL = os.getenv("AWS_SAM_LOCAL") == "true"
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL") or logging.NOTSET

