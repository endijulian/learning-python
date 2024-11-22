class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# x = Person("Endi", "Julian")
# x.printname()

# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)

# x = Student("Mike", "Olsen")
# x.printname()



# Use the super() Function
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome, " + self.firstname + " " + self.lastname + " to the class", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
# print(x.graduationyear)
x.welcome()