def retorno_codigo(code):
    code_dict = {200: ("", ""), 201: ("Autorização extra necessária", ""), 202: ("Falta uma transação parcial", ""),
        400: ("A assinatura falhou", ""), 401: ("[Apenas em modo GET] Usuário não existe na nossa base", ""), 402: (
        "Quando o usuário tenta conectar a conta bancária com dados de login errados (ex: senha digitada errada)",
        "Instruir a inserção correta da senha ou MFA"),
        403: ("O banco está fora do ar", "Pedir para o usuário conectar novamente mais tarde"),
        404: ("Erro inesperado", "Abrir um ticket com time da Klavi"),
        405: ("A conexão foi feita com sucesso mas a conta não tem dados", ""), 406: (
            "Nosso sistema não permite que usuários tentem acessar a conta com asenha errada muitas vezes, para evitar bloqueio pelo banco. Recomendamos tentar novamente no próximo dia",
            "Pedir para o usuário conectar após 1 dia (24h)"), 407: (
        "Conta inativa, senha inativa, senha temporária ou senha vencida",
        "Pedir para o usuário resolver a sua pendência diante do Banco"),
        408: ("A conta ou senha está bloqueada", "Pedir para o usuário renovar a sua senha de internet banking"), 409: (
        "O usuário usou credenciais de um tipo de conta errado (ex, usou login de PJ em ambiente de PF)",
        "Pedir para o usuário conectar uma conta compatível a conexão"),
        410: ("O formato credencial de Entrada do utilizador está incorrecto Ou EM Falta", ""),
        411: ("TraceId da tarefa é nulo ou não foi encontrado", ""), 412: ("Token não é necessário", ""), 413: (
        "Ops! Verificamos que uma sessão está ativa. Faça logout do seu internet banking e tente novamente",
        "Pedir para o usuário encerrar as atuais sessões ativas")}

    descricao, instrucao = code_dict.get(code,
                                         ("Código de retorno desconhecido", "Verificar documentação e buscar suporte"))

    return descricao, instrucao
