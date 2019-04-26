import time
import paho.mqtt.client as paho

from mqtt_practise.handlers import BROKER, on_message, on_connect, \
    on_publish, on_subscribe, on_log

NewClient = paho.Client()

NewClient.on_message = on_message
NewClient.on_connect = on_connect
NewClient.on_publish = on_publish
NewClient.on_subscribe = on_subscribe
NewClient.on_log = on_log

NewClient.connect(BROKER, 1883)
NewClient.loop_start()

NewClient.subscribe("office/block/+", qos=2)
NewClient.subscribe([("office/kitchen/",2),("office/bath/",1),("office/factory/",0)])


NewClient.publish("office/block/3", "empty", qos=0)
NewClient.publish("office/block/5", "3 people", qos=1)
NewClient.publish("office/kitchen/", "5 people and 1 dog", qos=2)
time.sleep(1)
NewClient.loop_stop()



