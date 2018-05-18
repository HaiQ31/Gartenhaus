#!/usr/bin/python3

import spidev
import os
import RPi.GPIO as gpio
from urllib.request import urlopen
import time
import Adafruit_DHT as dht

# SPI Verbindung herstellen und Geschwindigkeit festlegen
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

# Daten vom MCP3008 lesen
def mcp(channel):
 adc = spi.xfer2([1,(8+channel)<<4,0])
 data = ((adc[1]&3) << 8) + adc[2]
 return data

licht = mcp(0)
sensor = dht.DHT11
pin = 17
feuchtigkeit, temperatur = dht.read_retry(sensor,pin)

# Messfehler abfangen
if str(feuchtigkeit) !='None' and feuchtigkeit > 100:
 time.sleep(2)
 feuchtigkeit, temperatur = dht.read_retry(sensor,pin)

fobj_out = open("wetter.txt","a")
fobj_out.write("\n"+time.strftime("%d.%m.%Y,%H:%M:%S") + ","+str(temperatur)+","+str(feuchtigkeit)+","+str(mcp(0)))
fobj_out.close()

# Daten an Thingspeak senden
baseURL = 'https://thingspeak.com/update?key='
APIkey = '1UD90R8GS1L0217H'

f1 = str(temperatur)
f2 = str(feuchtigkeit)
f3 = str(licht)

f = urlopen(baseURL + APIkey + '&field1=' + f1 + '&field2=' + f2 + '&field3=' + f3)
fdata = f.read()
fdata_out = open("tswrite.log","a")
# Website response in logfile schreiben
fdata_out.write("\n"+time.strftime("%d.%m.%Y,%H:%M:%S") + ","+str(fdata))
fdata_out.close()
#print(fdata)
f.close()

# Es wird ein cronjob in crontab -e angelget, der diese Datei regelmäßig ausfürht. Bei Änderungen beachten.
