import json

print("AJR")

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! /n anisio manda abraço')
    }
