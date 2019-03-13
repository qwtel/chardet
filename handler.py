import json
import base64
import chardet

cors_headers = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Credentials": True,
}

def detect(event, context):
    if not 'body' in event:
        return {
            "statusCode": 400,
            "headers": cors_headers,
            "body": json.dumps({ "error": "No request body" })
        }

    try:
        rawdata = base64.b64decode(event['body'])
        det = chardet.detect(rawdata)
        return {
            "statusCode": 200,
            "headers": cors_headers,
            "body": json.dumps(det)
        }
    except:
        e = sys.exc_info()[0]
        return {
            "statusCode": 500,
            "headers": cors_headers,
            "body": json.dumps({ "error": "%s" % e })
        }
