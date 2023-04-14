#try:
#    print(x)
#except:
#    print("An exception occured")


#try:
#    print(x)
#except NameError:
#    print("Variable not defined")
#except:
#    print("Something else went wrong") 



try:
    print("Hello")
except NameError:
    print("Variable not defined")
except:
    print("Something else went wrong")
else:
    print("Hi!,How are you?")
    



try:
    print(x)
except:
    print("Something else went wrong")
else:
    print("Hi!,How are you?")
finally:
    print("The 'Try Except' is over😊")



try:
    f = open("demofile.txt")
    try:
        f.write("Onkar Joshi")
    except:
        print("Something went wrong while writing")
    finally:
        f.close()
except:
    print("Something went wrong while opening the file")




#x = -1
#if x < 0:
#    raise Exception("Sorry,!!")

x = 9
if not type(x) is str:
    raise Exception("only string allowed")


