from dataclasses import dataclass

import boto3




@dataclass
class DynamoDbORM:
    env: str
    db_name: str
    amplify: bool = False

    def _get_table_name(self):
        table_name = f"{self.db_name}-{self.env}" if not self.amplify else f"{self.db_name}.{self.env}"
        return table_name

    def __post_init__(self):
        self.dynamodb = boto3.resource('dynamodb', endpoint_url='http://127.0.0.1:8001' if self.env == 'dev' else None)
        self.table = self.dynamodb.Table(self._get_table_name())

    def get(self, key):
        response = self.table.get_item(Key=key)
        return response.get('Item')

    def query(self, index_name, key_condition):
        items = []
        response = self.table.query(IndexName=index_name, KeyConditionExpression=key_condition)
        items += response.get("Items", [])
        while 'LastEvaluatedKey' in response:
            response = self.table.query(IndexName=index_name, KeyConditionExpression=key_condition,
                                        ExclusiveStartKey=response['LastEvaluatedKey'])
            items += response.get("Items", [])
        return items

    def scan(self, filter_expression=None):
        items = []
        if filter_expression:
            response = self.table.scan(FilterExpression=filter_expression)
        else:
            response = self.table.scan()
        items += response.get("Items", [])
        while "LastEvaluatedKey" in response:
            if filter_expression:
                response = self.table.scan(FilterExpression=filter_expression,
                                           ExclusiveStartKey=response["LastEvaluatedKey"])
            else:
                response = self.table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
            items += response.get("Items", [])
        return items

    def put(self, item):
        self.table.put_item(Item=item)

    def update(self, key, updates):
        update_expression = "set " + ", ".join(f"{k} = :{k}" for k in updates.keys())
        expression_attribute_values = {f':{k}': v for k, v in updates.items()}
        self.table.update_item(Key=key, UpdateExpression=update_expression,
                               ExpressionAttributeValues=expression_attribute_values,
                               ReturnValues="UPDATED_NEW")

    def delete(self, key):
        self.table.delete_item(Key=key)

    def batch_put(self, items: list):
        with self.table.batch_writer() as batch:
            for item in items:
                batch.put_item(Item=item)

    def batch_delete(self, keys: list):
        with self.table.batch_writer() as batch:
            for key in keys:
                batch.delete_item(Key=key)

    def get_relations(self, main_table, main_key, relation_list):
        main_record = self.get(main_table, main_key)
        related_records = {}
        for relation in relation_list:
            related_record = self.get(relation, main_key)
            if related_record:
                related_records[relation] = related_record
        main_record.update(related_records)
        return main_record
