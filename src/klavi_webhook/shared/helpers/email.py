import boto3
from .email.EmailConfig import EmailConfig

def send_simple_mail(subject, content, destination):
    config = EmailConfig(to_email="silvio.junior@pontte.com.br")

    ses_client = boto3.client("ses")
    ses_client.send_email(
        Source="silvio.junior@pontte.com.br",
        Destination={
            "ToAddresses": [destination]
        },
        Message={
             'Subject': {
                 'Data': subject,
                 'Charset': 'UTF-8'
             },
             'Body': {
                 'Text': {
                     'Data': content,
                     'Charset': 'UTF-8'
                 },
                 'Html': {
                     'Data': content,
                     'Charset': 'UTF-8'
                 }
             }
        },
    )