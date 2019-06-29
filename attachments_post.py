import boto3
import common


def handler(event, _):
    dynamodb = boto3.client('dynamodb', region_name='eu-west-1')

    payload = {
        'interventionId': {'S': event['interventionId']},
        'attachmentUrl': {'S': event['attachmentUrl']},
    }

    payload = common.strip_empty_values(payload)

    dynamodb.put_item(TableName='interventions', Item=payload)