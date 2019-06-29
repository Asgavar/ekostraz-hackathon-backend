import boto3
from botocore.exceptions import ClientError
from pip._internal.utils import logging


def handler(event, _):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': "ekostraz-attachments2",
                                                            'Key': event['fileName']},
                                                    ExpiresIn=3600)
    except ClientError as e:
        logging.error(e)
        return None

    return response
