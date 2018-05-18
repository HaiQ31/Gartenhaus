import sys
import Adafruit_DHT as dht
#import Python_DHT
#import RPi.GPIO as gpio
#import time

#while True:
#sensor = 11
#sensor = dht.DHT11
#pin = 4
#f, t = dht.read_retry(sensor, pin)
f, t = dht.read_retry(dht.DHT11, 4)
print("Temperatur = "+str(t)+ "C Feutigkeit = "+str(f)+"%")
#time.sleep(1)
