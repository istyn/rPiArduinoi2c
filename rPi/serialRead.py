import time
import serial

ser = serial.Serial("/dev/ttyAMA0",9600)
time.sleep(2)
while 1:
    print ser.readline()
