import json
import logging
import random
import uuid

import boto3

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
        'phoneNumber': {'S' : data.get('phoneNumber', None)},
        'reporterEmail': {'S': data.get('reporterEmail', None)},
        'reporterName': {'S' : data.get('reporterName', None)},
        'status': {'S' : data.get('status', None)},
    }

    payload = {  # filter out non-existent keys
        k: payload[k] for k in payload
        if payload[k].get('S', payload[k].get('N')) is not None
    }

    dynamodb.put_item(TableName='interventions', Item=payload)

    return {
        'statusCode': 201,
        'body': json.dumps({'id': assigned_id}),
    }
