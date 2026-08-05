import paho.mqtt.client as mqtt

def callback(client, userdata, message):
    print("Message received:", message.payload.decode())

subscriber = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

subscriber.on_message = callback

subscriber.connect(host="localhost", port=1883)

subscriber.subscribe("sensor/ldr")

print("Waiting for messages...")

subscriber.loop_forever()