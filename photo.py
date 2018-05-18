import spidev
import time
import os
import RPi.GPIO as gpio
from mcp3008 import mcp

# SPI Verbindung herstellen
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

# Liest Daten vom MCP3008

#def mcp3008(channel):
# adc = spi.xfer2([1,(8+channel)<<4,0])
## print(adc)
# data = ((adc[1]&3) << 8) + adc[2]
## print(data)
# return data

while True:
  wert = mcp(0)
#  print("wert: ", wert)
  print("0: "+str(analogEingang(0)))
  time.sleep(1)
