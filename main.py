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

#import sys
#import UI
import data

class Main:
    window = None
    s = None
    
    #TODO: Disable test when ready
    def __init__(self, window, test=True):
        print("Initialising UI...")
        self.window = window
        
        if not test:
            import dataStream as stream
            
            self.window.statusBar().showMessage("Opening connection to remote...", 2000)
            print("Opening connection to remote...")
            self.s = stream.DataStream()
        else:
            print('hello')
            import tester as t
            
            self.window.statusBar().showMessage("Opening tester data stream...", 2000)
            print("Opening tester data stream...")
            self.s = t.Tester()
            

    def main(self):
        
        temp_data = self.s.get_data()
        data.update_all(temp_data)
            
        self.arrays = data.get_arrays()
        self.window.altitude.update_figure()
        self.window.acceleration.update_figure()
        
        return

if __name__=='__main__':
    temp = Main()
    temp.main()