#!/bin/python

###############################################################################
# Description
# 
# Ground control software for June 17 - 18 Student Rocket Launch
# Parse downlink strings and send uplink commands.
# Matthew Patrick
# June 11, 2016


# Modified by Robbie Ridgway
# June 7th, 2017
# There is no checksum or error correction.



# This is not a default module, make sure to install it!!!
import serial



import sys
import os
import matplotlib.pyplot as plt
import time



print('Opening Serial Port...')
if sys.platform == 'win32':
    isWindows=True
else:
    isWindows=False    
#if isWindows:      # This needs to be adjusted to the correct port name... []
#    import msvcrt
#    ser=serial.Serial('COM4',timeout=1)
#if not isWindows:
#    # Import the linux version
#    ser=serial.Serial('/dev/ttyUSB0')
#    pass
print('Opening Serial Port...')
print('Serial Port Opened.')

import numpy as np
class DataStream():
    def __init__(self):

        self.Altitude=[]
        self.Temperature=[]
        self.Pressure=[]
        self.AccelerationX=[]
        self.AccelerationZ=[]
        self.AccelerationY=[]
        self.AngAccelerationX=[]
        self.AngAccelerationZ=[]
        self.AngAccelerationY=[]
        self.MagX=[]
        self.MagY=[]
        self.MagZ=[]
        self.Pitch=[]
        self.Yaw=[]
        self.Roll=[]
        
        self.filename='Data_MASTER.npy'
        return None
    
    #Takes in a working line with the control characters removed
    def Update(self,line):
        self.Altitude.append(float(line[0]))
        self.Pressure.append(float(line[1]))
        
        self.AccelerationX.append(float(line[2]))
        self.AccelerationY.append(float(line[3]))
        self.AccelerationZ.append(float(line[4]))
        
        self.AngAccelerationX.append(float(line[5]))
        self.AngAccelerationY.append(float(line[6]))
        self.AngAccelerationZ.append(float(line[7]))
        
        self.MagX.append(float(line[8]))
        self.MagY.append(float(line[9]))
        self.MagZ.append(float(line[10]))

        self.Pitch.append(float(line[11]))
        self.Yaw.append(float(line[12]))
        self.Roll.append(float(line[13]))
        self.Temperature.append(float(line[14]))
        return None

    def DataSave(self):
        arr=np.array([self.Altitude,self.Temperature,self.Pressure,
                      self.AccelerationX,self.AccelerationY,self.AccelerationZ,
                      self.AngAccelerationX,self.AngAccelerationY,
                      self.AngAccelerationZ,self.MagX,self.MagY,self.MagZ,
                      self.Pitch, self.Yaw, self.Roll])
        np.save(self.filename,arr)
        
        return None

isThisaTest=True
if isThisaTest:
    print('THIS IS A TEST')
    
def tester():
    q=np.random.rand(1)
    if q[0] < 0.01:
        string='$iuhoihj9oij*'
        return string
    arr=np.random.rand(15)
    string='$'
    for elem in arr:
        string+=str(elem)+'|'
    
    string=string[:-1]+'*'
    return string

Data=DataStream()
count= 0
while True and count < 1e4:
    #os.system('clear')
    print(count)
    if isThisaTest:
        currentLine=tester()
    else:
        pass
        #currentLine = ser.readline().rstrip()
  
    if len(currentLine) > 3 and currentLine[0] == '$' and currentLine[-1] == '*':
        currentLine = currentLine[1:-1]
        try:
            line = currentLine.split('|')
            
        except:
            print('Got a malformed telemetry line. Skipping...')
            next

        try:
            Data.Update(line)
        except:
            print('Failed to parse line. Skipping...')

        count+=1
        
        if len(Data.Altitude) % 1000 == 0:
            Data.DataSave()
        
import matplotlib.pyplot as plt
plt.plot(Data.Altitude)
plt.show()



