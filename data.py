# -*- coding: utf-8 -*-
"""
Student Organisation for Aerospace Reasearch
University of Calgary
Canada

Developers:
    Nathan Meulenbroek
    
Description:

"""
import datetime
from tkinter import *
from tkinter.filedialog import askopenfilename

class Data():
    """
    Data from rocket.
    
    """
    data_file = ''
    altitude = []
    pressure = []
    acceleration = []
    ang_acceleration = []
    magnetic_field = []
    pitch = []
    yaw = []
    roll = []
    temperature = []
    
    def __init__(self):
        self.data_file = open('data_file.txt', 'w')
        
        self.data_file.write('# Data file initialised: %s' % datetime.datetime.now() + '\n#\n')
        
        self.data_file.write("""
# This data file is free to use for the general public. All data found in this 
# file is raw data from the rocket. If there was no data available from the
# sensors when the rocket was attempting to send the data, the data received
# is repeated from the last measurement. The pitch, roll and yaw columns were
# all calculated on board the rocket from the magnetometer, gyroscope and 
# accelerometer data.
#
# Sensors were calibrated at the time when the first data was received.
#
# Units: 
# 
                             """)
        return
    
    def update_all(self, data):
        """
        Updates all data at once
        
        Params:
            data - (string) data, separated with vertical lines
        """
        
        self.data_file.write('%s' % datetime.datetime.now())
        
        for item in data:
            self.data_file.write('{:30}'.format(item))
        
        self.data_file.write('\n')
        
        
        self.altitude.append(data[0])
        self.pressure.append(data[1])
        self.acceleration.append(data[2])
        self.ang_acceleration.append(data[3])
        self.magnetic_field.append(data[4])
        self.pitch.append(data[5])
        self.yaw.append(data[6])
        self.roll.append(data[7])
        self.temperature.append(data[8])
        
        return 

#Preliminary file reading function???
#Not really clear on what we're doing
#Authors: John and Courtney
#Status: Confused
	def getData(self):
		root = Tk()
		root.filename =  askopenfilename(initialdir = "E:/Images",title = "choose your file",filetypes = (("Text Files","*.txt"),("all files","*.*")))
		fileName = root.filename
		root.withdraw()
		textFile = open(fileName, "r")
		data = textFile.read()
		return data	
		
		