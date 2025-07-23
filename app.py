from flask import Flask
from flask import request
import os
import json
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
    #Retornar la hora y dia actual
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return json.dumps({
        "message": "La hora actual es la siguiente:",
        "timestamp": current_time
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
