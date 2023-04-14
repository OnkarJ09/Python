fruits = ["orange", "Apple", "pinEapple", "Kiwi", "banana", "Mango"]
thislist = [100, 212,34,54,4,56,56,67,7, 63630]
#fruits.sort(reverse = True)
#print(fruits)

#def myfunc(n):
#    return abs(n - 50)

##thislist = []
#thislist.sort(key = myfunc)
#print(thislist)


##fruits = ["orange", "Apple", "pinEapple", "Kiwi", "banana", "Mango"]
##fruits.sort(key = str.lower)
##print(fruits)

#fruits.reverse()
#print(fruits)

#mylist = thislist.copy()
#print(mylist)

#mylist = list(thislist)
#print(mylist)

#for x in thislist:
#    fruits.append(x)

#print(fruits)

#fruits.extend(thislist)
#print(fruits)



mytuple = ("orange", "Apple", "pinEapple", "Kiwi", "banana", "Mango")
print(mytuple)
print(len(mytuple))
print(mytuple)



tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
# res = tuple1.index(311)
# res = tuple1.index(3, 4, 8)
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)



import time
t = time.strftime('%H:%M:%S') 
hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))
# print(hour)

if(hour>=0 and hour<12):
  print("Good Morning Sir!")
elif(hour>=12 and hour<17):
  print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
  print("Good Night Sir!") 


x = ("apple", "kiwi", "banana")
print(x)
y = list(x)
y[1] = "cherry"
x = tuple(y)
print(x)
z = list(x)
z.append("cherry")
x = tuple(z)
print(z)

a = x + tuple1
print(a)


(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
