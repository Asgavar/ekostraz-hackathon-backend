import json
import logging
import random

import boto3

l = logging.getLogger()


def handler(event, _):
    dynamodb = boto3.client('dynamodb', region_name='eu-west-1')
    data = json.loads(event['body'])

    payload = {
        'id': {'S': str(random.randint(0, 999999))},
        'createdAt': {'N': str(data.get('createdAt', None))},
        'description': {'S': data.get('description', None)},
        'interventionAddress': {'S': data.get('interventionAddress', None)},
        'reporterEmail': {'S': data.get('reporterEmail', None)},
    }

    print('PRZED', payload)
    payload = {  # filter out non-existent keys
        k: payload[k] for k in payload
        if payload[k].get('S', payload[k].get('N')) is not None
    }
    print('PO', payload)

    dynamodb.put_item(TableName='interventions', Item=payload)

    return {
        'statusCode': 201
    }
