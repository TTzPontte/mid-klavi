import json
import os
from http import HTTPStatus

import requests
from common.handlerbase import Handler, Result

from helpers.Models.Payload import Parser
from helpers.Models.s3_helper import S3Helper
from helpers.Pipefy.search.main import PipefyDataFacade
from helpers.ReportURLsDAO import ReportURLsDAO
from helpers.email_helper.validate_payload import validate_payload
from helpers.Pipefy.create import make_variables, send_to_pipefy

ENV = os.getenv('ENV')


def send_to_pipedream(new_dict):
    url = "https://eonzjtv05gp53jt.m.pipedream.net"
    resp = requests.post(url, data=json.dumps(new_dict))
    print(resp)
    return resp


def find_relation(enquiry_cpf):
    he_bacem_phase_id = "319165329"
    fi_bacem_phase_id = "319165324"
    facade = PipefyDataFacade(he_phase_id=he_bacem_phase_id, fi_phase_id=fi_bacem_phase_id, document_number=enquiry_cpf)
    facade.run()
    return facade


def make_report_urls( enquiry_cpf, report_type):
    json_key = f"{enquiry_cpf}/{report_type}.json"
    xlsx_key = f"{enquiry_cpf}/{report_type}.xlsx"
    json_report_url = f"https://s3.amazonaws.com/openfinance-dev/{json_key}"
    xlsx_report_url = f"https://s3.amazonaws.com/openfinance-dev/{xlsx_key}"
    return json_report_url, xlsx_report_url


def make_files(xlsx_report_url, json_report_url):
    obj = {"xlsx_report_url": xlsx_report_url, "json_report_url": json_report_url}
    print("obj: %s" % obj)
    return obj


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
        if "query_param" in body:
            del body["query_param"]

        data = body.get("data")
        enquiry_cpf = data.get("enquiry_cpf")
        report_type = data.get("report_type").lower()
        report_types = ["category_checking", "income"]
        if report_type in "category_checking":
            bucket_name = "openfinance-dev"
            json_report_url, xlsx_report_url = make_report_urls( enquiry_cpf, report_type)
            print("-----")
            print("-----")
            print("json_report_url, xlsx_report_url", json_report_url, xlsx_report_url)
            s3_helper = S3Helper()
            s3_helper.save_to_s3(json.dumps(body), bucket_name, json_report_url)

            parser = Parser(**body)
            other_report = None
            title = None

            if report_type == "income":
                other_report = "category_checking"
                parser.income_to_excel(xlsx_report_url)
                title = data.get('Income')[0].get("account_holder")
            elif report_type == "category_checking":
                other_report = "income"
                parser.category_checking_to_excel(xlsx_report_url)
                title = data.get("Category_checking")[0].get("holder_name")

            dao = ReportURLsDAO(ENV)
            base_obj = {"enquiry_cpf": enquiry_cpf, "title": title, "report_type": report_type}
            current_report = make_files(xlsx_report_url, json_report_url)
            dao.put_item({**base_obj, **current_report})

            file_counts = s3_helper.count_files_in_s3_bucket( enquiry_cpf, report_types)

            has_both_reports = all(value == 2 for value in file_counts.values())
            new_dict = {**base_obj, f'{report_type}': current_report}
            if has_both_reports:
                other_json_report_url, other_xlsx_report_url = make_report_urls( enquiry_cpf, other_report)
                print("other_json_report_url, other_xlsx_report_url", other_json_report_url, other_xlsx_report_url)
                facade = find_relation(enquiry_cpf)

                variables = make_variables(facade, title, report_type, other_report, other_json_report_url,
                                           json_report_url,
                                           enquiry_cpf, xlsx_report_url, other_xlsx_report_url)
                card = send_to_pipefy(variables)
                return Result(HTTPStatus.OK, card)

            return Result(HTTPStatus.OK, new_dict)
        return Result(HTTPStatus.OK, {"report_type": report_type})


def handler(event, context):
    print("Event: %s", event)
    return OpenFinanceCreate(event, context).run()
