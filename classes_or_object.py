# class MyClass:
#     x = 5

# # print(MyClass)
# p1 = MyClass()
# print(p1.x)


# The __init__() Function
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Jhon", 36)

# print(p1.name)
# print(p1.age)


# The __str__() Function
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
    
# p1 = Person("John", 36)
# print(p1)



# Object Methods
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myFunc(self):
#         print("Hello, my name is " + self.name)

# p1 = Person("John", 36)
# p1.myFunc()

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myFunc(abc):
        print("Hello, my name is " + abc.name)

p1 = Person("John", 36)
# p1.myFunc()
# p1.age = 40
del p1.age
print(p1.age)