print("Hello World!")
print("To exit type exit.")
print("Type Hello or Test!")
print("")
x = input("#")
for i in range(2147000000):
    if x == "Hello":
        print("Hi!!!!")
        x = input("#")
    if x == "Test":
        print("THIS PROGRAM WORKS!!!!!")
        x = input("#")
    if x == "exit":
        with open("PyDos Beta 0.1.0.py") as file:
                exec(file.read())