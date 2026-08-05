
import paho.mqtt.client as mqtt
from dbconnection import get_dbconnection as dbconn

ldr=None
temp=None

def callback(client,userdata,message):

    global ldr
    global temp

    topic=message.topic
    payload=message.payload.decode()

    print(topic,payload)

    if topic=="sensor/ldr":
        ldr=payload
    elif topic=="sensor/lm35":
        temp=payload

    if ldr is not None and temp is not None:

        query= f"""insert into sensors(intensity,temperature)values({ldr},{temp});
        """

        conn=dbconn()
        cursor=conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print("Record Inserted")
        ldr=None
        temp=None

subscriber = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)
subscriber.on_message=callback
subscriber.connect("localhost",1883)
subscriber.subscribe("sensor/ldr")
subscriber.subscribe("sensor/lm35")
subscriber.loop_forever()

