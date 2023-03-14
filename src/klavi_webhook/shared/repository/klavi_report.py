import os
from dataclasses import dataclass
from typing import List
from uuid import UUID

from shared.data_access_objects.klavi_report import KlaviReportDAO
from shared.models.klavi_report import KlaviReportSchema, KlaviReport
from shared.repository.category_checking import CategoryCheckingRepository
from shared.repository.income import IncomeRepository


@dataclass
class KlaviReportRepository:
    klavi_report_dao: KlaviReportDAO = KlaviReportDAO()
    category_checking_repository: CategoryCheckingRepository = CategoryCheckingRepository()
    income_repository: IncomeRepository = IncomeRepository()

    def save(self, klavi_report: KlaviReport):
        klavi_report_schema = KlaviReportSchema()
        klavi_report_document = klavi_report_schema.dump(klavi_report)

        bucket_name = "klavi-{env}".format(env=os.getenv("ENV"))
        object_key = "{report_id}/{report_type}.xlsx".format(report_id=klavi_report_document["report_id"],
                                                             report_type=klavi_report_document["report_type"])
        object_url = "https://{bucket_name}.s3.amazonaws.com/{object_key}".format(bucket_name=bucket_name,
                                                                                  object_key=object_key)

        klavi_report_document["json_object"] = {
            "bucket_name": bucket_name,
            "object_key": object_key,
            "object_url": object_url
        }

        category_checkings_ids = [str(category_checking.id) for category_checking in klavi_report.category_checkings]
        klavi_report_document['category_checkings'] = category_checkings_ids

        income_ids = [str(income.id) for income in klavi_report.income]
        klavi_report_document['income'] = income_ids

        self.klavi_report_dao.put(klavi_report_document)

        if klavi_report.report_type == "category_checking":
            for category_checking in klavi_report.category_checkings:
                category_checking.report_id = klavi_report.id
                self.category_checking_repository.save(category_checking)

        if klavi_report.report_type == "income":
            for income in klavi_report.income:
                income.report_id = klavi_report.id
                self.income_repository.save(income)

    def getByReportId(self, report_id: UUID, enquiry_cpf: str) -> KlaviReport:
        report = self.klavi_report_dao.get({'id': report_id, 'enquiry_cpf': enquiry_cpf})

        klavi_report = KlaviReport(**report)
        klavi_report.category_checkings = []
        klavi_report.income = []

        if klavi_report.report_type == 'category_checking':
            category_checkings = [self.category_checking_repository.getByReportId({'id': category_checking_id, 'report_id': report_id})
                                  for category_checking_id in report['category_checkings']]
            klavi_report.category_checkings = category_checkings

        if klavi_report.report_type == 'income':
            income_items = [self.income_repository.getByReportId({'id': income_id, 'report_id': report_id})
                            for income_id in report['income']]
            klavi_report.income = income_items

        return klavi_report
