# AWS Serverless Web Application (Lambda + API Gateway + DynamoDB)

## 📌 Repository Name
aws-serverless-web-application

## 📖 Description
A fully serverless AWS web application using API Gateway, AWS Lambda, and DynamoDB.
The application hosts a contact form that stores submitted data in DynamoDB and returns a success page.

---

## 🏗️ Architecture
User → API Gateway → Lambda → DynamoDB


<img width="1016" height="212" alt="image" src="https://github.com/user-attachments/assets/9bab42d5-f891-471f-a723-854cc464b1f6" />

*Figure 1: Serverless architecture showing Client → API Gateway → Lambda → DynamoDB**
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
└── IAM_POLICIES.md

```

---

## 🚀 Step-by-Step Guide
1. Create DynamoDB table `leetable`
2. Create IAM role for Lambda
3. Create Lambda function (Python 3.10)
4. Upload all files together
5. Create API Gateway (GET & POST)
6. Test via Invoke URL

   

<img width="1023" height="469" alt="image" src="https://github.com/user-attachments/assets/10e0ac4e-683a-4ea0-b970-25febf2718b6" />

*Figure 2: DynamoDB table leetable storing submitted form data**





<img width="1024" height="441" alt="image" src="https://github.com/user-attachments/assets/610ca712-f456-4fdd-ac5e-0a81a030d7e5" />

*Figure 3: IAM role attached to Lambda with DynamoDB access**





<img width="1013" height="438" alt="image" src="https://github.com/user-attachments/assets/9c189cb5-b079-428f-8e61-0a5b1ed7ef26" />

*Figure 4: Lambda function handling GET and POST requests**





<img width="1049" height="449" alt="image" src="https://github.com/user-attachments/assets/138e9862-dfab-4be7-baf8-a0f86f07f386" />

*Figure 5: HTML files packaged with Lambda deployment**





<img width="994" height="429" alt="image" src="https://github.com/user-attachments/assets/3407b97d-5db0-4350-950b-67d089281ffd" />

*Figure 6: API Gateway resources with GET and POST methods integrated with Lambda**





<img width="1030" height="521" alt="image" src="https://github.com/user-attachments/assets/d885e72b-83b3-4cd1-a8c4-f757c5a6ae21" />


<img width="1010" height="528" alt="image" src="https://github.com/user-attachments/assets/476cae47-e345-458f-8411-1cd64d403a09" />


<img width="970" height="530" alt="image" src="https://github.com/user-attachments/assets/008b5831-bc91-426f-8697-f328a1ddb225" />

<img width="970" height="444" alt="image" src="https://github.com/user-attachments/assets/71729823-b648-4c27-9c14-d03e152fb342" />

*Figure 7,8,9,10: Contact form loaded successfully via API Gateway invoke URL & Success Page  displayed with data’s updated in the DynamoDB table*






---

## 👨‍💻 Author
Mouli S
