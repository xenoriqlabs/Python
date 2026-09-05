# 1. type()
# type() tells you the exact data type of a value.

name = "Saif"
age = 22
price = 99.99
is_active = True

print(type(name))
print(type(age))
print(type(price))
print(type(is_active))

# You can also store the result
age = 22

data_type = type(age)

print(data_type)

# 2. Using type() for Type Comparison
# You can compare the result of type() with a specific type.

age = 22

if type(age) == int:
    print("Age is an integer")

# Another example:
name = 'Saif'

if type(name) == str:
    print("Name is string.")

# Multiple comparisons
value = 10

if type(value) == int:
    print("Value is intiger.")
elif type(value) == str:
    print("Value is string.")
elif type(value) == bool:
    print("Value is boolean.")
else:
    print("Other type")

# 3. isinstance()
# isinstance() checks whether a value is an instance of a particular type.

age = 22

print(isinstance(age, int))

# Another example:
name = 'Saif'

print(isinstance(age, int))
print(isinstance(age, str))

# 4. Practical isinstance() Example
age = 22

if isinstance(age, int):
    print("Age is an intiger.")
else:
    print("Age is not an intiger.")

# Another example:
username = "Saif"

if isinstance(name, str):
    print("Valid username")

# 5. Checking Multiple Types
# One very useful feature of isinstance() is that you can check multiple types at once.

value = 10

if isinstance(value, (int, str)):   # "Check whether the value is int OR float."
    print("Value is a number")

# 6. type() vs isinstance()

value = True

print(type(value) == bool)
print(isinstance(value, bool))

# But there is an important difference when inheritance is involved.

value = True

print(type(value) == int)
print(isinstance(value, int))

# Why? Because in Python, bool is a subclass of int.

# 7. Type Comparison
# You can compare types using type():

x = 100
y = "100"

print(type(x) == type(y))

# 8. Comparing Two Values' Types

a = 10
b = 20.5

if type(a) == type(b):
    print("Same type")
else:
    print("Different types")

# 9. Real-World Example — Form Data

age = 22
name = 'Saif'
salary = 90000

if not isinstance(name, str):
    print("Name must be a string")
if not isinstance(age, int):
    print("Age must be an integer")
if not isinstance(salary, (int, float)):
    print("Salary must be a number")

# This kind of checking is very useful when validating data.
