import json

import boto3
from boto3.dynamodb.conditions import Key


def handler(event, _):
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
    table = dynamodb.Table('interventions')

    response = table.query(
        KeyConditionExpression=Key('id').eq(event['id'])
    )

    return response['Items']
