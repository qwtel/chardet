import json
import base64
import chardet

def detect(event, context):
    rawdata = base64.b64decode(event['body'])
    det = chardet.detect(rawdata)
    return {
        "statusCode": 200,
        "headers": {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps(det)
    }
