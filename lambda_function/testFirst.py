import json
import boto3


def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('8PIN-TEST-PROBLEM')

    result = table.get_item(
        Key={
            'ID': 'test'
        }
    )

    return {
        'statusCode': 200,
        'body': str(result['Item']['ANS'])
    }
