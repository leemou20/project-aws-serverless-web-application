# AWS Serverless Web Application (Lambda + API Gateway + DynamoDB)

## 📌 Repository Name
aws-serverless-web-application

## 📖 Description
A fully serverless AWS web application using API Gateway, AWS Lambda, and DynamoDB.
The application hosts a contact form that stores submitted data in DynamoDB and returns a success page.

---

## 🏗️ Architecture
User → API Gateway → Lambda → DynamoDB

---

## 🛠️ Services Used
- AWS Lambda (Python)
- Amazon API Gateway (HTTP API)
- Amazon DynamoDB
- AWS IAM
- HTML / CSS
- boto3

---

## 📂 Project Structure
```
aws-serverless-web-application/
│
├── README.md
├── lambda_function.py
├── lambda_function_code_explanation.md
├── contactus.html
├── success.html
└── iam-policy.json
```

---

## 🚀 Step-by-Step Guide
1. Create DynamoDB table `leetable`
2. Create IAM role for Lambda
3. Create Lambda function (Python 3.10)
4. Upload all files together
5. Create API Gateway (GET & POST)
6. Test via Invoke URL

---

## 👨‍💻 Author
Mouli S
