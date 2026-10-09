# Python Nested If Statements

# Example 1: Check Age and License

age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("You need a driving license.")
else:
    print("You are too young to drive.")


# Example 2: Check Username and Password

username = "Saif"
password = "python123"

if username == "Saif":
    if password == "python123":
        print("Login successful.")
    else:
        print("Incorrect password.")
else:
    print("Incorrect username.")


# Example 3: Check Positive Number and Even Number

number = 8

if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is zero or negative.")


# Example 4: Exam Eligibility and Result

attendance = 85
marks = 75

if attendance >= 75:
    if marks >= 40:
        print("You passed the exam.")
    else:
        print("You failed the exam.")
else:
    print("You are not eligible due to low attendance.")


# Example 5: Check Multiple Levels of Access

is_logged_in = True
is_admin = True
has_permission = True

if is_logged_in:
    if is_admin:
        if has_permission:
            print("Access granted to admin dashboard.")
        else:
            print("You do not have permission.")
    else:
        print("You have regular user access.")
else:
    print("Please log in first.")


# Example 6: Xenoriq Labs Course Enrollment

age = 17
has_basic_knowledge = True
course = "Python"

if course == "Python":
    if age >= 15:
        if has_basic_knowledge:
            print("You can enroll in the Python course.")
        else:
            print("Please learn the basics first.")
    else:
        print("You do not meet the minimum age requirement.")
else:
    print("Course not found.")


# Example 7: Shopping Discount Eligibility

purchase_amount = 6000
is_member = True

if purchase_amount >= 5000:
    if is_member:
        print("You qualify for a 15% discount.")
    else:
        print("You qualify for a 10% discount.")
else:
    print("No discount available.")


# Example 8: Check a Number in Multiple Levels

number = 12

if number > 0:
    print("The number is positive.")

    if number >= 10:
        print("The number is at least 10.")

        if number % 2 == 0:
            print("The number is also even.")
else:
    print("The number is not positive.")