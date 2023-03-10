createOrg = """mutation {
  createOrganization(input: {documentNumber: $documentNumber, name: $name, legalName: $legalName}) {
    id
    name
    legalName
  }
}"""

createMember = """mutation {
  createMember(input: {email: $email, documentNumber: $documentNumber, organizationId: $organizationId, name: $name}) {
    id
    name
    organizationId
    email
  } 
}
"""

createInvite = """mutation MyMutation {
  createUserInvite(input: {organizationId: $organizationId, organizationName: $organizationName, email: $email, status: pending, hostId: $hostId, guestId: $guestId, authType: $authType}) {
    id
    organizationId
    hostId
    guestId
    status
    organizationName
    email
    authType
  }
}
"""

updateOrganization = """mutation {
  updateOrganization(input: {id: $id, pipefyId: $pipefyId, _version: $version}) {
    id
    name
    pipefyId
  }
}
"""


_updateMember = """mutation MyMutation($input: UpdateMemberInput!) {
  updateMember(input: $input) {
    id
    email
    userId
    _version
  }
}
"""

updateUserInvite = """mutation {
  updateUserInvite(input: {id: $id, guestId: $guestId, hostId: $hostId, _version: 1}) {
    hostId
    guestId
    email
    id
  }
}
"""
