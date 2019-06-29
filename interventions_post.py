import json
import logging
import uuid

import boto3

import common

l = logging.getLogger()


def handler(event, _):
    dynamodb = boto3.client('dynamodb', region_name='eu-west-1')
    data = json.loads(event['body'])

    assigned_id = str(uuid.uuid4())
    payload = {
        'id': {'S': assigned_id},
        'createdAt': {'N': str(data.get('createdAt', None))},
        'description': {'S': data.get('description', None)},
        'interventionAddress': {'S': data.get('interventionAddress', None)},
        'phoneNumber': {'S': data.get('phoneNumber', None)},
        'reporterEmail': {'S': data.get('reporterEmail', None)},
        'reporterName': {'S': data.get('reporterName', None)},
        'status': {'S': data.get('status', None)}
    }

    payload = common.strip_empty_values(payload)

    dynamodb.put_item(TableName='interventions', Item=payload)

    return {
        'statusCode': 201,
        'body': json.dumps({'id': assigned_id}),
    }
