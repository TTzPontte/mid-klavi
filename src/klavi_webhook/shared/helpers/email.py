import boto3

def send_simple_mail(subject, content, destination):
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