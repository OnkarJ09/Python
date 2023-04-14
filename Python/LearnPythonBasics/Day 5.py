x = int(input("Enter the number:"))

match x:
    #x is the Varible to match 
    case 0:
        print('x is zero')
    case 4:
        print('x is four')
    case _ if x >= 5 and x <=10:
        print('greater then five')
    case _ if x != 5:
        print('five absent')
    case _:
        print(x)

for i in range(1,20001):
    print(i)

for i in range(1, 15, 3):
    print(i + 2)

count = 5
while (count > 0):
    print(count)
    count = count - 1

