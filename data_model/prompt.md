following the Nosql Workbench DataModel.json format bellow

```json
    {
  "TableName": "Activities",
  "KeyAttributes": {
    "PartitionKey": {
      "AttributeName": "id",
      "AttributeType": "S"
    },
    "SortKey": {
      "AttributeName": "date",
      "AttributeType": "S"
    }
  },
  "DataAccess": {
    "MySql": {}
  },
  "BillingMode": "PROVISIONED",
  "ProvisionedCapacitySettings": {
    "ProvisionedThroughput": {
      "ReadCapacityUnits": 5,
      "WriteCapacityUnits": 5
    },
    "AutoScalingRead": {
      "ScalableTargetRequest": {
        "MinCapacity": 1,
        "MaxCapacity": 10,
        "ServiceRole": "AWSServiceRoleForApplicationAutoScaling_DynamoDBTable"
      },
      "ScalingPolicyConfiguration": {
        "TargetValue": 70
      }
    },
    "AutoScalingWrite": {
      "ScalableTargetRequest": {
        "MinCapacity": 1,
        "MaxCapacity": 10,
        "ServiceRole": "AWSServiceRoleForApplicationAutoScaling_DynamoDBTable"
      },
      "ScalingPolicyConfiguration": {
        "TargetValue": 70
      }
    }
  }
}

```

write the DataModel.json for our application