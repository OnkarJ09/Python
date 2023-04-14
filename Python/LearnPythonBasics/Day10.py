thislist = ("apple", "banana", "cherry", "kiwi")
tuple1 = (131, 141, 14, 432, 4, 3, 5,2 ,25,242, 0)

#for x in thislist:
#    print(x)

#for i in range(len(thislist)):   
#   print(thislist[i])          #if we code "print(i)" insted of "print(thislist[i])"
#                               #then we get index of the tuple else we get the range

#i = 0
#while i < len(thislist):
#    print(thislist[i])
#    i = i + 1

##a = thislist + tuple1
#a = thislist * 2
#print(a)

#print(thislist.count("apple"))
#print(tuple1.index(5))


myset = {"apple", "banana", "chery", "kiwi", "apple", True, 1, 2, 3, 6, 0}
tropical = {"pineapple", "mango", "papaya", "apple"}


#print(myset)
#print(len(myset))
#print(type(myset))

#for x in myset:
#    print(x)

#print("banana" in myset)

#myset.add("orange")
#print(myset)

#myset.update(tropical)
#print(myset)
#print(tropical)

##myset.remove("banana")
#myset.discard("banana")
#print(myset)

#i = 0
#while i < len(myset):
#    print(myset[i])
#    i = i + 1

#myset.intersection_update(tropical)
#print(myset)

#z = myset.intersection(tropical)
#print(z)




thisdict = {"brand":"ford", 
            "model":"mustang gtr", 
            "year":2023
           }
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))

#x = thisdict.get("model")
#print(x)

x = thisdict.keys()
print(x)

thisdict["colour"] = "black"
print(x)

y = thisdict.values()
print(y)

z = thisdict.items()
print(z)


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
