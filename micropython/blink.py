from machine import Pin
import time

myLED = Pin('D13', Pin.OUT)

while True:
    myLED.value(0)
    time.sleep(1)
    myLED.value(1)
    time.sleep(1)