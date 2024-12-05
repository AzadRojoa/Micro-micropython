from machine import Pin,PWM
import time

micro = Pin(4, mode=Pin.IN)
LED = Pin(32, mode=Pin.OUT)
while True:
    print( micro.value())
    if micro.value():
        LED.value(1)
    else:
        LED.value(0)
    time.sleep(0.2)