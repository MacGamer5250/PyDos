print("PyDos Command Prompt Beta 0.1.0")
print("MacGamer5250 - 2025")
def is_valid_input(input_string, valid_strings):
    return input_string not in valid_strings
import os
rootpath = (os.path.abspath(__file__))
rootpath = rootpath.replace('PyDos Beta 0.1.0.py', '')
allowed_commands = ("quit", "about", "comcalc", "clock", "help", "exec")
x = input("#")
for i in range(2147000000):
    if is_valid_input(x, allowed_commands):
       print("ERROR!\nINVALID SYNTAX!\nERROR!")
       x = input("#")
    else:
        if x == "quit":
            exit()
        if x == "help":
            print("Commands Page 1 of 2 \n help, opens this menu. \n about, shows the about menu. \n quit, quits the command line. \n exec, executes third party programs. \n comcalc, opens CommandCalc \n clockco, shows the current time")
            x = input("#")
        if x == "about":
            print("PyDos Command Prompt\nVersion Beta 0.1.0\nCoded By MacGamer5250 in 2025")
            x = input("#")
        if x == "exec":
            print("Program file name. (*.py)")
            e = input("$") 
            print("Loading",e,"...")
            with open(e) as file:
                exec(file.read())
        
        if x == "comcalc":
            print("Loading CommandCalc...")
            with open("ComCalc0.1.0b.py") as file:
                exec(file.read())
        if x == "clock":
            from datetime import datetime
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)
            x = input("#")
    
   
