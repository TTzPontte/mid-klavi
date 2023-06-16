import uuid

import boto3


class KlaviOpenStatementDAO:
    TABLE_NAME = 'Klavi-OpenStatement-staging'

    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table(self.TABLE_NAME)

    def update_item_with_pipefy_id(self, statement, card_id):
        statement_id = statement['id']
        update_expression = 'SET pipefy_card_id = :card_id'
        expression_attribute_values = {':card_id': card_id}

        # Update the item in the table
        self.table.update_item(Key={'id': statement_id}, UpdateExpression=update_expression,
                               ExpressionAttributeValues=expression_attribute_values, ReturnValues="UPDATED_NEW")

        # Retrieve the updated item from the table
        response = self.table.get_item(Key={'statement_id': statement_id})

        return response.get('Item')

    def get_statement_by_id(self, statement_id):
        response = self.table.get_item(Key={'statement_id': statement_id})
        return response.get('Item')

    def create_statement(self, statement_data):
        statement_data['id'] = str(uuid.uuid4())
        self.table.put_item(Item=statement_data)
        return statement_data

    def update_statement(self, statement_data, card_id):
        statement_data['pipefy_card_id'] = card_id
        self.table.put_item(Item=statement_data)
        return statement_data

    def delete_statement(self, statement_id):
        response = self.table.delete_item(Key={'statement_id': statement_id})
        return response
