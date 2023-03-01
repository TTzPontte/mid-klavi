from shared.models.klavi_report import KlaviReportExcelSchema
from shared.exports.category_checking import export_category_checkings_to_excel
from shared.exports.category_creditcard import export_category_creditcard_to_excel
from shared.exports.liabilities import export_liabilities_to_excel
from shared.exports.financial_insight import export_financial_insight_to_excel

import pandas


def export_klavi_report_to_excel(report, output):
    report_schema = KlaviReportExcelSchema()
    pandas_excel_writter = pandas.ExcelWriter(output)
    data_frame = pandas.DataFrame(report_schema.dump(report), index=[0])
    data_frame.to_excel(pandas_excel_writter, sheet_name='Report')

    print("Genrating XLSX")
    if report.report_type == 'category_checking':
        export_category_checkings_to_excel(report, writer=pandas_excel_writter)
    if report.report_type == 'category_creditcard':
        export_category_creditcard_to_excel(report, writer=pandas_excel_writter)
    if report.report_type == 'liabilities':
        export_liabilities_to_excel(report, writer=pandas_excel_writter)
    if report.report_type == 'financial_insight':
        export_financial_insight_to_excel(report, writer=pandas_excel_writter)

    print("GEROU")


    #pandas_excel_writter.close()

    return pandas_excel_writter

