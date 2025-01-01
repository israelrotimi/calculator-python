# A calculator implemented in python
# TODO:
#  Define functions to carry out Arith. ops
#   Collect input
#   Display output

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
# I/O: Implement a program display loop 
keep_running = True
print("Basic Calculator")
while keep_running:
    operation = input("What do you want to do?, type +, -, x, / ")
    if operation == "+":
        first_num = input("Enter first number: ")
        sec_num = input("Enter second number: ")
        print("result is: ", add(first_num, sec_num))
    if operation == "-":
        first_num = input("Enter first number: ")
        sec_num = input("Enter second number: ")
        print("Result is: ", subtract(first_num, sec_num))
    if operation == "x":
        first_num = input("Enter first number: ")
        sec_num = input("Enter first number: ")
        print("Result is: ", multiply(first_num, sec_num))
    if operation == "/":
        first_num = input("Enter first number: ")
        sec_num = input("Enter second number: ")
        print("Result is: ", divide(first_num, sec_num))
