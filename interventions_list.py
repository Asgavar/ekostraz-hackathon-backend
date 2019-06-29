import json

import boto3

import common


def handler(event, _):
    table = boto3.resource('dynamodb', region_name='eu-west-1').Table('interventions')
    return {
        'statusCode': 200,
        'body': json.dumps(table.scan()['Items'], default=common.decimal_aware_json_serializer),
    }
