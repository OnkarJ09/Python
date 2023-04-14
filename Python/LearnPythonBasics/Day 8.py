l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
# l.append(7)
# l.sort(reverse=True)
# l.reverse()
# print(l.index(1))
# print(l.count(1))
# m = l.copy()
# m[0] = 0
# l.insert(1, 899)
#m = [900, 1000, 1100]
#k = l + m
## print(k)
## l.extend(m)
#print(l)


#tup = (1, 2, 76, 342, 32, "green", True)
## tup[0] = 90
#print(type(tup), tup)
#print(len(tup))
#print(tup[0])
#print(tup[-1])
#print(tup[2])
## print(tup[34])

#if  3421 in tup:
#  print("Yes 342 is present in this tuple")
#tup2 = tup[1:4]
#print(tup2)



fruits = ["apple", "banana", "cherry", "kiwi", "mango", "pineapple"]
print(fruits)
#newlist = []

#for x in fruits:
#    if "a" in x:
#        newlist.append(x)

#print(newlist)

#
#print(newlist)
#newlist = [x for x in fruits if x != "apple"]
#newlist = [x for x in fruits]
#newlist = [x for x in range(10) if x < 6]
#print(newlist)

#newlist = ["hello" for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
