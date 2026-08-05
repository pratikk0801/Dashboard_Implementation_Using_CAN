
from flask import Flask,request

server=Flask(__name__)

@server.get('/')
def home():
    return "Temperature and Light server"

@server.post('/data')
def store_data():
    temperature=request.get_json().get("temperature")
    light=request.get_json().get("light")

    with open("temperature.txt","w") as file:
        file.write(str(temperature))

    with open("light.txt","w") as file:
        file.write(str(light))

    return "Data stored Successfully"

@server.get("/temperature")
def get_temperature():
    with open("temperature.txt","r") as file:
        return file.read()
    
@server.get("/light")
def get_light():
    with open("light.txt","r") as file:
        return file.read()
    
if __name__ == "__main__":
    server.run(debug=True)