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



def main(test=False):
    if not test:
        import dataStream as stream
        
        print("Opening connection to remote...")
        s = stream.DataStream()
    else:
        import tester
        
        print("Opening tester data stream...")
        s = tester.start()
    
    print("Initialising UI...")
    UI.__init__()
    
    
    while True:
        temp_data = s.get_data()
        data.update_all(temp_data)
        
    
    return

if __name__=='__main__':
    main(sys.argv[1])