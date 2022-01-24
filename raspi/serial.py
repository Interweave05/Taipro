# -*- coding: UTF-8 -*-
# author: Interweave
# date: 2022.1.19 20:57
# email: interweave@qq.com

import serial  # import serial module


def connect_serial(data, timeout, frequency):
    ser = serial.Serial('/dev/ttyAMA0', frequency, timeout=timeout)
    ser

# while True:
#   ser.write('s'.encode())  # writ a string to port
#   response = ser.readall()  # read a string from port
#   print(response.decode())
