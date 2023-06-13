import json
from http import HTTPStatus
from typing import Dict, Optional

from .email_service import EmailService, EmailConfig


def retorno_codigo(code):
    code_dict = {200: ("", ""), 201: ("Autorização extra necessária", ""), 202: ("Falta uma transação parcial", ""),
                 400: ("A assinatura falhou", ""), 401: ("[Apenas em modo GET] Usuário não existe na nossa base", ""),
                 402: (
                     "Quando o usuário tenta conectar a conta bancária com dados de login errados (ex: senha digitada errada)",
                     "Instruir a inserção correta da senha ou MFA"),
                 403: ("O banco está fora do ar", "Pedir para o usuário conectar novamente mais tarde"),
                 404: ("Erro inesperado", "Abrir um ticket com time da Klavi"),
                 405: ("A conexão foi feita com sucesso mas a conta não tem dados", ""), 406: (
            "Nosso sistema não permite que usuários tentem acessar a conta com asenha errada muitas vezes, para evitar bloqueio pelo banco. Recomendamos tentar novamente no próximo dia",
            "Pedir para o usuário conectar após 1 dia (24h)"), 407: (
            "Conta inativa, senha inativa, senha temporária ou senha vencida",
            "Pedir para o usuário resolver a sua pendência diante do Banco"), 408: (
            "A conta ou senha está bloqueada", "Pedir para o usuário renovar a sua senha de internet banking"), 409: (
            "O usuário usou credenciais de um tipo de conta errado (ex, usou login de PJ em ambiente de PF)",
            "Pedir para o usuário conectar uma conta compatível a conexão"),
                 410: ("O formato credencial de Entrada do utilizador está incorrecto Ou EM Falta", ""),
                 411: ("TraceId da tarefa é nulo ou não foi encontrado", ""), 412: ("Token não é necessário", ""),
                 413: (
                     "Ops! Verificamos que uma sessão está ativa. Faça logout do seu internet banking e tente novamente",
                     "Pedir para o usuário encerrar as atuais sessões ativas")}

    descricao, instrucao = code_dict.get(code,
                                         ("Código de retorno desconhecido", "Verificar documentação e buscar suporte"))

    return descricao, instrucao


def build_html(enquiry_cpf: str, error_message: str, code: int, suggested_action: str, payload: Dict) -> str:
    """
    Builds an HTML table with the given error information and payload.
    """
    with open("template.html", "r") as f:
        template = f.read()
    table_html = template.replace("{{ enquiry_cpf }}", enquiry_cpf) \
        .replace("{{ code }}", str(code)) \
        .replace("{{ error_message }}", error_message) \
        .replace("{{ suggested_action }}", suggested_action) \
        .replace("{{ payload }}", json.dumps(payload, indent=2))
    return table_html


def validate_payload(payload: Dict) -> Optional[Dict]:
    def create_error_dict(status_code: int, error_message: str) -> Dict:
        descricao, instrucao = retorno_codigo(status_code)
        return {
            "code": status_code,
            "message": error_message,
            "suggested_action": instrucao
        }

    def send_email_if_needed(error_dict: Dict, payload: Dict) -> None:
        enquiry_cpf = payload.get('data', {}).get('enquiry_cpf')
        if enquiry_cpf:
            html = build_html(
                enquiry_cpf,
                error_dict["message"],
                error_dict["code"],
                error_dict["suggested_action"],
                payload
            )
            # Send email with the generated HTML error report
            to = ["lucas@pontte.com.br", "pietra.oliveira@pontte.com.br"]
            for to_email in to:
                email_service = EmailService(EmailConfig())
                sent_email = email_service.send_email(html, to_email)
                print(sent_email)

    if not payload:
        error_dict = create_error_dict(HTTPStatus.BAD_REQUEST, "Invalid request body")
        send_email_if_needed(error_dict, payload)
        return error_dict

    try:
        status_code = payload.get("code")
        if status_code is None:
            error_dict = create_error_dict(HTTPStatus.BAD_REQUEST, "Invalid request payload: code is missing.")
            send_email_if_needed(error_dict, payload)
            return error_dict

        if not (200 <= int(status_code) <= 299):
            error_dict = create_error_dict(status_code, "Invalid status code")
            send_email_if_needed(error_dict, payload)
            return error_dict

    except ValueError as e:
        error_dict = create_error_dict(HTTPStatus.BAD_REQUEST, str(e))
        send_email_if_needed(error_dict, payload)
        return error_dict


if __name__ == '__main__':
    event = {
        "body": "{\n  \"msg\": \"User credential error\",\n  \"code\": 402,\n  \"data\": {\n    \"user_consent\": \"Yes\",\n    \"allow_autoupdate\": \"No\",\n    \"connection_key\": \"gPuKXrCJU0kUDQO65J4k\",\n    \"connection_id\": \"f45c899f-11eb-231f-97c4-4b2c16484587\",\n    \"report_id\": \"4b2c1648-231f-11eb-97c4-f45c899f4587\",\n    \"Category_checking\": null,\n    \"enquiry_cpf\": \"70079872140\",\n    \"report_type\": \"category_checking\",\n    \"institution_id\": \"341\",\n    \"report_version\": \"V1\"\n  },\n  \"report_time\": \"2023-03-23 13:53:45\",\n  \"query_param\": {}\n}",
    }
    raw_body = event.get("body")
    body = json.loads(raw_body)
    validate_payload(body)
