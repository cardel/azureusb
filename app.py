from flask import Flask
from flask import request
import os
import json
from datetime import datetime
app = Flask(__name__)
import requests

@app.route('/')
def hello_world():
    #Retornar la hora y dia actual
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    temperature = requests.get("https://api.open-meteo.com/v1/forecast?latitude=3.4372&longitude=-76.5225&hourly=temperature_2m")
    return json.dumps({
        "message": "La hora actual:",
        "timestamp": current_time,
        "mensaje_temperatura":"La temperatura en Cali es",
        "temperatura": temperature.json()['hourly']['temperature_2m'][0]
    })

#this route add two numbers sended by GET method
@app.route("/sum", methods=['GET'])
def sum():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(a+b)

#this route substract two numbers sended by POST method
@app.route("/sub", methods=['POST'])
def sub():
    a = int(request.form['a'])
    b = int(request.form['b'])
    return str(a-b)

#this route multiply two numbers sended by GET method
@app.route("/mult", methods=['GET'])
def mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(a*b)

#this route divide two numbers sended by POST method
@app.route("/div", methods=['POST'])
def div():
    a = int(request.form['a'])
    b = int(request.form['b'])
    return str(a/b)

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0')
