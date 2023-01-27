from http import HTTPStatus
from shared.helpers.handler_base import Handler, Result
from shared.helpers.hw_helper import helper_fn
from shared.repository.klavi_report import KlaviReportRepository
import json


class MidKlavi(Handler):
    body: str

    def pre_process(self):
        if self.event['body']:
            self.body = json.loads(self.event['body'])

    def handler(self):
        #report = build_klavi_report(self.body)
        report_repository = KlaviReportRepository()
        #report_repository.save(report)
        report_repository.getByReportId({'id': 'report_id', 'enquiry_cpf': '12345678901'})
        print("FIM")

        # 1 - Identificar Relatorio
        # 2 - Parsiar o Relatorio
        # 3 - Salvar no Banco
        # 4 - Recuperar do Banco
        # 5 - Gerar Modelo XLSX
        # 6 - Fazer Upload no S3
        # 7 - Adicionar URL do S3 no Card do Pipefy

        return Result(HTTPStatus.OK, {"message": "hello world Novo"})


def lambda_handler(event, context):
    helper_fn()
    return MidKlavi(event, context).run()
