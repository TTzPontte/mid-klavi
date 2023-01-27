from shared.models.klavi_report import KlaviReportExcelSchema
from shared.exports.category_checking import export_category_checkings_to_excel
import pandas


def export_klavi_report_to_excel(report, output):
    report_schema = KlaviReportExcelSchema()
    pandas_excel_writter = pandas.ExcelWriter(output)
    data_frame = pandas.DataFrame(report_schema.dump(report), index=[0])
    data_frame.to_excel(pandas_excel_writter, sheet_name='Report')

    if report.report_type == 'category_checking':
        export_category_checkings_to_excel(report, writer=pandas_excel_writter)


    pandas_excel_writter.close()

    return output

