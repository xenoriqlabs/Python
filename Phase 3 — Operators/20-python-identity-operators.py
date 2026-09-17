# ==========================================
# 1. 'is' Operator
# ==========================================

# 'is' checks whether two variables
# refer to the SAME object

a = [1, 2, 3]
b = a

print("IS Operator:")
print("a is b:", a is b)

# ==========================================
# 2. 'is not' Operator
# ==========================================

# 'is not' checks whether two variables
# refer to DIFFERENT objects.

x = [10, 20, 30]
y = [10, 20, 30]

print("\nIS NOT Operator:")
print("x is not y:", x is not y)

# ==========================================
# 3. '==' vs 'is'
# ==========================================

# '==' compares values.
# 'is' compares object identity.

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print("\n== vs is:")
print("list1 == list2:", list1 == list2)
print("list1 is list2:", list1 is list2)

# ==========================================
# 4. Same Object
# ==========================================

numbers1 = [10, 20, 30]
numbers2 = numbers1

print("\nSame Object:")
print("numbers1 == numbers2:", numbers1 == numbers2)
print("numbers1 is numbers2:", numbers1 is numbers2)

# ==========================================
# 5. Different Objects
# ==========================================

numbers3 = [10, 20, 30]
numbers4 = [10, 20, 30]

print("\nDifferent Objects:")
print("numbers3 == numbers4", numbers3 == numbers4)
print("numbers3 is numbers4", numbers3 is numbers4)

# ==========================================
# 6. Using 'is' with None
# ==========================================

name = None

print("\nNone Check:")

print("name is None:", name is None)
print("name is not None:", name is not None)

# ==========================================
# 7. Practical None Example
# ==========================================

print("\nPractical None Example")

username = None

if username is None:
    print("Username is not available")
else:
    print("Username is available")

# ==========================================
# 8. Practical 'is not None' Example
# ==========================================

print("\nPractical 'is not None' Example")

email = "xenoriqlabs@gmail.com"

if email is not None:
    print("Email is available")
else:
    print("Email is not available")

# ==========================================
# 9. Object Reference Example
# ==========================================

print("\nObject Reference Example")

company1 = ["Xenoriq Labs"]
company2 = company1

print("\nObject Reference:")
print("company1 is company2:", company1 is company2)

# ==========================================
# 10. Separate Object Example
# ==========================================

company3 = ["Xenoriq Labs"]
company4 = ["Xenoriq Labs"]

print("\nSeperate Objects:")
print("company3 == company4:", company3 == company4)
print("company3 is company4:", company3 is company4)
print("company3 is not company4:", company3 is not company4)

# ==========================================
# 11. Boolean Identity Example
# ==========================================

value = True

print("\nBoolean Identity:")
print("value is True:", value is True)
print("value is not True:", value is not True)

# ==========================================
# 12. Practical User Data Example
# ==========================================

user = {
    "name" : "Saif",
    "email" : None
}

print("\nUser Data:")

if user["email"] is None:
    print("User has not provided an email")
else:
    print("User email:", user["email"])

# ==========================================
# 13. Important Difference
# ==========================================

first = [100, 200]
second = [100, 200]

print("\nImportant Difference:")
print("Same values:", first == second)
print("Same object:", first is second)
print("Different object:", first is not second)
