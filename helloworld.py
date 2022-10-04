import random
print("Hello World!")

if 5 > 2:
    print("Five is greater than two!")
    # print("Five is greater than two!")
#    Commening
"""
    please bare it
    it is not my problem
    """
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

x = 5
y = "Jane"
print(y)
print(x)

x = 40
x = "Kim"
print(x)

# Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

# Type of Variable
x = 5
y = "John"
print(type(x))
print(type(y))

# Single or double Quote
x = 'Joan'
y = "Jon"
print(x)
print(y)
if x == y:
    print("The name is Joan")

# Case sensitive
a = 4
A = "Sally"
# A will not overwrite a. Python is case sensitive
print(a)
print(A)

# Variable naming
myvar = "James"
my_var = "James"
MyVar = "James"
_my_var = "James"
myVar = "James"
myVAR = "James"
myvar2 = "James"
MYVAR = "James"

print(myvar)
print(my_var)
print(MyVar)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
print(myVAR)

# Variable Casing
# Camel Case
myVariableName = "Joan"
print(myVariableName)
# Pascal Case
MyVariableName = "Joan"
print(MyVariableName)
# Snake Case
my_variable_name = "Joan"
print(my_variable_name)

# Assigning multiple values
x, y, z = 'Joan', 'Cynthia', 'Kuria'
print(x)
print(y)
print(z)

# Assigning one value to multiple variables
x = y = z = "Cynthia"
print(x)
print(y)
print(z)

# Unpackin
fruits = ['apples', 'bananas', 'cherries']
x, y, z = fruits
print(x)
print(y)
print(z)

# print function
x = ("Python is amazing")
print(x)

# mulitple outputs
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# + operator without space (Pythonisamaizing)
x = "Python"
y = "is"
z = "amaizing"
print(x + y + z)

# + operator with space (Python is amaizing)
x = "Python "
y = "is "
z = "amaizing"
print(x + y + z)

# + operator with interger
x = 5
y = 8
print(x+y)

# Global Variables
x = "amaizing"


def myfunc():
    print("Cynthia is " + x)


myfunc()

# Global variables and local variables
x = "awesome"


def myfun():
    x = "fantastic"
    print("Python is " + x)


myfun()

print("Python is " + x)

# Global Keyword (Local keyword used globally)


def myfunction():
    global x
    x = "amaizing"


myfunction()

print("Cynthia is really " + x)

# Defining Data Types
# String
x = str('Jane')
y = ("Jane")
print(x, y)
print(type(x))
print(type(y))

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# integers
x = 5
y = int(5)
print(x, y)
print(type(x))
print(type(y))

# float
x = 3.5
y = float(3.5)
print(x, y)
print(type(x))
print(type(y))

# complex
x = 1j
y = complex(1j)
print(x, y)
print(type(x))
print(type(y))

# list
x = ["Joan", "Cynthia", "Kuria"]
y = list(("Joan", "Cynthia", "Kuria"))
print(x, y)
print(type(x))
print(type(y))

# tuple
x = ("Joan", "Cynthia", "Kuria")
y = tuple(("Joan", "Cynthia", "Kuria"))
print(x, y)
print(type(x))
print(type(y))

# range
x = range(6)
y = range(6)
print(x, y)
print(type(x))
print(type(y))

# Dictionary
x = {"Name: ": "Jack", "Age: ": 30}
y = dict(Name="John", Age=30)
print(x, y)
print(type(x))
print(type(y))

# Sets
x = {"Joan", "Cynthia", "Kuria"}
y = set(("Joan", "Cynthia", "Kuria"))
print(x, y)
print(type(x))
print(type(y))

# frozenset
x = frozenset({"Joan", "Cynthia", "Kuria"})
y = frozenset(("Joan", "Cynthia", "Kuria"))
print(x, y)
print(type(x))
print(type(y))

# Boolean (True or False)
x = True
y = bool(5)
print(x, y)
print(type(x))
print(type(y))

# Bytes
x = b"Hello"
y = bytes(5)
print(x, y)
print(type(x))
print(type(y))

# bytearray
x = bytearray(5)
y = bytearray(5)
print(x, y)
print(type(x))
print(type(y))

# memoryview
x = memoryview(bytes(5))
y = memoryview(bytes(5))
print(x, y)
print(type(x))
print(type(y))

# Nonetype
x = None
print(x)
print(type(x))

# Print a random number in the range of 1-11
print(random.randrange(1, 11))
