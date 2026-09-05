# ============================================================
#              PYTHON ARITHMETIC OPERATORS
# ============================================================

# Arithmetic Operators:
# +   Addition
# -   Subtraction
# *   Multiplication
# /   Division
# //  Floor Division
# %   Modulus (Remainder)
# **  Exponentiation (Power)


# ============================================================
# 1. ADDITION (+)
# ============================================================

a = 20
b = 10

addition = a + b

print("----- Addition -----")
print("a =", a)
print("b =", b)
print("a + b =", addition)


# Practical Example
price = 500
delivery_charges = 100

total_price = price + delivery_charges

print("\nProduct Price:", price)
print("Delivery Charges:", delivery_charges)
print("Total Price:", total_price)


# ============================================================
# 2. SUBTRACTION (-)
# ============================================================

a = 20
b = 10

subtraction = a - b

print("\n----- Subtraction -----")
print("a =", a)
print("b =", b)
print("a - b =", subtraction)


# Practical Example
account_balance = 5000
withdrawal = 1500

remaining_balance = account_balance - withdrawal

print("\nAccount Balance:", account_balance)
print("Withdrawal:", withdrawal)
print("Remaining Balance:", remaining_balance)


# ============================================================
# 3. MULTIPLICATION (*)
# ============================================================

a = 20
b = 10

multiplication = a * b

print("\n----- Multiplication -----")
print("a =", a)
print("b =", b)
print("a * b =", multiplication)


# Practical Example
product_price = 750
quantity = 4

total_cost = product_price * quantity

print("\nProduct Price:", product_price)
print("Quantity:", quantity)
print("Total Cost:", total_cost)


# ============================================================
# 4. DIVISION (/)
# ============================================================

a = 20
b = 4

division = a / b

print("\n----- Division -----")
print("a =", a)
print("b =", b)
print("a / b =", division)

# / always returns a float
print("Type:", type(division))


# Practical Example
total_marks = 500
number_of_subjects = 5

average_marks = total_marks / number_of_subjects

print("\nTotal Marks:", total_marks)
print("Subjects:", number_of_subjects)
print("Average Marks:", average_marks)


# ============================================================
# 5. FLOOR DIVISION (//)
# ============================================================

a = 20
b = 6

floor_division = a // b

print("\n----- Floor Division -----")
print("a =", a)
print("b =", b)
print("a // b =", floor_division)


# Difference between / and //

print("\nNormal Division:", 20 / 6)
print("Floor Division:", 20 // 6)


# Practical Example
total_items = 23
boxes = 5

items_per_box = total_items // boxes

print("\nTotal Items:", total_items)
print("Number of Boxes:", boxes)
print("Complete Items Per Box:", items_per_box)


# ============================================================
# 6. MODULUS (%)
# ============================================================

a = 20
b = 6

remainder = a % b

print("\n----- Modulus -----")
print("a =", a)
print("b =", b)
print("a % b =", remainder)


# Practical Example: Check Even or Odd

number = 25

if number % 2 == 0:
    print("\n", number, "is Even")
else:
    print("\n", number, "is Odd")


# Another Example

number = 40

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")


# ============================================================
# 7. EXPONENTIATION (**)
# ============================================================

a = 2
b = 5

power = a ** b

print("\n----- Exponentiation -----")
print("a =", a)
print("b =", b)
print("a ** b =", power)


# Practical Examples

print("\n2 ** 3 =", 2 ** 3)
print("5 ** 2 =", 5 ** 2)
print("10 ** 2 =", 10 ** 2)
print("3 ** 4 =", 3 ** 4)


# Square Root using exponentiation

number = 25
square_root = number ** 0.5

print("\nSquare Root of", number, "=", square_root)


# ============================================================
#              ALL OPERATORS TOGETHER
# ============================================================

a = 20
b = 6

print("\n========================================")
print("       ALL ARITHMETIC OPERATORS")
print("========================================")

print("Addition:       ", a + b)
print("Subtraction:    ", a - b)
print("Multiplication: ", a * b)
print("Division:       ", a / b)
print("Floor Division: ", a // b)
print("Modulus:        ", a % b)
print("Exponentiation: ", a ** b)


# ============================================================
#              REAL-WORLD CALCULATION
# ============================================================

print("\n========================================")
print("         SHOPPING CALCULATION")
print("========================================")

product_price = 1200
quantity = 3
discount = 500
delivery = 200

# Multiplication
subtotal = product_price * quantity

# Subtraction
after_discount = subtotal - discount

# Addition
final_price = after_discount + delivery

print("Product Price:", product_price)
print("Quantity:", quantity)
print("Subtotal:", subtotal)
print("Discount:", discount)
print("After Discount:", after_discount)
print("Delivery Charges:", delivery)
print("Final Price:", final_price)


# ============================================================
#              EVEN / ODD USING %
# ============================================================

print("\n========================================")
print("             EVEN / ODD")
print("========================================")

number = 17

remainder = number % 2

print("Number:", number)
print("Remainder:", remainder)

if remainder == 0:
    print("Result: Even Number")
else:
    print("Result: Odd Number")


# ============================================================
#              OPERATOR COMPARISON
# ============================================================

print("\n========================================")
print("          OPERATOR COMPARISON")
print("========================================")

x = 10
y = 3

print("x =", x)
print("y =", y)

print("\nx + y  =", x + y)
print("x - y  =", x - y)
print("x * y  =", x * y)
print("x / y  =", x / y)
print("x // y =", x // y)
print("x % y  =", x % y)
print("x ** y =", x ** y)


# ============================================================
# END OF FILE
# ============================================================