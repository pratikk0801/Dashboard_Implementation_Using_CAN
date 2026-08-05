

import paho.mqtt.client as mqtt

publisher = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2
)

publisher.connect("localhost", 1883)

publisher.publish("sensor/ldr", "900")
publisher.publish("sensor/lm35", "27.5")

publisher.disconnect()