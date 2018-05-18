def mcp(channel):
 adc = spi.xfer2([1,(8+channel)<<4,0])
# print(adc)
 data = ((adc[1]&3) << 8) + adc[2]
# print(data)
 return data
