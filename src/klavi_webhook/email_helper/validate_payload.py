import json
from http import HTTPStatus
from typing import Dict, Optional

from email_helper.EmailService import EmailService, EmailConfig


def build_html(enquiry_cpf: str, error_message: str, code: int, suggested_action: str, payload: Dict) -> str:
    """
    Builds an HTML table with the given error information and payload.
    """
    table_style = "border-collapse: collapse; width: 100%;"
    th_style = "text-align: left; padding: 8px; background-color: #dddddd;"
    td_style = "text-align: left; padding: 8px; border: 1px solid #dddddd;"
    table_html = f"<table style='{table_style}'><tr style='background-color: #f2f2f2;'><th style='{th_style}'>Enquiry CPF</th>" \
                 f"<td style='{td_style}'>{enquiry_cpf}</td></tr>" \
                 f"<tr><th style='{th_style}'>Code</th><td style='{td_style}'>{code}</td></tr>" \
                 f"<tr><th style='{th_style}'>Message</th><td style='{td_style}'>{error_message}</td></tr>" \
                 f"<tr><th style='{th_style}'>Suggested Action</th><td style='{td_style}'>{suggested_action}</td></tr>" \
                 f"<tr><th style='{th_style}'>Raw Payload</th><td style='{td_style}'>{json.dumps(payload, indent=2)}</td></tr></table>"
    return table_html


def validate_payload(payload: Dict) -> Optional[Dict]:
    """Validates the payload and returns an error dictionary if there is an error.
    Returns None if the payload is valid."""
    if not payload:
        return {"message": "Invalid request body"}

    try:
        status_code = payload.get("code")
        if status_code is None:
            return {"message": "Invalid request payload: code is missing."}
        if not (200 <= int(status_code) <= 299):
            raise ValueError(f"Invalid status code: {status_code}")

    except ValueError as e:
        error_message = str(e)
        message = payload.get("msg")

        error_dict = {"code": HTTPStatus.BAD_REQUEST, "message": message,
            "suggested_action": "Please fix the request payload and try again."}

        # Send email
        enquiry_cpf = payload.get('data', {}).get('enquiry_cpf')
        if enquiry_cpf:
            html = build_html(enquiry_cpf, error_message, HTTPStatus.BAD_REQUEST, error_dict["suggested_action"],
                              payload)
            to = "lucas@pontte.com.br"
            email_service = EmailService(EmailConfig())
            sent_email = email_service.send_email(html, to)
            print(sent_email)

        return error_dict

    # Return None if the payload is valid
    return None
