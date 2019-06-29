import logging

import boto3
from botocore.vendored import requests

l = logging.getLogger()


def handler(event, _):
    table = boto3.resource('dynamodb').Table('interventions')

    address = event['Records'][0]['dynamodb']['NewImage']['interventionAddress']['S']
    row_id = event['Records'][0]['dynamodb']['NewImage']['id']['S']
    row_createdAt = event['Records'][0]['dynamodb']['NewImage']['createdAt']['N']

    r = requests.get(f'https://nominatim.openstreetmap.org/search/{address}?format=json').json()

    table.update_item(
        Key={'id': row_id},
        UpdateExpression='SET #LAT = :lat, #LON = :lon',
        ExpressionAttributeNames={'#LAT': 'lat', '#LON': 'lon'},
        ExpressionAttributeValues={':lat': r[0]['lat'], ':lon': r[0]['lon']})
