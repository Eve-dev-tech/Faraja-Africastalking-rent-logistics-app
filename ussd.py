import os
import africastalking 
from flask import Flask, request

app = Flask(__name__)
username = "sandbox"
api_key = "sandbox"
africastalking.initialize(username, api_key)
sms = africastalking.SMS

#response = ""

@app.route("/ussd", methods = ['POST', 'GET'])

def ussd():
    global response
    session_id = request.values.get("sessionId",None)
    serviceCode =  request.values.get("serviceCode",None)
    phone_number = request.values.get("phoneNumber",None)
    text = request.values.get("text", "null")
    sms_phone_number = []
    sms_phone_number.append(phone_number)


    if text == "":
        response = "CON Welcome to Maridadi house customer service. Choose a service you'd like below?\n"
        response += "1.Make payment \n"
        response += "2. Report an issue or repair service\n"
    elif text == "2":
        response = "CON Choose the service that you require:\n"
        response += "1. Complaints\n"
        response += "2. Services\n"
    elif text == "2*1":
        response = "CON Choose the complaint that you have:\n"
        response += "1. Noise\n"
        response += "2. Theft\n"
        response += "3. Water shortage\n"
        response += "4. Electrical shortage\n"
    elif text == "2*2":
        response = "CON Choose the Service that you require:\n"
        response += "1. Plumbing\n"
        response += "2. Deposit refund\n"
        response += "3. Internet connection\n"
           

    else:
        response = "END Invalid choice"

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=os.environ.get("PORT"),debug=True)
