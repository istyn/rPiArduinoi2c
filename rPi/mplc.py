import matplotlib.pyplot as plt
import numpy as np
import serial

ser = serial.Serial('/dev/ttyAMA0',9600)
plt.ion() ## Note this correction
#fig=plt.figure()
#plt.axis([0,1000,0,1000])

i=0
x=list()
y=list()
seq=[]

while True:
    bytesToRead = ser.inWaiting()
    #bytesToRead.split(b'\n')
    for line in ser.read():
        seq.append(chr(line))#conv from ascii
        joined_seq = ''.join(str(v) for v in seq)

        if chr(c) == '\n':
            print joined_seq
            seq = []
            i += 1
            break

ser.close()
    #temp_y=ser.readline()
    #x.append(i)
    #y.append(temp_y)
    #plt.scatter(temp_y,temp_y)
    #i+=1
    #plt.show()
    #plt.pause(0.0001) #Note this correction
