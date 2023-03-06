from dataclasses import dataclass
from shared.data_access_objects.identity import IdentityDAO
from shared.models.identity import IdentitySchema
from shared.models.identity import Identity


@dataclass
class IdentityRepository:
    def save(self, document):
        identity_schema = IdentitySchema()
        identity_document = identity_schema.dump(document)
        identity_dao = IdentityDAO()
        identity_dao.put(identity_document)


    def getByReportId(self, report_id):
        identity_dao = IdentityDAO()
        identity_obj = identity_dao.get(report_id)
        identity = Identity(**identity_obj)

        return identity
