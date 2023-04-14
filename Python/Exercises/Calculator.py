import sys


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def calculator():
    operation = input("Which operation do you want to do?(+, -, *, /) or ()exit for exiting: ")
    if (operation == "q"):
        sys.exit()
    try:
        n1 = float(input("Enter the 1st number: "))
        n2 = float(input("Enter the 2nd number: "))
        if (operation == '+'):
            print(add(n1, n2))
        elif (operation == '-'):
            print(sub(n1, n2))
        elif (operation == '*'):
            print(mult(n1, n2))
        elif (operation == '/'):
            print(div(n1, n2))
    except:
        print("An error occured while runing the code")

def factorial(n):
    try:
        if (n==0 or n==1):
            return n
        else:
            return n * factorial(n-1)           
    except:
        print("Only integer/int are allowed")

def fibonacci(n):
    try:
        if (n==0):
            return 0
        elif (n==1):
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    except:
        print("Only integer/int are allowed")




class Calci():
    op = input("Which operation?(calculator(1), factorial(2) , fibonacci seq.(3): ")
    if (op=="1"):
        calculator()
        while True:
            calculator()
    elif (op=="2"):
        print(factorial(int(input("Enter the number of which you want the Factorial of: "))))
    else:
        print(fibonacci(int(input("Enter the number till which you want the Fibonacci series of: "))))


Calci()
     



