b = 33
#b = 200
a = 330
c = 550



if b > a:
  print("b is greater than a")

if b > a:
    print("s")
elif a == b:
    print("n")
else:
    print("hi")

if a > b: print("a > b")             #This technique is known as Ternary Operators, 
                                           # or Conditional Expressions.
print("A") if a < b else print("B")

print("A") if a > b else print("=") if a == b else print("B")

if a > b and c > a:
  print("Both conditions are True")

if a > b or c < a:
    print("one of  them is true")

if not a < b:
    print("its not")

if a > 10:
    print("above ten")
    if a > 20:
        print("and also above 20")
    else:
        print("and also less then 20")

if a > b:
    pass

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print("i no longer exit")




