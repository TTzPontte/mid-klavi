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

update_card_field_mutation = """
mutation UpdateCardField($card_id: ID!, $field_id: ID!, $value: [UndefinedInput]!) {
      updateCardField(input: { card_id: $card_id, field_id: $field_id, new_value: $value }) {
        success
      }
    }
"""

