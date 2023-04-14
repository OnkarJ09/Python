#def hello(n):
#    '''Hiii How are you'''
#    print(n**3)
#hello(12)
#print(hello.__doc__)


def factorial(n):                         #This is a function that find's the factorial of the given number.
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(999))


def fibonacci(n):                       #This is a function that find's the fibonacci series of the given number.
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))


