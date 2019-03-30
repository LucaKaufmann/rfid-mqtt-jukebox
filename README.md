# rfid-mqtt-jukebox
A set of scripts to turn a Raspberry Pi combined with an mfrc522 RFID card reader into a jukebox.

# Installation/What's needed
* Set up the Raspberry Pi + RFID Chip: [https://pimylifeup.com/raspberry-pi-rfid-rc522/](https://pimylifeup.com/raspberry-pi-rfid-rc522/)
* Clone this repository
* Edit jukebox.py add your MQTT credentials
* Edit jukebox_control.py, add MQTT credentials and path to jukebox.py
* Optional: Use systemd to start jukebox_control.py on boot.

# Scripts description
jukebox.py: Takes care of reading the RFID cards and sending the values to an MQTT topic
jukebox_control.py: Takes care of starting and stopping jukebox.py, as well as shutting down the raspberry pi to allow you to remotely control it

# Write the RFID cards
Use the write.py script to write data to your RFID cards. I went with numbering them starting from 1. Those values will then get sent to the MQTT topic and can be used to assign different songs/playlists to each card.

# Node Red flow
Check example_flow for an example. I'm using Sonos speakers and the following method to play a random Sonos playlist: [https://www.reddit.com/r/homeassistant/comments/agdbh2/neat_trick_autoplaying_sonos_favorites_by_emoji/](https://www.reddit.com/r/homeassistant/comments/agdbh2/neat_trick_autoplaying_sonos_favorites_by_emoji/)
