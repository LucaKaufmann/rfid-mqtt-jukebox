#!/usr/bin/env python

import psutil
import subprocess
from subprocess import Popen
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

client = mqtt.Client("JokeboxControl")
mqtt.Client.connected_flag=False#create flag in class

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        client.subscribe("jukebox/control/#")
    else:
        print("Bad connection Returned code=",rc)


def on_message(client, userdata, msg):
    payload = str(msg.payload.decode("utf-8"))
    topic = msg.topic
    print("Received message '" + payload + "' on topic '"
        + topic + "' with QoS " + str(msg.qos))

    if topic == 'jukebox/control/on':
        print('Starting RFID process')
        Popen(['/usr/bin/python3', '-u', '/path/to/jukebox.py'])
    elif topic == 'jukebox/control/off':
        for process in psutil.process_iter():
           if process.cmdline() == ['/usr/bin/python3', '-u', '/path/to/jukebox.py']:
             print('Process found. Terminating it.')
             process.terminate()
             break
    elif topic == 'jukebox/control/shutdown':
        subprocess.call("sudo shutdown now", shell=True)

client.username_pw_set('user', 'password')

client.on_connect=on_connect  #bind call back function
client.on_message=on_message
client.loop_start()
client.connect('MQTT_BROKER_IP', 1883)
while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)

while 1:
    print("")
    time.sleep(10)