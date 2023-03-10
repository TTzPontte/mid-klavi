import boto3
import smtplib
import uuid
from dataclasses import dataclass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from botocore.exceptions import ClientError


SMTP_PASSWORD='BCCXKD3rmtIJcZfsuf74jvcVYN1wpS4pYIE07YQpjQS5'
SMTP_EMAIL='AKIA4LFWKXXN22C52A4J'
SMTP_SERVER='email-smtp.us-east-1.amazonaws.com'
SENDING_IDENTITY_ARN="arn:aws:ses:us-east-1:848638426587:identity/juntos@pontte.com.br"

AWS_REGION = 'us-east-1'
CONFIG_SET = 'klavi'


@dataclass
class EmailConfig:
    user_password: str = SMTP_PASSWORD
    from_email: str = 'juntos@pontte.com.br'
    from_name: str = "Pontte"
    to_email: str = 'lucas@pontte.com.br'
    smtp_server: str = SMTP_SERVER
    smtp_port: int = 587
    login_email: str = SMTP_EMAIL
    subject: str = 'Klavi Erro Inesperado'

    def _build_message(self, html: str, to: str):
        msg = MIMEMultipart()
        msg['From'] = f"{self.from_name} <{self.from_email}>"
        msg['To'] = to
        msg['Subject'] = self.subject
        msg.attach(MIMEText(html, 'html'))
        msg['X-SES-CONFIGURATION-SET'] = CONFIG_SET
        msg['X-SES-MESSAGE-TAGS'] = 'vdm=1'
        msg['X-SES-MESSAGE-ID'] = str(uuid.uuid4())
        return msg

    def _send_email(self, msg: MIMEMultipart):
        try:
            # Create a new SES resource and specify a region
            client = boto3.client('ses', region_name=AWS_REGION)
            response = client.send_raw_email(
                Source=self.from_email,
                Destinations=[msg['To']],
                RawMessage={'Data': msg.as_string()},
                SourceArn=SENDING_IDENTITY_ARN
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:", response['MessageId'])

    def send_email(self, html: str):
        msg = self._build_message(html, self.from_email)
        self._send_email(msg)

    def send_emails(self, html: str, emails):
        for email in emails:
            msg = self._build_message(html, email)
            self._send_email(msg)