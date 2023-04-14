x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b * a + b
print(x(5, 6))

def myfunc(n):
    return lambda a: a * n 
#myfunc(6)
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

cars = ["Ford", "Volvo", "BMW"]

print(cars[0])
#print(cars[0])
cars[0] = "Toyota"
print(cars)

for x in cars:
    print(x)

cars.append('Audi')
print(cars)

#cars.pop(0)
#print(cars)

#cars.remove("Volvo")
#print(cars)

class Myclass:
    x = 5
print(Myclass)

obj = Myclass()
print(obj.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #def __str__(self):
    #    return f"{self.name} {self.age}"

    def myfunc(abc):
        print(("Hello my name is " + abc.name) + (" and my age is " + str(abc.age)))
p1 = Person("Onkar", 18)
p1.myfunc()

print(p1.name)
print(p1.age)
print(p1)


p1.age = 19
p1.myfunc()

#del p1.age
#p1.myfunc()


class Person1:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Son(Person1):
    pass
x = Son("Mikel", "Jacken")
x.printname()

