print("Welcome to CommandCalc for PyDos!")
print("MacGamer5250-2025 \n VERSION: BETA 1.0 \n Type exit to exit.")
print("      ")
for i in range(100000):
    operation = ()
    firstnumber = ()
    secondnumber = ()
    operation = (input("What operation do you want to do. Addition, subtracton, multiplication, or divison. (Note, for multiplication you need to, type \"*\", and for division you need to, type \"/\".)"))
    if(operation == "+"):
                 firstnumber = (input("What is your first addend?"))
                 secondnumber = (input("What is your second addend?"))
                 print(firstnumber,"+",secondnumber,"=",int(firstnumber) + int(secondnumber))
    if(operation == "-"):
                 firstnumber = (input("What is your minuend?"))
                 secondnumber = (input("What is your subtrahend?"))
                 print(firstnumber,"-",secondnumber,"=",int(firstnumber) - int(secondnumber))
    if(operation == "*"):
                 firstnumber = (input("What is your multiplicand?"))
                 secondnumber = (input("What is your multiplier?"))
                 print(firstnumber,"*",secondnumber,"=",int(firstnumber) * int(secondnumber))
    if(operation == "/"):
                 firstnumber = (input("What is your dividend?"))
                 secondnumber = (input("What is your divisor?"))
                 print(firstnumber,"/",secondnumber,"=",int(firstnumber) / int(secondnumber))
    if(operation == "exit"):
                  with open("PyDos Beta 0.1.0.py") as file:
                    exec(file.read())
    print("\n")





    

    


