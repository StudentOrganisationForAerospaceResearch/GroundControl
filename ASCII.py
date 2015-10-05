"""
2015/XX/XX

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
This part of the game is in charge of simply being called by the GUI.py to print out ASCII (Due to Windows overwriting UTF-8 ASCII the need for this file exists)
"""


def printOutASCII():
    asciiIntro = ("Welcome to" + "\n" +
    """
      ___                    _ 
     | _ \_____ _____ _ _ __(_)
     |   / -_) V / -_) '_(_-< |
     |_|_\___|\_/\___|_| /__/_|
                               
    """ + "\n" +
    "In this game you will be able to..." + "\n" +
    """
      _____                                   _   _    _           
     |_   _|  _ _ __  ___   ___ ___ _ __  ___| |_| |_ (_)_ _  __ _ 
       | || || | '_ \/ -_) (_-</ _ \ '  \/ -_)  _| ' \| | ' \/ _` |
       |_| \_, | .__/\___| /__/\___/_|_|_\___|\__|_||_|_|_||_\__, |
           |__/|_|                                           |___/ 
    """+ "\n" +
    "You will eventually be able to click on the tile where you want to play your piece, " + "\n" +
    "but for now, please input coordinates. The point of the game is as follows:"+ "\n" +
    """
       ___     _                                     ___ _               
      / __|___| |_   __ _ ___  _ __  __ _ _ _ _  _  | _ (_)___ __ ___ ___
     | (_ / -_)  _| / _` (_-< | '  \/ _` | ' \ || | |  _/ / -_) _/ -_|_-<
      \___\___|\__| \__,_/__/ |_|_|_\__,_|_||_\_, | |_| |_\___\__\___/__/
                                              |__/                       
                                _ _    _     
      __ _ ___  _ __  ___ _____(_) |__| |___ 
     / _` (_-< | '_ \/ _ (_-<_-< | '_ \ / -_)
     \__,_/__/ | .__/\___/__/__/_|_.__/_\___|
               |_|                           
      ___                                   _              
     |_ _|_ _    _  _ ___ _  _ _ _   __ ___| |___ _  _ _ _ 
      | || ' \  | || / _ \ || | '_| / _/ _ \ / _ \ || | '_|
     |___|_||_|  \_, \___/\_,_|_|   \__\___/_\___/\_,_|_|  
                 |__/                                      
    """)
    return asciiIntro

