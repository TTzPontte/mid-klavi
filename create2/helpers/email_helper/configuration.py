import logging
import os
from dataclasses import dataclass

#from dotenv import load_dotenv

#load_dotenv()


@dataclass
class Config:
    AWS_SAM_LOCAL = os.getenv("AWS_SAM_LOCAL") == "true"
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL") or logging.NOTSET
    CONFIG_SET = os.getenv('CONFIG_SET') or 'klavi'
    API_TOKEN = os.getenv('API_TOKEN')
    SMTP_PORT = os.getenv('SMTP_PORT') or 508
    SMTP_EMAIL = os.getenv('SMTP_EMAIL')
    SMTP_SERVER = os.getenv('SMTP_SERVER')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
    SENDING_IDENTITY_ARN = "arn:aws:ses:us-east-1:848638426587:identity/juntos@pontte.com.br"
    AWS_REGION = "us-east-1"
