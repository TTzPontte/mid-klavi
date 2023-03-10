getMember = """query MyQuery($id: ID!) {
  getMember(id: $id) {
    id
    email
    name
    documentNumber
    organizationId
    _version
  }
}
"""

listOrganizations = """query MyQuery {
  listOrganizations {
    items {
      id
      legalName
      name
      Members {
        items {
          id
          name
          organizationId
        }
      }
    }
  }
}
"""
get_org = """query MyQuery {
  getOrganization(id: $id) {
    id
    legalName
  }
}"""

getUser = """query MyQuery($id: ID!) {
  getUser(id: $id){
    id
  }
}
"""

createUser = """mutation createUser($input: CreateUserInput!) {
  createUser(input: $input){
    id
    name
    email
    welcome
  }
}
"""

get_cards_from_phase = """
        query GetCardsFromPhase($phase_id: ID!) {
            phase(id: $phase_id) {
                id
                name
                cards_count
                cards {
                    edges {
                        node {
                            fields {
                                field {
                                    id
                                    index_name
                                }
                                name
                                value
                            }
                        }
                    }
                }
            }
        }
    """
