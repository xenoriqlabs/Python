# Variables are used to store data in Python.
# A variable is a name that refers to a value.

# --> 1. Variables

name = 'Saif'
age = 22
salary = 50000

print("Your name is:", name)
print("Your age is:", age)
print("Your Salary is:", salary)

# --> 2. Variable Assignment

name = 'Saif'
print("Your name is:", name)

name = 'Saif Tahir'
print("Your name after updation is:", name)     # The value of name is changed

age = 19
age = 22
print("Your age after updation is:", age)       # The value of age is changed

# --> 3. Multiple Assignment

name, age, city = 'Saif', 22, 'Sahiwal'

print('Your name is:', name)
print('Your age is:', age)
print('Your city is:', city)

x = y = z = 22

print('Value of x is:', x)
print('Value of y is:', y)
print('Value of z is:', z)

# --> 4. Variable Naming

# Variable names can contain letters, numbers, and underscores.

first_name = 'Saif'
CompanyName = "Xenoriq Labs"
age2 = 22

print("Your First Name is:", first_name)
print("Your Company Name is:", CompanyName)
print("Your ags is:", age2)

# Variable names cannot start with a number.

# 2name = "Saif"       # Invalid


# Variable names cannot contain spaces.

# first name = "Saif"  # Invalid


# Use underscores instead of spaces.

first_name = "Saif"
last_name = "Rahman"

print(first_name)
print(last_name)

# Variable names are case-sensitive.

name = "Saif"
Name = "Ali"

print(name)
print(Name)


# Python keywords cannot be used as variable names.

# class = "Python"     # Invalid
# if = 10              # Invalid


# --> 5. Constants Convention

# Python does not have a strict constant keyword.
# By convention, constants are written in uppercase letters.

# --> 5. Constants Convention

# Python does not have a strict constant keyword.
# By convention, constants are written in uppercase letters.

PI = 3.14159
MAX_USERS = 100
COMPANY_NAME = "Xenoriq Labs"

print(PI)
print(MAX_USERS)
print(COMPANY_NAME)


# Constants can technically be changed in Python,
# but uppercase names indicate that the value should not be changed.

PI = 3.14
print(PI)

# --> 6. Dynamic Typing

# Python is dynamically typed.
# A variable does not need a data type declaration.

value = 100
print(value)

value = "Python"
print(value)

value = 3.14
print(value)

value = True
print(value)


# The same variable can refer to different types of values
# during the execution of the program