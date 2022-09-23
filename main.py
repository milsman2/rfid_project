"""
All imports
"""
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import requests

reader = SimpleMFRC522()

try:
    while True:
        rfid, text = reader.read()
        webhook = requests.post("https://webhook-event.kanebroslab.com/example", json={"channel":"pets","message":"Margo pooped!"})
        webhook = requests.post("http://192.168.20.208:8001/api/v1/doodle/number_2")
        print(webhook.status_code)
finally:
    GPIO.cleanup()
