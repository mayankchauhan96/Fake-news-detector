from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from firebase import firebase

app = Flask(__name__)

firebase = firebase.FirebaseApplication("https://covid-19-fake-news-detector.firebaseio.com/", None)


@app.route("/sms", methods=['POST'])
def sms_reply():

    # Fetch the message
    msg = request.form.get('Body')
    print(msg)

    #json format for firebase
    data = {
        "title": "Title 1",     
        "news": msg,
        "status": "Nobody has flaged it till now"   
    }
    print("coming")
    
    #Create db
    create = firebase.post('/covid-19-fake-news-detector/Incoming', data)
    print(create['name'])


    #read db
    update = firebase.get('/covid-19-fake-news-detector/Incoming/'+create['name'],'status')
    print(update)

    # Create reply
    resp = MessagingResponse()
    resp.message(update)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)