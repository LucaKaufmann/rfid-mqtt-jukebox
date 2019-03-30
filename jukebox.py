#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
from time import sleep
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

reader = SimpleMFRC522.SimpleMFRC522()
client = mqtt.Client("hass-client")
client.username_pw_set('user', 'password')
client.connect('IP', 1883)
client.loop_start()

try:
        while True:
            id, text = reader.read()
            print(id)
            print(text)
            client.publish("jukebox/play", text, retain=False)
            print("Published message")
            sleep(5)
finally:
        GPIO.cleanup()