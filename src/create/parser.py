from collections import defaultdict

from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4).pprint
response = [
    {
        'enquiry_cpf': '70079872140',
        'json_report_url': 'https://s3.amazonaws.com/openfinance-dev/70079872140/category_checking.json',
        'report_type': 'category_checking',
        'title': 'Usuaro anonimo',
        'xlsx_report_url': 'https://s3.amazonaws.com/openfinance-dev/70079872140/category_checking.xlsx'
    },
    {
        'enquiry_cpf': '70079872140',
        'json_report_url': 'https://s3.amazonaws.com/70079872140/income.json',
        'report_type': 'income',
        'xlsx_report_url': 'https://s3.amazonaws.com/70079872140/income.xlsx'
    }
]
goal = [
    {
        'title': 'Usuaro anonimo',
        'enquiry_cpf': '70079872140',
        'category_checking': {
            'json_report_url': 'https://s3.amazonaws.com/openfinance-dev/70079872140/category_checking.json',
            'xlsx_report_url': 'https://s3.amazonaws.com/openfinance-dev/70079872140/category_checking.xlsx'
        },
        'income': {
            'json_report_url': 'https://s3.amazonaws.com/70079872140/income.json',
            'xlsx_report_url': 'https://s3.amazonaws.com/70079872140/income.xlsx'}
    }
]

merged_objects = defaultdict(dict)

for obj in response:
    cpf = obj['enquiry_cpf']
    merged_objects[cpf].update(obj)

normalized_response = list(merged_objects.values())

print(normalized_response)
