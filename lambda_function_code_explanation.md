Lambda Function – Step-by-Step Python Code Explanation

This document explains the lambda_function.py file line by line in very simple language.
It is written for beginners who are new to AWS Lambda, API Gateway, DynamoDB, and serverless architecture.

----

1️⃣ Importing Required Libraries
import json
import os
import boto3

Explanation:

json → Used to format error responses

os → Reserved for environment variables (best practice)

boto3 → AWS SDK for Python (used to access DynamoDB)

----

2️⃣ Lambda Entry Point
def lambda_handler(event, context):

Explanation:

This is the main function executed by AWS Lambda

event → Contains request data from API Gateway

context → Contains runtime details (not used here)

----

3️⃣ Detecting HTTP Method (GET / POST)
httpmethod = event.get('httpMethod')

if not httpmethod:
    httpmethod = event['requestContext']['http']['method']

Explanation:

REST API sends httpMethod

HTTP API (v2) sends requestContext.http.method

This logic makes the Lambda compatible with both API types

✅ Interview Tip

“This makes the Lambda reusable across REST and HTTP APIs.”

-----

4️⃣ Routing Requests (Page Router)
mypage = page_router(
    httpmethod,
    event.get('queryStringParameters'),
    event.get('body')
)

Explanation:

Routes the request based on HTTP method

Keeps code clean and modular

Calls different logic for GET and POST

----

5️⃣ Handling GET Requests (Load Contact Form)
if httpmethod == 'GET':

with open('contactus.html', 'r') as htmlFile:
    htmlContent = htmlFile.read()

What Happens:

Reads contactus.html from Lambda package

Returns it as an HTTP response

Browser displays the contact form

----

6️⃣ Handling POST Requests (Form Submission)
elif httpmethod == 'POST':

insert_record(formbody)

with open('success.html', 'r') as htmlFile:
    htmlContent = htmlFile.read()

What Happens:

Receives form data

Inserts data into DynamoDB

Displays success page

----

7️⃣ Returning HTML Response
return {
    'statusCode': 200,
    'headers': {"Content-Type": "text/html"},
    'body': htmlContent
}

Explanation:

Sends HTML back to the browser

Browser renders the page normally

Works like a traditional web server (but serverless)

----

8️⃣ Inserting Data into DynamoDB (PartiQL)
def insert_record(formbody):

Step 1: Convert Form Data
formbody = formbody.replace("=", "' : '")
formbody = formbody.replace("&", "', '")

Explanation:

Converts form-encoded data into JSON-like structure

Required for PartiQL insert

Step 2: Build PartiQL Insert Query
formbody = "INSERT INTO leemou VALUE {'" + formbody + "'}"

Explanation:

Uses DynamoDB PartiQL

Inserts one item per request

leemou is the DynamoDB table name

Step 3: Execute DynamoDB Statement
client = boto3.client('dynamodb')
response = client.execute_statement(Statement=formbody)

Explanation:

Uses IAM role authentication

No credentials stored in code

Executes PartiQL safely

----

9️⃣ Error Handling (Very Important)
except Exception as e:
    return {
        'statusCode': 500,
        'body': json.dumps({'error': str(e)})
    }

Explanation:

Prevents Lambda from crashing

Returns readable error messages

Helps debugging in CloudWatch Logs

-----

🔐 IAM Permissions Required

This Lambda requires the following IAM permission:

"dynamodb:ExecuteStatement"
