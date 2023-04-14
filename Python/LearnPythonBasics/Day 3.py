from string import ascii_lowercase


x, y, z = "Hey", "How", "Are"
print(x)
print(y)
print(z)
print(x, y, z)
a=b=c='Hiiiiiiiiiiiii'
print(a,b,c)

fruits=['hiiii','hello','abe']              # This is Unpacking 
x,y,z=fruits                                # Tuple Unpacking
print(x,y,z)

print(x + y + z)

a=5345
b=453455
print(a+b)
print(a-b)
print(a*b)
print(a/b)


def myfunc():
    print('Python is '+x)

myfunc()

x='awesome'

def myfunc():
    global x
    x='fantastic'
    print('Python is '+x)
myfunc()
print('Python is '+x)

d=5j
print(type(d))


import random

e=random.randrange(1,10)
print(e)
###how 
###are 
###you

print("Hello World!")
