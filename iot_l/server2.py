
from flask import Flask

server=Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1> This is homepage </h1></body></html>"

@server.get('/welcome')
def welcome():
    return "<html><body><h1> welcome to Iot application </h1></body></html>"

server.run(host='0.0.0.0',port=4000,debug=True)

