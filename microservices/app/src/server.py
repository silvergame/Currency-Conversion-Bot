from src import app
from flask import render_template
# from flask import jsonify

import requests
import urllib
import json
import os


#scnsjcn
from flask import request
from flask import make_response,Response
from functools import wraps

def check_auth(username, password):
    url = "https://auth.audiologist98.hasura-app.io/v1/login"
    # This is the json payload for the query
    requestPayload = {
        "provider": "username",
        "data": {
            "username": username,
            "password": password
        }
    }

    # Setting headers
    headers = {
        "Content-Type": "application/json"
    }

    # Make the query and store response in resp
    resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)
    # resp.content contains the json response.
    print(resp.content)
    #if "auth_token" in resp.content:
    if resp.content:
        return True
    else:
        return False
def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        #auth = request.authorization
        #print(request["contexts"])
        print(request.data)
        if check_auth(auth.usernae, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated



@app.route('/')
def home():
    return "Welcome to App service LATEST UPDATED - 1st March "

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    result = req.get("result")
    parameters = result.get("parameters")
    fro = parameters.get("from")
    to = parameters.get("to")
    to=to.upper()
    fro=fro.upper()
    no = float(parameters.get("number"))
    st1=fro+'_'+to
    r=requests.get('https://free.currencyconverterapi.com/api/v5/convert?q='+st1)

    print(r.content)
    r=json.loads(r.content)
    cost=r["results"][st1]["val"] * no
    print(cost)
    cost =round(answer,3)
    #print(cost1)

    speech = "Amount in " + to + " is " + str(cost)

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        #"source": "apiai-onlinestore-shipping"
    }


