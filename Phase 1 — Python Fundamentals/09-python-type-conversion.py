# Type conversion means changing a value from one data type to another.

# Python provides several built-in functions for this:

# int() → converts to integer
# float() → converts to floating-point number
# str() → converts to string
# bool() → converts to Boolean
# Explicit conversion → when you manually convert a value using these functions

# 1. --> int()

# int() converts a value into an integer.

age = "23"
age = int(age)

print(age)
print(type(age))

# 2. --> float()

# float() converts a value into a floating-point number.

price = "99.9"
price = float(price)

print(price)
print(type(price))

# Practical example

price = input("Enter price of a product: ")
quantity = input("Enter quantity: ")

price = float(price)
quantity = int(quantity)

total = price * quantity

print("Total Price is:", total)

# 3. --> str()

# str() converts a value into a string.

age = 25

age = str(age)

print(age)
print(type(age))

# Practical example

# You can use str() when you need to combine a number with text.

age = 25

message = "I am " + str(age) + " years old"

print(message)

# With f-strings, you normally don't need to manually use str():

age = 25

print(f"I am {age} years old.")

# 4. --> bool()

# bool() converts a value into either: true or false

print(bool(0))
print(bool(1))

print(bool(""))
print(bool("Hello"))

print(bool(25))
print(bool(0))

# Practical example

username = input("Enter username: ")

if bool(username):
    print("Username entered.")
else:
    print("Username is empty.")

# Actually, you can simplify this to:

if username:
    print("Username entered.")
else:
    print("Username is empty.")

# 5. --> Explicit Conversion

name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height: ")

age = int(age)
height = float(height)

print("Name:", name)
print("Age:", age)
print("Height:", height)