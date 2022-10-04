a = "Hello, World!"
print(a[3])

for x in "banana":
    print(x)

a = "Hey you!"
print(len(a))

a = "'The best things in life are free!"
print("free" in a)

txt = "The best things in life are free!"
if "free" in txt:
    print('Yes, "free" is in txt.')

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("'Expensive' is not in txt")


def myfunc():

    a = "Cynthia"
    print(a)

myfunc()

# slicing 
a = "Hello World!"
print(a[2:6])

# Slice from start 
a = "Hello World!"
print(a[:7])

# Slice to end 
a = "Hello World!"
print(a[2:])

# slice negative 
b = "Hello, World!"
print(b[-5:-2])

# Uppercase
a= "Hey you!"
print(a.upper())

# Lowercase
a= " Hey you! "
print(a.lower())

# Stip
a= " Hey you! "
print(a.strip())

#capitalize
a= "hey you! " + "i don't really like you. " + "have a great day!"
print(a.capitalize())

# replace 
a = "Hello, World!"
print(a.replace("H", "J"))

# Split 
a = "Hello, World! I am, Cynthia"
print(a.split(",")) 

# Concatiation 
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# insert numbers into strings 
age = 20
txt = "I am {}"
txt2 = " years old"
print(txt.format(age) + txt2)

age = 65
txt = "I am {} years old"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars. Plus {} Change"
print(myorder.format(quantity, itemno, price, price))

# escape Character
txt = "The best things in life are \"free\"!"
print(txt)

txt = "It's alright."
print(txt)

txt = 'It\'s alright.'
print(txt)

# How to insert a backslash 
txt = "This will insert one \\ (backslash)."
print(txt) 

# Insert on line (br)
txt = "Hello\nWorld!"
print(txt) 



































