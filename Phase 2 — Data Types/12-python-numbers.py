# ==============================
# 1. int — Integer
# ==============================

# An int is a whole number without a decimal point.

age = 22
quantity = 10
temperature = -5
year = 2026

print(age)
print(quantity)
print(temperature)
print(year)

# Positive, negative, and zero are all integers:

x = 100
y = -50
z = 0

print(x)
print(y)
print(z)

# You can perform mathematical operations with integers:

a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a // b)  # Floor division
print(a % b)   # Remainder
print(a ** b)  # Power

# You can check the data type using type():

number = 100

print(type(number))

# ==============================
# 2. float — Decimal Number
# ==============================

# A float is a number that contains a decimal point.

price = 99.99
height = 5.9
temperature = 36.5
pi = 3.14159

print(price)
print(height)
print(temperature)
print(pi)

# Negative decimal numbers are also floats:

temperature = -2.5

print(temperature)
print(type(temperature))

# Practical Example — Shopping

price = 150.50
quantity = 3

total = price * quantity

print("Total:", total)

# Float Division

# The / operator always produces a float:

result = 10 / 2

print(result)
print(type(result))

# ==============================
# 3. complex — Complex Number
# ==============================

# A complex number contains:

# Real part
# Imaginary part

# Python uses j for the imaginary part.

number = 3 + 4j

print(number)
print(type(number))

# You can access the real and imaginary parts:

number = 3 + 4j

print(number.real)
print(number.imag)

# Practical Example — Complex Numbers

voltage = 5 + 3j
current = 2 + 1j

print("Voltage:", voltage)
print("Current:", current)

# You can also perform mathematical operations:

a = 3 + 2j
b = 1 + 4j

print(a + b)
print(a - b)
print(a * b)
# ==============================
# Checking Number Types
# ==============================

integer_number = 100
float_number = 10.5
complex_number = 3 + 4j

print(type(integer_number))
print(type(float_number))
print(type(complex_number))