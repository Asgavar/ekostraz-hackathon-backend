import boto3


def handler(event, _):
    bucket_location = boto3.client('s3').get_bucket_location(Bucket='ekostraz-attachments2')
    object_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
        bucket_location['eu-west-1'],
        'ekostraz-attachments2',
        event['fileName'])

    # Bucket name hardcoded

    return object_url;
