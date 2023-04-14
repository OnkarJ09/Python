adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]


for x in range(5):
    if x == 3: break
    print(x)
else:
    print("done")

print("success")

for x in adj:
    for y in fruits:
        print(x, y)

for x in [0, 1, 2]:
    pass



def myfunc():
    print("hello guys how are you")

myfunc()

def myfunc1(fname):
    print(fname + " hello")

myfunc1("hey")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)



x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b * a + b
print(x(5, 6))



