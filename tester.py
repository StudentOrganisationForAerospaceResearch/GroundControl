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
    
    def __init__(self, *args, **kwargs):
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
   
def __init__():
    temp = Tester()
    
    for i in range(10):
        print(temp.get_data())
        
    return
        
if __name__=='__main__':
    __init__()