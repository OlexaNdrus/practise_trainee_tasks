import time
import paho.mqtt.client as paho

from handlers import BROKER, on_message, on_connect, \
    on_publish, on_subscribe, on_log

if __name__ == '__main__':
    NewClient = paho.Client()

    NewClient.on_message = on_message
    NewClient.on_connect = on_connect
    NewClient.on_publish = on_publish
    NewClient.on_subscribe = on_subscribe
    NewClient.on_log = on_log

    NewClient.connect(BROKER, 1883, 60)

    while True:
        NewClient.publish("office/block/3", "empty", qos=0)
        time.sleep(3)
