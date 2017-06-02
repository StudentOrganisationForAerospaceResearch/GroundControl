# -*- coding: utf-8 -*-
"""
Student Organisation for Aerospace Reasearch
University of Calgary
Canada

Developers:
    Nathan Meulenbroek
    
Description:

"""
import random
import datetime
from tkinter.filedialog import askopenfilename

class Data():
    """
    Data from rocket.
    
    """
    data_file = ''
    altitude = []
    pressure = []
    acceleration_x = []
    acceleration_y = []
    acceleration_z = []
    ang_acceleration_x = []
    ang_acceleration_y = []
    ang_acceleration_z = []
    magnetic_field_x = []
    magnetic_field_y = []
    magnetic_field_z = []
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

    def get_data(self):
        self.altitude.append(random.randrange(0, 30, 1))
        self.pressure.append(random.randrange(0, 30, 1))
        self.acceleration_x.append(random.randrange(0, 30, 1))
        self.acceleration_y.append(random.randrange(0, 30, 1))
        self.acceleration_z.append(random.randrange(0, 30, 1))
        self.ang_acceleration_x.append(random.randrange(0, 30, 1))
        self.ang_acceleration_y.append(random.randrange(0, 30, 1))
        self.ang_acceleration_z.append(random.randrange(0, 30, 1))
        self.magnetic_field_x.append(random.randrange(0, 30, 1))
        self.magnetic_field_y.append(random.randrange(0, 30, 1))
        self.magnetic_field_z.append(random.randrange(0, 30, 1))
        self.pitch.append(random.randrange(0, 30, 1))
        self.yaw.append(random.randrange(0, 30, 1))
        self.roll.append(random.randrange(0, 30, 1))
        self.temperature.append(random.randrange(0, 30, 1))
        
        return (self.altitude, self.pressure, self.acceleration_x, 
                self.acceleration_y, self.acceleration_z, 
                self.ang_acceleration_x, self.ang_acceleration_y, 
                self.ang_acceleration_z, self.magnetic_field_x,
                self.magnetic_field_y, self.magnetic_field_z,
                self.pitch, self.yaw, self.roll, self.temperature)
        
#Preliminary file reading function???
#Not really clear on what we're doing
#Authors: John and Courtney
#Status: Confused
    def read_file(self):
        #Removed unnessesary method calls
        
        #This method call will open up a dialog which will ask for the location of the file to be imported
        fileName =  askopenfilename(initialdir = "E:/Images",
                                    title = "choose your file",
                                    filetypes = (("Text Files","*.txt"),
                                                 ("all files","*.*")))
        
        textFile = open(fileName, "r") #this opens the file
        data = textFile.read() #this reads the first line of the file and then doesn't 
        
        # What still needs to happen is tha tyou import the file specified, and then assign all of the arrays above.
        # You can use the method call I sent you in the sample code on slack to get the data from the file.
        # The method call will parse all of the columns as arrays, which you can then throw into the respective variables.
        # Assume that the data will be in the same order as above (so column 1 would be Altitude and so on)
        
        return data	
		
		