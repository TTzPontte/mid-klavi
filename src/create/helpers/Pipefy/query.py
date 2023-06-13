createCard = """
    mutation createCard($input: CreateCardInput!) {
        createCard(input: $input) {
            card {
                id
            }
        }
    }
    """
get_cards_from_phase = """query GetCardsFromPhase($phase_id: ID!) {
  phase(id: $phase_id) {
    id
    name
    cards_count
    cards {
      edges {
        node {
          id
          title
          fields {
            field {
              id
              index_name
            }
            name
            value
            array_value
          }
        }
      }
    }
  }
}
"""
