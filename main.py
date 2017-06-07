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
import data
import tester
from PyQt5 import QtCore, QtWidgets, QtGui

class Main:
    window = None
    s = None
    
    #TODO: Disable test when ready
    def __init__(self, window, test=True):
        print("Initialising UI...")
        self.window = UI.__init__()

        
        if not test:
            import dataStream as stream
            
            self.window.statusBar().showMessage("Opening connection to remote...", 2000)
            print("Opening connection to remote...")
            s = stream.DataStream()
        else:
            print('hello')
            
            self.window.statusBar().showMessage("Opening tester data stream...", 2000)
            print("Opening tester data stream...")
          
            

    def main(self):
        
        temp_data = tester.Tester.get_data(tester.Tester)
        data.Data.update_all(data.Data,temp_data)
            
        self.arrays = data.Data.get_arrays(data.Data)

        
        return

if __name__=='__main__':
    temp = Main(Main.window)
    temp.main()