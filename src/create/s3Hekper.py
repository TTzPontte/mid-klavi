import json
import logging
import os
from dataclasses import dataclass
from http import HTTPStatus

import boto3
from botocore.exceptions import ClientError

from common.handlerbase import Handler, Result
from helpers.Models.Payload import Parser
from helpers.Pipefy.GqlClient import PipefyClient
from helpers.Pipefy.query import createCard
from helpers.Pipefy.search import PipefyDataFacade
from helpers.ReportURLsDAO import ReportURLsDAO
from helpers.email_helper.validate_payload import validate_payload

ENV = os.getenv('ENV')
BUCKET_NAME = "openfinance-dev"
REPORT_TYPES = ["category_checking", "income"]
HE_BACEM_PHASE_ID = "319165329"
FI_BACEM_PHASE_ID = "319165324"

@dataclass
class S3Helper:
    enquiry_cpf: str
    BUCKET_NAME: str = BUCKET_NAME
    s3_client = boto3.client("s3")

    def generate_report_urls(self, enquiry_cpf, report_type):
        json_key = f"{enquiry_cpf}/{report_type}.json"
        xlsx_key = f"{enquiry_cpf}/{report_type}.xlsx"
        json_report_url = f"https://s3.amazonaws.com/{BUCKET_NAME}/{json_key}"
        xlsx_report_url = f"https://s3.amazonaws.com/{BUCKET_NAME}/{xlsx_key}"
        return json_report_url, xlsx_report_url

    def save_to_s3(self, body, bucket_name, key):
        """Save data to S3."""
        try:
            self.s3_client.put_object(Body=body, Bucket=bucket_name, Key=key)
        except ClientError as e:
            logging.error(e)
            raise RuntimeError(f"Failed to save data to S3. Bucket: {bucket_name}, Key: {key}")

    def list_files_in_s3_bucket(self, enquiry_cpf, report_types):
        files = []
        for report_type in report_types:
            prefix = f"{enquiry_cpf}/{report_type}"
            response = self.s3_client.list_objects_v2(Bucket=BUCKET_NAME, Prefix=prefix)

            if 'Contents' in response:
                files.append(response['Contents'])
        return files

    def count_files_in_s3_bucket(self, enquiry_cpf, report_types):
        file_counts = {report_type: 0 for report_type in report_types}

        for report_type in report_types:
            prefix = f"{enquiry_cpf}/{report_type}"
            response = self.s3_client.list_objects_v2(Bucket=BUCKET_NAME, Prefix=prefix)

            if 'Contents' in response:
                file_counts[report_type] = len(response['Contents'])
            else:
                file_counts[report_type] = 0

        return file_counts


class ReportManager:
    def __init__(self, body):
        self.body = body
        self.s3_helper = S3Helper()

    def generate_report_urls(self, enquiry_cpf, report_type):
        json_key = f"{enquiry_cpf}/{report_type}.json"
        xlsx_key = f"{enquiry_cpf}/{report_type}.xlsx"
        json_report_url = f"https://s3.amazonaws.com/{BUCKET_NAME}/{json_key}"
        xlsx_report_url = f"https://s3.amazonaws.com/{BUCKET_NAME}/{xlsx_key}"
        return json_report_url, xlsx_report_url

    def save_report_to_s3(self, json_report_url):
        self.s3_helper.save_to_s3(json.dumps(self.body), BUCKET_NAME, json_report_url)

    def generate_excel(self, xlsx_report_url, report_type):
        parser = Parser(**self.body)
        if report_type == "income":
            parser.income_to_excel(xlsx_report_url)
        else:
            parser.category_checking_to_excel(xlsx_report_url)


class PipefyCardCreator:
    def __init__(self, enquiry_cpf, report_type, other_report, title,
                 json_report_url, xlsx_report_url, other_json_report_url, other_xlsx_report_url):
        self.enquiry_cpf = enquiry_cpf
        self.report_type = report_type
        self.other_report = other_report
        self.title = title
        self.json_report_url = json_report_url
        self.xlsx_report_url = xlsx_report_url
        self.other_json_report_url = other_json_report_url
        self.other_xlsx_report_url = other_xlsx_report_url

    def generate_variables(self, facade):
        fields = [
            {"field_id": "nome", "field_value": self.title},
            {"field_id": "cpf_cnpj", "field_value": self.enquiry_cpf},
            {"field_id": f'{self.report_type}_xlsx', "field_value": self.xlsx_report_url},
            {"field_id": f'{self.other_report}_xlsx', "field_value": self.other_xlsx_report_url},
            {"field_id": f'{self.report_type}_json', "field_value": self.json_report_url},
            {"field_id": f'{self.other_report}_json', "field_value": self.other_json_report_url}
        ]
        return {"input": {"pipe_id": "303111869", "parent_ids": facade.related_cards, "fields_attributes": fields}}

    def create_card(self):
        facade = PipefyDataFacade(he_phase_id=HE_BACEM_PHASE_ID, fi_phase_id=FI_BACEM_PHASE_ID,
                                  document_number=self.enquiry_cpf)
        facade.run()

        variables = self.generate_variables(facade)
        client = PipefyClient()
        card = client.post(createCard, variables)
        return card


class OpenFinanceCreate(Handler):
    def pre_process(self):
        if isinstance(self.event["body"], str):
            self.event["body"] = json.loads(self.event["body"])
        if "query_param" in self.event["body"]:
            del self.event["body"]["query_param"]

    def validate(self) -> Result:
        error = validate_payload(self.event['body'])
        if error:
            return Result(HTTPStatus.BAD_REQUEST, error)

    def handler(self):
        body = self.event["body"]
        data = body.get("data")
        enquiry_cpf = data.get("enquiry_cpf")
        report_type = data.get("report_type").lower()

        if report_type in REPORT_TYPES:
            report_manager = ReportManager(body)
            json_report_url, xlsx_report_url = report_manager.generate_report_urls(enquiry_cpf, report_type)
            report_manager.save_report_to_s3(json_report_url)
            report_manager.generate_excel(xlsx_report_url, report_type)

            title = data.get('Income')[0].get("account_holder") if report_type == "income" \
                else data.get("Category_checking")[0].get("holder_name")

            dao = ReportURLsDAO(ENV)
            base_obj = {"enquiry_cpf": enquiry_cpf, "title": title, "report_type": report_type}
            current_report = {"xlsx_report_url": xlsx_report_url, "json_report_url": json_report_url}
            dao.put_item({**base_obj, **current_report})

            file_counts = S3Helper().count_files_in_s3_bucket(enquiry_cpf, REPORT_TYPES)
            has_both_reports = all(value == 2 for value in file_counts.values())
            new_dict = {**base_obj, f'{report_type}': current_report}

            if has_both_reports:
                other_report = "income" if report_type == "category_checking" else "category_checking"
                other_json_report_url, other_xlsx_report_url = report_manager.generate_report_urls(
                    enquiry_cpf, other_report
                )
                report_manager.save_report_to_s3(other_json_report_url)
                report_manager.generate_excel(other_xlsx_report_url, other_report)

                card_creator = PipefyCardCreator(
                    enquiry_cpf, report_type, other_report, title,
                    json_report_url, xlsx_report_url, other_json_report_url, other_xlsx_report_url
                )
                card = card_creator.create_card()
                return Result(HTTPStatus.OK, card)

            return Result(HTTPStatus.OK, new_dict)

        return Result(HTTPStatus.OK, {"report_type": report_type})


def handler(event, context):
    return OpenFinanceCreate(event, context).run()
