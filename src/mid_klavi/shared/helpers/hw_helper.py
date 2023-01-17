import logging
import os

LOGGING_LEVEL = os.getenv("LOGGING_LEVEL") or logging.NOTSET

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name
logger.setLevel(LOGGING_LEVEL)


def helper_fn():
    logger.debug("-----------------")
    logger.debug(" helper run ok")
    logger.debug("-----------------")
