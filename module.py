# import mymodule
import mymodule as mx
import platform
from mymodule import person1

mx.greeting("Jonathan")

a = mx.person1["age"]
print(a)

x = platform.system()
y = platform.processor()
print(x)
print(y)

z = dir(platform)
print(z)

print(person1["age"])