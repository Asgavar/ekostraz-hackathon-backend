import json

import boto3

import common


def handler(event, context):
    dynamodb = boto3.client('dynamodb', region_name='eu-west-1')
    data = json.loads(event['body'])

    payload = {
        'interventionId': {'S': event['pathParameters']['interventionId']},
        'createdAt': {'N': str(data.get('createdAt', None))},
        'author': {'S': data.get('author', None)},
        'body': {'S': data.get('body', None)},
    }

    payload = common.strip_empty_values(payload)

    dynamodb.put_item(TableName='comments', Item=payload)

    return {
        'statusCode': 201,
        'body': str(payload['interventionId']),
        'headers': {
            'Access-Control-Allow-Origin': '*',
        }
    }
