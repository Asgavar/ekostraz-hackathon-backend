import json

import boto3

import common


def handler(event, context):
    dynamodb = boto3.client('dynamodb', region_name='eu-west-1')
    data = json.loads(event['body'])

    payload = {
        'interventionId': {'S': event['pathParameters']['interventionId']},
        'createdAt': {'S': data.get('createdAt', None)},
        'author': {'S': data.get('author', None)},
        'body': {'S': data.get('body', None)},
    }

    payload = {
        k: payload[k] for k in payload
        if payload[k].get('S', payload[k].get('N')) is not None
    }
    payload = common.strip_empty_values(payload)

    dynamodb.put_item(TableName='comments', Item=payload)

    return {
        'statusCode': 201,
        'headers': {
            'Access-Control-Allow-Origin': '*',
        }
    }
