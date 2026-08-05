
from flask import Flask,request

from dbconnection import get_dbconnection as dbconn

import paho.mqtt.client as mqtt
import random

server=Flask(__name__)

publisher=mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

publisher.connect("localhost",1883)

@server.get('/')
def homepage():
    return "Health monitoring system"

@server.post('/patient')
def add_patient():
    patient_id=request.get_json().get("patient_id")
    patient_name=request.get_json().get("patient_name")

    temperature=round(random.uniform(36,39),1)
    heartrate=random.randint(60,120)

    publisher.publish("hospital/action","add")
    publisher.publish("hospital/id",str(patient_id))
    publisher.publish("hospital/name",patient_name)
    publisher.publish("hospital/temp",str(temperature))
    publisher.publish("hospital/heartrate",str(heartrate))

    print("Temperature =", temperature)
    print("Heartrate =", heartrate)

    return "Patient added successfully"

@server.get('/patient')
def view_patient():
    query="""
    select * from patient order by patient_id desc limit 1"""

    conn=dbconn()
    curser=conn.cursor()
    curser.execute(query)
    patient=curser.fetchone()
    curser.close()
    conn.close()

    return{
        "patient_id":patient[0],
        "patient_name":patient[1],
        "temperature":patient[2],
        "heartrate":patient[3]
    }

@server.put("/patient")
def update_patient():
    patient_id=request.get_json().get('patient_id')

    temperature=round(random.uniform(36,39),1)
    heartrate=random.randint(60,120)

    publisher.publish("hospital/action","update")
    publisher.publish("hospital/id",str(patient_id))
    publisher.publish("hospital/temp",str(temperature))
    publisher.publish("hospital/heartrate",str(heartrate))

    return "Patient Updated Successfully"

@server.delete("/patient")
def delete_patient():

    patient_id=request.get_json().get("patient_id")

    publisher.publish("hospital/action","delete")
    publisher.publish("hospital/id",str(patient_id))

    return "Patient Deleted Successfully"


server.run(debug=True)