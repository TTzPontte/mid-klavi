import uuid
from dataclasses import dataclass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import boto3
from botocore.exceptions import ClientError

from shared.helpers.config import Config

config = Config()



@dataclass
class EmailConfig:
    smtp_server: str = config.SMTP_SERVER
    smtp_port: int = config.SMTP_PORT
    login_email: str = config.SMTP_EMAIL
    user_password: str = config.SMTP_PASSWORD
    from_email: str = 'juntos@pontte.com.br'
    from_name: str = "Pontte"
    subject: str = 'error'
    ses_config_set: str = config.CONFIG_SET
    ses_message_tags: str = 'vdm=1'


@dataclass
class EmailService:
    email_config: EmailConfig

    def _build_message(self, html: str, to: str) -> MIMEMultipart:
        print('to email: ', to)
        msg = MIMEMultipart()
        msg['From'] = f"{self.email_config.from_name} <{self.email_config.from_email}>"
        msg['To'] = to
        msg['Subject'] = self.email_config.subject
        msg.attach(MIMEText(html, 'html'))
        msg['X-SES-CONFIGURATION-SET'] = self.email_config.ses_config_set
        msg['X-SES-MESSAGE-TAGS'] = self.email_config.ses_message_tags
        msg['X-SES-MESSAGE-ID'] = str(uuid.uuid4())
        return msg

    def _send_email(self, msg: MIMEMultipart) -> str:
        print("sending email")
        try:
            client = boto3.client('ses', region_name=config.AWS_REGION)
            response = client.send_raw_email(
                Source=self.email_config.from_email,
                Destinations=[msg['To']],
                RawMessage={'Data': msg.as_string()},
                SourceArn=config.SENDING_IDENTITY_ARN
            )
        except ClientError as e:
            return f"Failed to send email. Error message: {e.response['Error']['Message']}"
        return f"Email sent! Message ID: {response['MessageId']}"

    def send_email(self, html: str, to: str) -> str:
        print("sending email")
        msg = self._build_message(html, to)
        return self._send_email(msg)

    def send_emails(self, html: str, emails: list) -> str:
        for email in emails:
            msg = self._build_message(html, email)
            self._send_email(msg)
        return "All emails sent successfully"


# if __name__ == '__main__':
#     email_config = EmailConfig()
#     email_service = EmailService(email_config)
#
#     html = '<p>Hello, World!</p>'
#     recipient = 'jane@example.com'
#     email_service.send_email(html, recipient)
#
#     recipients = ['jane@example.com', 'john@example.com']
#     email_service.send_emails(html, recipients)
