import decimal


def strip_empty_values(payload):
    return {
        k: payload[k] for k in payload
        if payload[k].get('S', payload[k].get('N')) is not None
    }


def decimal_aware_json_serializer(obj):
    if isinstance(obj, decimal.Decimal):
        return int(obj)
    raise TypeError
