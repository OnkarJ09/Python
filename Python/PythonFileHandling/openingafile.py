#f = open("demofile.txt", "r")
#print(f.read())

#print(f.read(5))
#print(f.readline())
#print(f.readline())
#print(f.readline())

#for x in f:
#    print(x)


#print(f.readline())
#f.close()
#print(f.readline())

#f = open("demofile2.txt", "x")
#f = open("demofile2.txt", "a")
#f.write("\n Now the file has more contentdhsfnfjf")
#f.close()
#f = open("demofile2.txt", "r")
#print(f.read())



#f = open("myfile.txt", "w")


import os
#os.remove("demofile.txt")
#os.remove("myfile.txt") 

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("the file does not exist")
