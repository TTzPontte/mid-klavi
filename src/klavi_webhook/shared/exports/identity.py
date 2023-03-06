from shared.models.identity import IdentitySchema

import pandas


def export_identity_to_excel(report, writer):
    identity_schema = IdentitySchema()
    identity = identity_schema.dump(report.identity)
    line = {}
    for key in identity:
        line[key] = identity[key]
    del line["correspondence_address"]
    for key in identity["correspondence_address"]:
        line[key] = identity["correspondence_address"][key]


    data_frame_identity = pandas.DataFrame([line])

    data_frame_identity.to_excel(writer, sheet_name="Identity")
