from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from firebase import firebase
# from flask_cors import CORS
from twilio.rest import Client
import pyrebase

config = {
    "apiKey": "AIzaSyAEEO1frXfzyL6MCkRvgGz7qURfsTLajRc",
    "authDomain" : "covid-19-fake-news-detector.firebaseapp.com",
    "databaseURL" : "https://covid-19-fake-news-detector.firebaseio.com",
    "projectId" : "covid-19-fake-news-detector",
    "storageBucket" : "covid-19-fake-news-detector.appspot.com",
    "messagingSenderId" : "401417810179",
    "appId" : "1:401417810179:web:b5c7dac2f172bfdc11f936",
    "measurementId" : "G-59YT063WPN"
}

fb = pyrebase.initialize_app(config)
db = fb.database()


app = Flask(__name__)
app.config.from_object(__name__)

firebase = firebase.FirebaseApplication("https://covid-19-fake-news-detector.firebaseio.com/", None)


@app.route("/status", methods=['POST'])
def sms_status(key):
    update = firebase.get('/Incoming/'+key['name'],'status')
    from_whatsapp_no = 'whatsapp:+14155238886'
    to_whatsapp_no = 'whatsapp:+9189********'
    account = "ACa0b9328e73aae3240844*******"
    token = "cdd6da1ea1baf8050d20005d*******"
    client = Client(account,token)
    
    return str(client.messages.create(body= update, from_ =from_whatsapp_no, to = to_whatsapp_no))


@app.route("/sms", methods=['POST'])
def sms_reply():
    # Fetch the message
    usrid = request.form.get('From')
    print(usrid)


    msg = request.form.get('Body')

    #json format for firebase
    data = {
        "userid": usrid,     
        "news": msg,
        "status": "Wait, we are processing your request"   
    }
    print("coming")

    #Create db
    key = firebase.post('/Incoming', data)
    print(key['name'])

    #read db
    update = firebase.get('/Incoming/'+key['name'],'status')
    print(update)

    # Create reply
    resp = MessagingResponse()
    resp.message(update)
    return str(resp)
    # else:
    #     default = "Wait, we are processing your request"
    #     return (default)

if __name__ == "__main__":
    app.run(debug=True)