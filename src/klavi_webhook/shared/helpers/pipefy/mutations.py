create_table_record_mutation = """ 
    mutation insertReacord($table_id: ID!, $title: String, $values: [FieldValueInput]) {
      createTableRecord(input: { table_id: $table_id, title: $title, fields_attributes: $values }) {
        table_record {
          id
        }
      }
    }
"""
