# ============================================================
#              PYTHON ASSIGNMENT OPERATORS
#              File: 17-python-assignment-operators.py
# ============================================================

# Assignment Operators:
# =    Assignment
# +=   Add and assign
# -=   Subtract and assign
# *=   Multiply and assign
# /=   Divide and assign
# //=  Floor divide and assign
# %=   Modulus and assign
# **=  Exponentiation and assign


# ============================================================
# 1. ASSIGNMENT OPERATOR (=)
# ============================================================

print("\n----- Assignment (=) -----")

x = 10

print('x =', x)

# The value 10 is assigned to x.

# Multiple variables

name = "Saif"
age = 22
city = 'Sahiwal'

print("Name:", name)
print("Age:", age)
print("City:", city)

# Multiple assignment

a = b = c = 100

print("a =", a)
print("b =", b)
print('c =', c)

# Assign different values

x, y, z = 10, 20, 30

print("\nx =", x)
print("y =", y)
print("z =", z)

# ============================================================
# 2. ADD AND ASSIGN (+=)
# ============================================================

print("\n----- Add and Assign (+=) -----")

x = 10
x += 5

print("x =", x)

# Same as:
# x = x + 5

# Practical Example: Shopping Cart

cart_price = 1000
cart_price += 500

print("\nInitial Price: 1000")
print("After Adding 500:", cart_price)

# ============================================================
# 3. SUBTRACT AND ASSIGN (-=)
# ============================================================

print("\n----- Subtract and Assign (-=) -----")

x = 20
x -= 5

print("x =", x)

# Same as:
# x = x - 5

# Practical Example: Bank Balance

balance = 10000
balance -= 2500

print("\nInitial Balance: 10000")
print("After Withdrawal:", balance)


# ============================================================
# 4. MULTIPLY AND ASSIGN (*=)
# ============================================================

print("\n----- MULTIPLY AND ASSIGN (*=) -----")

x = 10
x *= 5

print("x =", x)

# Same as:
# x = x * 5

# Practical Example

price = 500
quantity = 3

price *= quantity

print('\nPrice:', 500)
print("Quantity:", quantity)
print("Total Price:", price)


# ============================================================
# 5. DIVIDE AND ASSIGN (/=)
# ============================================================

print("\n----- Divide and Assign (/=) -----")

x = 20
x /= 4

print("x =", x)

# Same as:
# x = x / 4

# Note:
# /= usually changes the value into a float.


# Practical Example: Average

total_marks = 500
subjects = 5

total_marks /= subjects

print("\nTotal Marks:", 500)
print("Subjects:", subjects)
print("Average:", total_marks)


# ============================================================
# 6. FLOOR DIVIDE AND ASSIGN (//=)
# ============================================================

print("\n----- Floor Divide and Assign (//=) -----")

x = 20
x //= 6

print("x =", x)

# Same as:
# x = x // 6

# Practical Example

total_items = 23
boxes = 5

total_items //= boxes

print("\nTotal Items: 23")
print("Boxes:", boxes)
print("Complete Items Per Box:", total_items)

# ============================================================
# 7. MODULUS AND ASSIGN (%=)
# ============================================================

print("\n----- Modulus and Assign (%=) -----")

x = 20
x %= 6

print("x =", x)

# Same as:
# x = x % 6

# Practical Example: Find Remainder

number = 17
number %= 2

print("\nNumber: 17")
print("Remainder:", number)

# Even / Odd Example

number = 25
number %= 2

if number == 0:
    print("Even Number")
else:
    print("Odd Number")


# ============================================================
# 8. EXPONENTIATION AND ASSIGN (**=)
# ============================================================

print("\n----- Exponentiation and Assign (**=) -----")

x = 2
x **= 5

print("x =", x)

# Same as:
# x = x ** 5


# Practical Example

number = 5
number **= 2

print("\nNumber: 5")
print("Square:", number)

# ============================================================
# ALL ASSIGNMENT OPERATORS TOGETHER
# ============================================================

print("\n========================================")
print("       ALL ASSIGNMENT OPERATORS")
print("========================================")


# =
x = 10
print("After =   :", x)


# +=
x = 10
x += 5
print("After +=  :", x)


# -=
x = 10
x -= 5
print("After -=  :", x)


# *=
x = 10
x *= 5
print("After *=  :", x)


# /=
x = 10
x /= 5
print("After /=  :", x)


# //=
x = 10
x //= 3
print("After //= :", x)


# %=
x = 10
x %= 3
print("After %=  :", x)


# **=
x = 10
x **= 2
print("After **= :", x)

# ============================================================
# REAL-WORLD EXAMPLE: BANK ACCOUNT
# ============================================================

print("\n========================================")
print("         BANK ACCOUNT EXAMPLE")
print("========================================")

balance = 50000

print("Starting Balance:", balance)

# Deposit
balance += 10000
print("After Deposit:", balance)

# Withdrawal
balance -= 5000
print("After Withdrawal:", balance)

# Divide into savings
balance //= 2
print("After Splitting:", balance)