# -*- coding: utf-8 -*-
"""
Student Organisation for Aerospace Reasearch
University of Calgary
Canada

Developers:
    Nathan Meulenbroek
    
Description:
    Tester file. Gives bogus data to the main file to run algorithm tests
"""
import random

class Tester():
    """
    Very much overengineered to support future improvements.
    """
    altitude = 0.0
    pressure = 0.0
    acceleration_x = 0.0
    acceleration_y = 0.0
    acceleration_z = 0.0
    ang_acceleration_x = 0.0
    ang_acceleration_y = 0.0
    ang_acceleration_z = 0.0
    magnetic_field_x = 0.0
    magnetic_field_y = 0.0
    magnetic_field_z = 0.0
    pitch = 0.0
    yaw = 0.0
    roll = 0.0
    temperature = 0.0
    
    def __init__(self, *args, **kwargs):
        return
    
    def get_data(self):
        self.altitude = random.randrange(0, 30, 1)
        self.pressure = random.randrange(0, 30, 1)
        self.acceleration_x = random.randrange(0, 30, 1)
        self.acceleration_y = random.randrange(0, 30, 1)
        self.acceleration_z = random.randrange(0, 30, 1)
        self.ang_acceleration_x = random.randrange(0, 30, 1)
        self.ang_acceleration_y = random.randrange(0, 30, 1)
        self.ang_acceleration_z = random.randrange(0, 30, 1)
        self.magnetic_field_x = random.randrange(0, 30, 1)
        self.magnetic_field_y = random.randrange(0, 30, 1)
        self.magnetic_field_z = random.randrange(0, 30, 1)
        self.pitch = random.randrange(0, 30, 1)
        self.yaw = random.randrange(0, 30, 1)
        self.roll = random.randrange(0, 30, 1)
        self.temperature = random.randrange(0, 30, 1)

        return ("$"+str(self.altitude) + '|' + str(self.pressure) + '|' + 
                str(self.acceleration_x) + '|' + str(self.acceleration_y) + '|' 
                + str(self.acceleration_z) + '|' + str(self.ang_acceleration_x)
                + '|' + str(self.ang_acceleration_y) + '|' + 
                str(self.ang_acceleration_z) + '|' + str(self.magnetic_field_x)
                + '|' + str(self.magnetic_field_y) + '|' + 
                str(self.magnetic_field_z) + '|' + str(self.pitch) + '|' + 
                str(self.yaw) + '|' + str(self.roll) + '|' + 
                str(self.temperature)+"*")
   
def __init__():
    temp = Tester()
    
    for i in range(10):
        print(temp.get_data())
        
    return