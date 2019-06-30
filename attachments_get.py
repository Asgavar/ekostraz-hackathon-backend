import json

import boto3
from boto3.dynamodb.conditions import Key


def handler(event, _):
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
    table = dynamodb.Table('attachments')

    response = table.query(
        KeyConditionExpression=Key('interventionId').eq(event['interventionId'])
    )

    return {
        'statusCode': 201,
        'body': json.dumps(response['Items']),
    }