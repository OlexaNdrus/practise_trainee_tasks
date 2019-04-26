import time
import paho.mqtt.client as paho

BROKER = 'test.mosquitto.org'

def on_message(client, userdata, message):
    if not(client,userdata,message):
        print('noothiing')
    else:
        print("message received " ,str(message.payload.decode("utf-8")))
        print("message topic=",message.topic)
        print("message qos=",message.qos)
        print("message retain flag=",message.retain)

def on_subscribe(paho,userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_publish(paho,userdata,result,mid):
    print("data published \n" + mid)

def on_log(paho, userdata, level, buf):
    print("log: ",buf)

def on_connect(paho, userdata, rc):
    print('Connected with result code ' + str(rc))


