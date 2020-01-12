

import RPi.GPIO as GPIO #import the GPIO library
import time
from firebase import firebase 
firebase=firebase.FirebaseApplication('https://smart-security-e2179.firebaseio.com/')
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN)

name = "Ryan"
print("Hello " + name)

def fir_data():
    if GPIO.input(18):
       print("Door is open")
       status='open'
    if GPIO.input(18)==False:
       print("Door is closed")
       status='closed'
    data={"open":status}
    firebase.patch('smart-security-e2179',data)
while True:
    fir_data()
    time.sleep(1)
