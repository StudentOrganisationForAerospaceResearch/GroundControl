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
#from threading import Thread
import data
from PyQt5.QtCore import QThread

class Main(QThread):
    window = None
    s = None
    data_recorder = None
    
    #TODO: Disable test when ready
    def __init__(self, window, test=True):
        QThread.__init__(self)
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
    
    def __del__(self):
        self.wait()
            
    def run(self):
        print("Main loop started...")
        while True:
            temp_data = self.s.get_data()
            print(temp_data)
            self.data_recorder.update_all(temp_data)
                
            arrays = self.data_recorder.get_arrays()
            
            self.window.altitude.update_figure(arrays[0])
            self.window.acceleration.update_figure(arrays[1])
            self.window.IMU.update_figure(arrays[2])
            self.window.gyro.update_figure(arrays[3])
            self.window.diode.update_figure(arrays[4])
            self.window.text_boxes.updateText()

            self.window.repaint()
        
        return

if __name__=='__main__':
    
    aw, qApp = UI.__init__()
    thread = Main(aw)
    print("Initialising backend...")
    thread.start()
    
    print("Initialising UI...")
    sys.exit(qApp.exec_())
    
    
    print("Done.")

