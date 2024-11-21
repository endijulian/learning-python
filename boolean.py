# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# a = 200
# b = 33
# if b > a:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")

# print(bool("Hello"))
# print(bool(15))

# x = "Hello"
# y = 15
# x = ""
# y = 0

# print(bool(x))
# print(bool(y))

# print(bool("abc"))
# print(bool(123))
# print(bool(["apple", "cherry", "banana"]))

# Nilai yang bernilai FALSE
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myClass():
    def __len__(self):
        return 0
    
myobj = myClass()
print("Ini adalah", bool(myobj))

def myFunction():
    return True

print("Ini adalah nilai function", myFunction())


def myFunction2():
    return True

if myFunction2():
    print("YES!")
else:
    print("NO!")


x = 200
print(isinstance(x, int))