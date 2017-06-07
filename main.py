# -*- coding: utf-8 -*-
"""
Student Organisation for Aerospace Reasearch
University of Calgary
Canada

Developers:
    Nathan Meulenbroek
    
Description:
    Main file. Run this to run the program.
"""

import sys
import UI
from threading import Thread
import data

class Main:
    window = None
    s = None
    data_recorder = None
    
    #TODO: Disable test when ready
    def __init__(self, window, test=True):
        self.window = window
        
        if not test:
            import dataStream as stream
            
            self.window.statusBar().showMessage("Opening connection to remote...", 2000)
            print("Opening connection to remote...")
            self.s = stream.DataStream()
        else:
            import tester as t
            
            self.window.statusBar().showMessage("Opening tester data stream...", 2000)
            print("Opening tester data stream...")
            self.s = t.Tester()
            
        self.data_recorder = data.Data()
        return
            

    def main_loop(self):
        print("Main Loop Started")
        while True:
            temp_data = self.s.get_data()
            print(temp_data)
            self.data_recorder.update_all(temp_data)
                
            self.arrays = self.data_recorder.get_arrays()
            self.window.altitude.update_figure()
            self.window.acceleration.update_figure()
            self.window.IMU.update_figure()
            self.window.gyro.update_figure()
            self.window.diode.update_figure()
        
        return

if __name__=='__main__':
    
    aw, qApp = UI.__init__()
    temp = Main(aw)
    
    t = Thread(target=temp.main_loop)
    print("Initialising backend...")
    t.daemon = True
    t.start()
    
    print("Initialising UI...")
    sys.exit(qApp.exec_())
    
    
    print("Done.")

