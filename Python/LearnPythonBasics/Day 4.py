#################### DAY 1 ###########################

print('Hello World!')
print('5')

#################### DAY 2 ###########################



if 5 > 2:
    print('Hiiii')
    print('Hello')


x='Hiii'  # Variables
y='Bye'   # Variables
print(x) 
print(y)


# how are you?
print(x)
"""
This is a comment
written in multi-Line
more Line
"""


a="Onkar"
b="Joshi"
c="D."
print(a)
print(b)
print(c)
c=5
d="Hiiii"
e=5.00
print(c)
print(d)
print(e)
print(type(c))
print(type(d))
print(type(e))

############################# DAY 3 ####################################



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


############################# DAY 4 ############################


a=""" Hey bro how are u
I am in Nag,
where r u {} """
b=38
print(a)
print(a[2])
print(a[1])                                                                        
print(a[5])


for x in "BANANNA":
    print(x)


print(len(a))


print("Nag" in a)
if "Nag" in a:
    print("Yes present")
if "u" in a:
    print('yes')
else:
    print('no')


print(a[5:10])
print(a[:10])
print(a[5:])
print(a[-6:-9])


print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace('h', 'j'))
print(a.split(','))


print(a.format(b))

c='Hiiiii'
print(c.center(40))
print(len(c))
print(c.center(40, "#"))

