'''
Created on Nov 8, 2019

@author: soaresb1
'''

#!/usr/bin/python
import Adafruit_DHT
import time
from socket import *
import sys
from threading import Thread

mySocket = socket(AF_INET, SOCK_STREAM)
serverPort = 1234
mySocket.bind(('',serverPort))
mySocket.listen(5)
print('Ready to accept connections.')

while True:
    connectionSocket, addr = mySocket.accept()
    print('%s:%s has connected' % addr)

    print('Fetching temperature...')
    tick = 1
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4) #on gpio pin 4
        if humidity is not None and temperature is not None:
            humidity = round(humidity, 1)
            temperature = round(temperature, 1)
            msg2 = 'Tempurature = {0:0.1f}*C Humidity = {1:0.1f}%'.format(temperature, humidity)
            msg = '{0}, {1:0.1f}'.format(tick ,temperature)
            connectionSocket.send(msg.encode())
            print(msg2)
        else:
            print('Can not connect to the sensor!')
        tick = tick + 1
        time.sleep(1) # Read data every X seconds


# python /home/pi/Desktop/DHT_sensor.py
