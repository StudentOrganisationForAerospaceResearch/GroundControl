# -*- coding: utf-8 -*-
"""
Student Organisation for Aerospace Reasearch
University of Calgary
Canada

Developers:
    Robbie Ridgeway
    Nathan Meulenbroek
    
Description:

"""
# This is not a default module, make sure to install it!!!
import serial
import sys

class DataStream():
    """
    Maintains data received from the downlink.
    
    """
    ser = None
    
    def __init__(self):
        if sys.platform == 'win32':
            isWindows=True
        else:
            isWindows=False    
        
        if isWindows:      # This needs to be adjusted to the correct port name... []
            # Import msvcrt
            self.ser=serial.Serial('COM4',timeout=1)
        if not isWindows:
            # Import the linux version
            self.ser=serial.Serial('/dev/ttyUSB0')
        return None
    
    
    def getData(self):
        currentLine = self.ser.readline().rstrip()
  
        if len(currentLine) > 3 and currentLine[0] == '$' and currentLine[-1] == '*':
            currentLine = currentLine[1:-1]
            return currentLine

        else:
            return None