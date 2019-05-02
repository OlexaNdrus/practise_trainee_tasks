import time
import paho.mqtt.client as paho

from handlers import BROKER, on_publish, on_subscribe, on_log


def on_connect(paho, userdata, flags, rc):
    paho.subscribe("office/block/3", qos=0)


def on_message(client, userdata, message):
    print(str(message.payload.decode("utf-8")))


if __name__ == '__main__':
    NewClient = paho.Client()
    NewClient.connect(BROKER, 1883, 60)

    NewClient.on_message = on_message
    NewClient.on_connect = on_connect
    NewClient.on_publish = on_publish
    NewClient.on_subscribe = on_subscribe
    NewClient.on_log = on_log


    NewClient.loop_forever()
