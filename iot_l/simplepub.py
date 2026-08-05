
import paho.mqtt.client as mqtt

publisher=mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

publisher.connect(host='localhost')

publisher.publish(topic='sensor/ldr',payload='4094')

publisher.disconnect()

