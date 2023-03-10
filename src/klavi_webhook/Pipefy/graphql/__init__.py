from .GqlClient import GqlClient
def save_item(item: object, schema: object) -> object:
    print("----item----", item)
    gql = GqlClient(api_key=env)
    mutation_query = create_invite
    for key_name, key_value in item.items():
        if key_name == '$version':
            mutation_query = mutation_query.replace(key_name, f'{key_value}')
        else:
            mutation_query = mutation_query.replace(key_name, f'"{key_value}"')
    print("----mutation_query-----")
    print(mutation_query)
    response = gql.post(mutation_query)
    print(response.status_code)
    print(response.text)
    return json.loads(response.text)
