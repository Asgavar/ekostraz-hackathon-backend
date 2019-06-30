import json
import boto3
import common


def handler(event, _):
    dynamodb = boto3.client('dynamodb', region_name='eu-west-1')

    payload = {
        'interventionId': {'S': event['pathParameters']['interventionId']},
        'attachmentUrl': {'S': json.loads(event['body'])['attachmentUrl']},
    }

    payload = common.strip_empty_values(payload)

    dynamodb.put_item(TableName='attachments', Item=payload)

    return {
        'statusCode': 201,
        'headers': {
            'Access-Control-Allow-Origin': '*',
        }
    }
