def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def calculator():
    operation = input("Which operation do you want to do?(+, -, *, /): ")
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
calculator()

while True:
    calculator()

