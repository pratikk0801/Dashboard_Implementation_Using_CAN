
import paho.mqtt.client as mqtt

from dbconnection import get_dbconnection as dbconn

action=None
patient_id=None
patient_name=None
temperature=None
heartrate=None

def callback(client,userdata,message):
    global action
    global patient_id
    global patient_name
    global temperature
    global heartrate

    topic=message.topic
    payload=message.payload.decode()

    print(topic,payload)

    if topic=="hospital/action":
        action=payload
    elif topic=="hospital/id":
        patient_id=payload
    elif topic=="hospital/name":
        patient_name=payload
    elif topic=="hospital/temp":
        temperature=payload
    elif topic=="hospital/heartrate":
        heartrate=payload

    if action=="add":
        if patient_id and patient_name and temperature and heartrate:
            query=f"""insert into patient values({patient_id},'{patient_name}',{temperature},{heartrate});"""

            conn=dbconn()
            cursor=conn.cursor()
            cursor.execute(query)
            conn.commit()
            print("Patient inserted")
            cursor.close()
            conn.close()

            action=None
            patient_id=None
            patient_name=None
            temperature=None
            heartrate=None
    elif action=="update":
        if patient_id and temperature and heartrate:
            query=f"""update patient set temperature={temperature},heartrate={heartrate} where patient_id={patient_id};"""

            conn=dbconn()
            cursor=conn.cursor()
            cursor.execute(query)
            conn.commit()
            print("Patient updated")
            cursor.close()
            conn.close()
            
            action=None
            patient_id=None
            patient_name=None
            temperature=None
            heartrate=None

    elif action=="delete":
        if patient_id:
            query=f"""delete from patient where patient_id={patient_id};"""

            conn=dbconn()
            cursor=conn.cursor()
            cursor.execute(query)
            conn.commit()
            print("patirnt deleted")
            cursor.close()
            conn.close()

            action=None
            patient_id=None

subscriber=mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)

subscriber.on_message=callback

subscriber.connect("localhost",1883)

subscriber.subscribe("hospital/action")
subscriber.subscribe("hospital/id")
subscriber.subscribe("hospital/name")
subscriber.subscribe("hospital/temp")
subscriber.subscribe("hospital/heartrate")


subscriber.loop_forever()



            