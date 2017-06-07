# -*- coding: utf-8 -*-
"""
Student Organisation for Aerospace Reasearch
University of Calgary
Canada

Developers:
    Nathan Meulenbroek
    John and Courtney
    
Description:

"""
import datetime
from tkinter.filedialog import askopenfilename
import numpy as np

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
        self.data_file = open('data_file.txt', 'w+')
        
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
#
# Columns in order w/(units): 
                             """)
        return
    
    def update_all(self, data_string):
        """
        Updates all data at once
        
        Params:
            data_string - (string) data, separated with vertical lines
        """
        data = data_string.split('|')
        self.data_file.write('%s' % datetime.datetime.now())
        
        for item in data:
            self.data_file.write('{:30}'.format(item))
        
        self.data_file.write('    %s' % datetime.datetime.now())
        self.data_file.write('\n')
        
        
        self.altitude.append(data[0])
        self.pressure.append(data[1])
        self.acceleration_x.append(data[2])
        self.acceleration_y.append(data[3])
        self.acceleration_z.append(data[4])
        self.ang_acceleration_x.append(data[5])
        self.ang_acceleration_y.append(data[6])
        self.ang_acceleration_z.append(data[7])
        self.magnetic_field_x.append(data[8])
        self.magnetic_field_y.append(data[9])
        self.magnetic_field_z.append(data[10])
        self.pitch.append(data[11])
        self.yaw.append(data[12])
        self.roll.append(data[13])
        self.temperature.append(data[14])
        
        return 

    def get_arrays(self):        
        return (self.altitude, self.pressure, self.acceleration_x, 
                self.acceleration_y, self.acceleration_z, 
                self.ang_acceleration_x, self.ang_acceleration_y, 
                self.ang_acceleration_z, self.magnetic_field_x,
                self.magnetic_field_y, self.magnetic_field_z,
                self.pitch, self.yaw, self.roll, self.temperature)
        
    def read_file(self):
        """
        Opens a gui asking for a text file to read, then sets
        this object's attributes to the data within this text file.
        This function assumes the data in the text file is properly
        formatted for this method to read; if it is not, it can cause a
        runtime error
        """
        
		 #Opens a gui asking for the file to read.
        fileName = askopenfilename(initialdir = "C:/",title = "choose your file",filetypes = (("Text Files","*.txt"),("all files","*.*")))
		 #Reads this file, then assigns the values found in this file to this object's attributes.
        data = np.genfromtxt(fname = fileName, dtype = "float", delimiter = "	")
        self.altitude = [data[0]]
        self.pressure = [data[1]]
        self.acceleration_x = [data[2]]
        self.acceleration_y = [data[3]]
        self.acceleration_z = [data[4]]
        self.ang_acceleration_x = [data[5]]
        self.ang_acceleration_y = [data[6]]
        self.ang_acceleration_z = [data[7]]
        self.magnetic_field_x = [data[8]]
        self.magnetic_field_y = [data[9]]
        self.magnetic_field_z = [data[10]]
        self.pitch = [data[11]]
        self.yaw = [data[12]]
        self.roll = [data[13]]
        self.temperature = [data[14]]
        
        return
