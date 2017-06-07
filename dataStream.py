# -*- coding: utf-8 -*-
"""
Student Organisation for Aerospace Reasearch
University of Calgary
Canada

Developers:
    Nathan Meulenbroek
    
Description:

"""

class DataStream():
    """
    Maintains data received from the downlink.
    
    """
    
    def __init__(self):
        #TODO: Initialise data stream
        
        if sys.platform == 'win32':
            isWindows=True
        else:
            isWindows=False    
        
        #if isWindows:      # This needs to be adjusted to the correct port name... []
        #    import msvcrt
        #    ser=serial.Serial('COM4',timeout=1)
        #if not isWindows:
        #    # Import the linux version
        #    self.ser=serial.Serial('/dev/ttyUSB0')
        return None
    
    
    def getData(self):
        currentLine = ser.readline().rstrip()
  
        if len(currentLine) > 3 and currentLine[0] == '$' and currentLine[-1] == '*':
            currentLine = currentLine[1:-1]
            return currentLine

        else:
            return None