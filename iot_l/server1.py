
from flask import Flask

server=Flask(__name__)

@server.get('/')
def homepage():
    return "This is home page"

@server.get('/welcome')
def welcome():
    return "This is a welcome page"

server.run()
