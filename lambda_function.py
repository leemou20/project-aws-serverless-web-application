import json
import boto3
import urllib.parse

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('leetable')

def lambda_handler(event, context):
    try:
        method = event.get('httpMethod')
        if not method:
            method = event['requestContext']['http']['method']

        if method == 'GET':
            return load_page('contactus.html')

        if method == 'POST':
            data = urllib.parse.parse_qs(event['body'])
            save_data(data)
            return load_page('success.html')

        return {'statusCode': 405, 'body': 'Method Not Allowed'}

    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps(str(e))}

def load_page(file):
    with open(file) as f:
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html'},
            'body': f.read()
        }

def save_data(data):
    table.put_item(
        Item={
            'email': data['email'][0],
            'first_name': data['fname'][0],
            'last_name': data['lname'][0],
            'message': data['message'][0]
        }
    )
