import json

import boto3


def handler(event, _):
    s3 = boto3.client('s3')
    url = s3.generate_presigned_url(
        ClientMethod='put_object',
        Params={
            'Bucket': 'ekostraz-attachments4',
            'Key': json.loads(event['body'])['filename'],
        })

    return {
        'statusCode': 200,
        'body': json.dumps({'signedUrl': url}),
    }
