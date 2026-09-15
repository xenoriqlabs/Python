# ==========================================
# 1. AND Operator
# ==========================================

# The 'and' operator returns True
# only when BOTH conditions are True.

age = 20
has_id = True

result = age >= 18 and has_id

print("AND Operator:")
print("Age is 18 or older AND has ID:", result)


# Example 2
username_correct = True
password_correct = True

login_successful = username_correct and password_correct

print("Username correct AND password correct:", login_successful)


# Example 3
marks = 75

passed = marks >= 50 and marks <= 100

print("Marks are between 50 and 100:", passed)


# ==========================================
# 2. OR Operator
# ==========================================

# The 'or' operator returns True
# when AT LEAST ONE condition is True.

is_student = True
is_teacher = False

result = is_student or is_teacher

print("\nOR Operator:")
print("Is student OR teacher:", result)


# Example 2
age = 16

has_parent_permission = True

can_join = age >= 18 or has_parent_permission

print("Can join with age 18+ OR parent permission:", can_join)


# Example 3
student = False
employee = True

discount = student or employee

print("Eligible for discount:", discount)


# ==========================================
# 3. NOT Operator
# ==========================================

# The 'not' operator reverses a Boolean value.
# True becomes False.
# False becomes True.

is_logged_in = True

print("\nNOT Operator:")
print("Is logged in:", is_logged_in)
print("Is NOT logged in:", not is_logged_in)


# Example 2
course_closed = False

print("Course closed:", course_closed)
print("Course is NOT closed:", not course_closed)


# Example 3
is_admin = False

print("Is admin:", is_admin)
print("Is NOT admin:", not is_admin)


# ==========================================
# 4. AND Truth Table
# ==========================================

print("\nAND Truth Table:")

print(True and True)
print(True and False)
print(False and True)
print(False and False)


# ==========================================
# 5. OR Truth Table
# ==========================================

print("\nOR Truth Table:")

print(True or True)
print(True or False)
print(False or True)
print(False or False)


# ==========================================
# 6. NOT Truth Table
# ==========================================

print("\nNOT Truth Table:")

print(not True)
print(not False)


# ==========================================
# 7. Practical Student Example
# ==========================================

student_age = 19
student_marks = 80
has_certificate = True

eligible = (
    student_age >= 18
    and student_marks >= 50
    and has_certificate
)

print("\nStudent Eligibility:")
print("Student is eligible:", eligible)


# ==========================================
# 8. Practical Login Example
# ==========================================

username = "Saif"
password = "12345"

correct_username = "Saif"
correct_password = "12345"

login = (
    username == correct_username
    and password == correct_password
)

print("\nLogin System:")
print("Login successful:", login)


# ==========================================
# 9. Practical Access Example
# ==========================================

age = 17
has_permission = True

access_allowed = age >= 18 or has_permission

print("\nAccess System:")
print("Access allowed:", access_allowed)


# ==========================================
# 10. Combining AND, OR and NOT
# ==========================================

age = 20
is_student = True
is_banned = False

can_access = (
    (age >= 18 and is_student)
    and not is_banned
)

print("\nCombined Logical Operators:")
print("Can access:", can_access)