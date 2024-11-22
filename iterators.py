# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# mystr = "banana"
# myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# mytuple = ("apple", "banana", "cherry")
# for x in mytuple:
#     print(x)


# mystr = "banana"
# for x in mystr:
#   print(x)

# class MyNumbers:
#     def __iter__(self):
#         self.n = 1
#         return self
    
#     def __next__(self):
#         x = self.n
#         self.n += 1
#         return x
    
# myClass = MyNumbers()
# myiter = iter(myClass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# StopIteration
class MyNumbers:
    def __iter__(self):
        self.n = 1
        return self
    
    def __next__(self):
        if self.n <= 20:
            x = self.n
            self.n += 1
            return x
        else:
            raise StopIteration("Iteration is over")
        
myClass = MyNumbers()
myiter = iter(myClass)

for x in myiter:
    print(x)