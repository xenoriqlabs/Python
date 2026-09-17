# ==========================================
# 1. Basic Operator Precedence
# ==========================================

# Multiplication (*) has higher precedence
# than addition (+).

result = 10 + 5 * 2

print("Basic Precedence:")
print("10 + 5 * 2 =", result)

# Evaluation:
# 5 * 2 = 10
# 10 + 10 = 20


# ==========================================
# 2. Parentheses
# ==========================================

# Parentheses are evaluated first.

result = (10 + 5) * 2

print("\nParentheses:")
print("(10 + 5) * 2 =", result)

# Evaluation:
# 10 + 5 = 15
# 15 * 2 = 30


# ==========================================
# 3. Without Parentheses vs With Parentheses
# ==========================================

without_parentheses = 10 + 5 * 2
with_parentheses = (10 + 5) * 2

print("\nWithout vs With Parentheses:")

print("Without parentheses:", without_parentheses)
print("With parentheses:", with_parentheses)


# ==========================================
# 4. Multiplication and Addition
# ==========================================

result = 2 + 3 * 4

print("\nMultiplication and Addition:")
print("2 + 3 * 4 =", result)

# Evaluation:
# 3 * 4 = 12
# 2 + 12 = 14


# ==========================================
# 5. Division and Multiplication
# ==========================================

result = 100 / 5 * 2

print("\nDivision and Multiplication:")
print("100 / 5 * 2 =", result)

# Same precedence.
# Evaluation is left to right:
#
# 100 / 5 = 20
# 20 * 2 = 40


# ==========================================
# 6. Subtraction and Addition
# ==========================================

result = 20 - 5 + 3

print("\nSubtraction and Addition:")
print("20 - 5 + 3 =", result)

# Same precedence.
# Evaluation is left to right:
#
# 20 - 5 = 15
# 15 + 3 = 18


# ==========================================
# 7. Exponentiation
# ==========================================

result = 2 + 3 ** 2

print("\nExponentiation:")
print("2 + 3 ** 2 =", result)

# Evaluation:
# 3 ** 2 = 9
# 2 + 9 = 11


# ==========================================
# 8. Parentheses with Exponentiation
# ==========================================

result = (2 + 3) ** 2

print("\nParentheses with Exponentiation:")
print("(2 + 3) ** 2 =", result)

# Evaluation:
# 2 + 3 = 5
# 5 ** 2 = 25


# ==========================================
# 9. Complex Arithmetic Expression
# ==========================================

result = 10 + 2 * 3 ** 2

print("\nComplex Arithmetic:")
print("10 + 2 * 3 ** 2 =", result)

# Step 1:
# 3 ** 2 = 9
#
# Step 2:
# 2 * 9 = 18
#
# Step 3:
# 10 + 18 = 28


# ==========================================
# 10. Complex Expression with Parentheses
# ==========================================

result = (10 + 2) * (3 ** 2)

print("\nComplex Expression with Parentheses:")
print("(10 + 2) * (3 ** 2) =", result)

# Step 1:
# 10 + 2 = 12
#
# Step 2:
# 3 ** 2 = 9
#
# Step 3:
# 12 * 9 = 108


# ==========================================
# 11. Comparison Operator Precedence
# ==========================================

age = 20
marks = 80

result = age >= 18 and marks >= 50

print("\nComparison + Logical Operators:")
print("Age >= 18 AND Marks >= 50:", result)

# Step 1:
# age >= 18 → True
#
# Step 2:
# marks >= 50 → True
#
# Step 3:
# True and True → True


# ==========================================
# 12. NOT, AND and OR Precedence
# ==========================================

result = True or False and False

print("\nNOT, AND and OR:")
print("True or False and False =", result)

# AND has higher precedence than OR.
#
# Step 1:
# False and False → False
#
# Step 2:
# True or False → True


# ==========================================
# 13. Parentheses Change Logical Evaluation
# ==========================================

result = (True or False) and False

print("\nLogical Parentheses:")
print("(True or False) and False =", result)

# Step 1:
# True or False → True
#
# Step 2:
# True and False → False


# ==========================================
# 14. Bitwise Operator Precedence
# ==========================================

a = 5
b = 3

result = a + b & 7

print("\nBitwise Precedence:")
print("a + b & 7 =", result)

# Arithmetic (+) has higher precedence
# than bitwise AND (&).
#
# Step 1:
# a + b = 8
#
# Step 2:
# 8 & 7 = 0


# ==========================================
# 15. Using Parentheses for Clarity
# ==========================================

a = 10
b = 5
c = 2

result1 = a + b * c
result2 = (a + b) * c

print("\nUsing Parentheses for Clarity:")

print("a + b * c =", result1)
print("(a + b) * c =", result2)


# ==========================================
# 16. Evaluation Order
# ==========================================

result = 50 - 10 + 5

print("\nEvaluation Order:")
print("50 - 10 + 5 =", result)

# + and - have the same precedence.
# Therefore Python evaluates from left to right:
#
# 50 - 10 = 40
# 40 + 5 = 45


# ==========================================
# 17. Multiple Operators
# ==========================================

result = 100 + 20 / 5 * 2 - 10

print("\nMultiple Operators:")
print("100 + 20 / 5 * 2 - 10 =", result)

# Step 1:
# 20 / 5 = 4.0
#
# Step 2:
# 4.0 * 2 = 8.0
#
# Step 3:
# 100 + 8.0 = 108.0
#
# Step 4:
# 108.0 - 10 = 98.0


# ==========================================
# 18. Practical Marks Example
# ==========================================

math = 80
english = 70
computer = 90

average = (math + english + computer) / 3

print("\nStudent Marks:")
print("Math:", math)
print("English:", english)
print("Computer:", computer)
print("Average:", average)


# ==========================================
# 19. Practical Shopping Example
# ==========================================

price = 1000
quantity = 3
discount = 200

total = price * quantity - discount

print("\nShopping Calculation:")
print("Price:", price)
print("Quantity:", quantity)
print("Discount:", discount)
print("Total:", total)

# Evaluation:
# price * quantity = 3000
# 3000 - 200 = 2800


# ==========================================
# 20. Best Practice
# ==========================================

# Even when you know the precedence,
# parentheses can make your code easier to read.

age = 20
marks = 80

eligible = (age >= 18) and (marks >= 50)

print("\nBest Practice:")
print("Eligible:", eligible)