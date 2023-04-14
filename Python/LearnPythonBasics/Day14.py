class Person1:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Son(Person1):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2023

x = Son("Mikel", "Jacken")
x.printname()

