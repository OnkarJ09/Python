mytuple = ("apple", "banana", "cherry")
mystr = "banana"
myit = iter(mystr)

#print(next(myit))
#print(next(myit))
#print(next(myit))
#print(next(myit))
#print(next(myit))
#print(next(myit))


for x in mytuple:
    print(x)

for x in mystr:
    print(x)



class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
           x = self.a
           self.a += 1
           return x
        else:
            raise StopIteration


#myclass = MyNumbers()
#myiter = iter(myclass)

#for x in myiter:
#    print(x)

#print(next(myiter))
#print(next(myiter))
#print(next(myiter))
#print(next(myiter))
#print(next(myiter))
#print(next(myiter))

def myfunc():
    x = 300
    #print(x)
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

x = 400

def myfunc():
    #global x
    x = 13
    print(x)
myfunc()

print(x)



from moduleslearning import greetuser as gu

gu.greeting("Onkar")

print(gu.person1["age"])

import platform
print(platform.system())
#print(dir(platform))
print(dir(gu))

import datetime
print(datetime.datetime.now())
x = datetime.datetime.now()
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%d:%m:%Y"))


from moduleslearning import greetuser as gu
print(gu.a)
