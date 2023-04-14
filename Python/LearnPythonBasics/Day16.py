#                 Creating Parent Class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)


#use the Person class to create an object, and then execute it using printname method

x = Person("Onkar", "Joshi")
x.printname()

#               Creating Child Class

class Child(Person):
    #pass
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.gradduatiionyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.gradduatiionyear)
     
    #def printname(self):
        #print(self.firstname, self.lastname, self.gradduatiionyear)
       #Person.__init__(self, fname, lname)


x = Child("Takla", "Bro", 2023)
x.printname()
print(x.gradduatiionyear)
x.welcome()
