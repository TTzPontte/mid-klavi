import pandas



def export_report_to_excel(report):
    print("LE REPORT")
    print(report)
    print("___________--")
    data_frame = pandas.DataFrame(report, index=[0])
    data_frame.to_excel("report_output.xlsx", sheet_name='Report_Sheet')