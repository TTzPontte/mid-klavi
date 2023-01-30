from http import HTTPStatus
from shared.helpers.handler_base import Handler, Result
from shared.helpers.hw_helper import helper_fn
from shared.repository.klavi_report import KlaviReportRepository
from shared.factory.klavi_report import build_report_from_klavi_payload
from shared.exports.klavi_report import export_klavi_report_to_excel
import json
import io


class MidKlavi(Handler):
    body: str

    def pre_process(self):
        if self.event['body']:
            self.body = json.loads(self.event['body'])

    def handler(self):
        report = build_report_from_klavi_payload(self.body)
        report_repository = KlaviReportRepository()
        print("Report to be Saved is")
        print(report)
        report_repository.save(report)
        report_from_database = report_repository.getByReportId(str(report.id), report.enquiry_cpf)
        print("Report from Database is")
        print(report_from_database)
        excel_file_buffer = io.BytesIO()
        excel_file = export_klavi_report_to_excel(report_from_database, '/home/silvio/temp/excel_test.xlsx')
        excel_file_buffer.close()
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
