import json

import boto3
from boto3.dynamodb.conditions import Key


def handler(event, _):
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
    table = dynamodb.Table('interventions')

    response = table.query(
        KeyConditionExpression=Key('id').eq(event['pathParameters']['id']))

    if len(response['Items']) == 0:
        return {'statusCode': 404}

    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'][0]),
    }
