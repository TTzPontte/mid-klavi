create_table_record_mutation = """ 
    mutation insertReacord($table_id: ID!, $title: String, $values: [FieldValueInput]) {
      createTableRecord(input: { table_id: $table_id, title: $title, fields_attributes: $values }) {
        table_record {
          id
        }
      }
    }
"""

create_card_into_pipe_mutation = """
mutation CreateCard($pipe_id: ID!, $fields_attributes: [FieldValueInput]!) {
      createCard(input: { pipe_id: $pipe_id, fields_attributes: $fields_attributes }) {
        card {
          id
        }
      }
    }
"""