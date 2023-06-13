createCard = """
    mutation createCard($input: CreateCardInput!) {
        createCard(input: $input) {
            card {
                id
            }
        }
    }
    """
