# The input() function is used to take input from the user.
# By default, input() always returns the user's input as a string.


# --> 1. input()

name = input("Enter your name:")
print('Your name is:', name)

# --> 2. User Input

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Name:", name)
print("Age:", age)

# --> 3. Input Conversion

# input() returns a string by default.

age = input("Enter your age: ")

print(age)
print(type(age))

# Convert string input to integer

age = int(input("Enter your age:"))

print('Your age is:', age)
print(type(age))

# Convert string input to float

price = float(input("Enter the price: "))

print(price)
print(type(price))

# Convert input to boolean

value = input("Enter True or False: ")
value = value == "True"

print(value)
print(type(value))

# --> 4. Multiple Inputs

name, age = input("Enter your name and age: ").split()

print('Your name is:', name)
print('Your age is:', age)

# Multiple integer inputs

num1, num2 = map(int, input("Enter num1 and num2: ").split())

print("Number 1:", num1)
print("Number 2:", num2)
print("Sum:", num1 + num2)

# Multiple inputs with map()

age, salary = map(int, input("Enter your age and salary: ").split())

print('Your age is:', age)
print('Your salary is:', salary)