import json

import boto3
from boto3.dynamodb.conditions import Key
from botocore.docs import paginator


def handler(event, _):
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
    table = dynamodb.Table('interventions')

    if len(event) == 0:
        response = table.scan()
    else:
        response = table.query(KeyConditionExpression=Key('id').eq(event['id']))

    return response['Items']
