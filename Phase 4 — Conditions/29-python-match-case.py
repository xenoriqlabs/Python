
# ========================================
# Python Match-Case Statement
# File: 29-python-match-case.py
# Company: Xenoriq Labs
# Requires: Python 3.10+
# ========================================

number = 2

match number:
    case 1:
        print("Number One")

    case 2:
        print("Number Two")

    case 3:
        print("Number Three")

    case _:
        print("Unknown NUmber")


# Example 2: Match a Day

day = "Monday"

match day:
    case "Monday":
        print("Start of the work week.")

    case "Friday":
        print("Almost the weekend.")

    case "Saturday" | "Sunday":
        print("It is the weekend.")

    case _:
        print("It is a regular weekday.")


# Example 3: Simple Calculator

first_number = 10
second_number = 5
operator = "+"

match operator:
    case "+":
        print("Result:", first_number + second_number)

    case "-":
        print("Result:", first_number - second_number)

    case "*":
        print("Result:", first_number * second_number)

    case "/":
        if second_number != 0:
            print("Result:", first_number / second_number)

        else:
            print("Cannot divide by zero.")

    case _:
        print("Invalid operator.")


# Example 4: Traffic Light

traffic_light = "red"

match traffic_light:
    case "red":
        print("Stop.")

    case "yellow":
        print("Prepare to stop.")

    case "green":
        print("Go.")

    case _:
        print("Invalid traffic light.")


# Example 5: Default Case

language = "JavaScript"

match language:
    case "Python":
        print("Python selected.")

    case "JavaScript":
        print("JavaScript selected.")

    case "C++":
        print("C++ selected.")

    case _:
        print("Language not found.")


# Example 6: Match Multiple Values

number = 4

match number:
    case 1 | 2 | 3:
        print("Number is between 1 and 3.")

    case 4 | 5 | 6:
        print("Number is between 4 and 6.")

    case _:
        print("Number is outside the range.")


# Example 7: User Role

role = "admin"

match role:
    case "admin":
        print("Welcome to the admin dashboard.")

    case "editor":
        print("Welcome to the editor dashboard.")

    case "user":
        print("Welcome to your account.")

    case _:
        print("Unknown user role.")


# Example 8: Xenoriq Labs Course Selection

course = "Python"

match course:
    case "Python":
        print("You selected the Python course.")

    case "CSS":
        print("You selected the CSS course.")

    case "Bootstrap":
        print("You selected the Bootstrap course.")

    case "C++":
        print("You selected the C++ course.")

    case _:
        print("Course not available.")

# Example 9: Match with a Condition (Guard)

number = 15

match number:
    case n if n > 0:
        print("The number is positive")

    case n if n < 0:
        print("The number is negative.")

    case _:
        print("The number is zero.")


# Example 10: Match a Tuple

point = (0, 5)

match point:
    case (0, 0):
        print("The point is at the origin.")

    case (0, y):
        print("The point is on the Y-axis.")

    case (x, 0):
        print("The point is on the X-axis.")

    case (x, y):
        print("The point is somewhere else.")
