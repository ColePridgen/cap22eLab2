# %% This file will be used to demostrate basic python concepts. From types to loops, functions, classes, etc.

# Python types
myint = 7
print(myint)
print(type(myint))

myfloat = 7.0
print(myfloat)
print(type(myfloat))

mystring = 'Hello'
print(mystring)
print(type(mystring))

mylist = [1, 2, 3]
print(mylist)
print(type(mylist))

mydict = {'a': 3, 'b': 2}
print(mydict)
print(type(mydict))
print(mydict['a'])

# %% Difference between lists and tuples
# Lists are mutable, tuples are not
mylist = [1, 2, 3]
mylist[0] = 4
print(mylist)

# %%
mytuple = (1, 2, 3)
mytuple[0] = 4 # This will raise an error

# %% Loops
# For loop
for i in range(1, 5, 2):
    print(i)


# Enumerate from a dictionary
mydict = {'a': 3, 'b': 2}
for key, value in mydict.items():
    print(key, value)

# While loop
i = 0
while i < 5:
    print(i)
    i += 1

# %% Functions
def myfunc(a, b):
    return a + b

print(myfunc(1, 2))

# %% Default arguments
def myfunc(a, b=2):
    return a + b

print(myfunc(1))
print(myfunc(1, 3))

# %% Functions defining argument types
def myfunc(a: int, b: int) -> int:
    return a + b

print(myfunc(1, 2))
print(myfunc('a', 'b')) # This will raise an error

# %% Additional arguments
def myfunc(*args):
    return sum(args)

print(myfunc(1, 2, 3))

# %% Additional arguments with key value pairs
def myfuncinernal(a = 1, b = 2):
    return a + b

def myfunc(**kwargs):
    return myfuncinernal(**kwargs)

print(myfunc(a=1, b=2, c=3))

# %% Classes
# Make a class dog that can barks
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f'Woof! my name is {self.name}'

mydog = Dog('Buddy')
print(mydog.bark())
mydogmish = Dog('Mish')
print(mydogmish.bark())

# %% Exceptions
try:
    print("Hello")
    print(1/1)
    print("World")
except ZeroDivisionError:
    print('Cannot divide by zero')
finally:
    print('This will always run')
    