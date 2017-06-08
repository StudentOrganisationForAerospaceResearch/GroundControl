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
        count = 0
        while True:
            temp_data = self.s.get_data()
            #print(temp_data) #Enable this for debugging
            self.data_recorder.update_all(temp_data)
                
            arrays = self.data_recorder.get_arrays()
            
            self.window.altitude.update_figure(((arrays[0][-200:],'Altitude'),))
            self.window.acceleration.update_figure(((arrays[2][-200:],'Accel-x'),
                                                    (arrays[3][-200:],'Accel-y'),
                                                    (arrays[4][-200:],'Accel-z')))
            self.window.gyro.update_figure(((arrays[5][-200:],'Ang Accel-x'),
                                            (arrays[6][-200:],'Ang Accel-y'),
                                            (arrays[7][-200:],'Ang Accel-z')))
            self.window.mag.update_figure(((arrays[8][-200:],'Mag-x'),
                                           (arrays[9][-200:],'Mag-y'),
                                           (arrays[10][-200:],'Mag-z')))
            
            self.window.IMU.update_figure(((arrays[11][-200:],'Pitch'),
                                            (arrays[12][-200:],'Yaw'),
                                            (arrays[13][-200:],'Roll')))
            self.window.text_boxes.updateText()
            
            #******DO NOT REMOVE*****
            # This code forces a refresh of the interface to prevent the gui
            # from appearing to freeze. If this is removed, the window will
            # stop updating at random intervals
            count += 1
            if (count == 8):
                count = 0
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

