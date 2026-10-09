# Python If-Elif-Else Statements

# Example 1: Check Positive, Negative, or Zero

number = -5

if number > 0:
    print("The number is positive.")

elif number < 0:
    print("The number is negative.")

else:
    print("The number is zero.")


# Example 2: Grade Calculator

marks = 85

if marks >= 90:
    print("Grade: A+")

elif marks >= 80:
    print("Grade: A")

elif marks >= 70:
    print("Grade: B")

elif marks >= 60:
    print("Grade: C")

elif marks >= 40:
    print("Grade: D")

else:
    print("Grade: F")


# Example 3: Check Age Group

age = 16

if age < 13:
    print("You are a child.")

elif age < 20:
    print("You are a teenager.")

elif age < 60:
    print("You are an adult.")

else:
    print("You are a senior.")


# Example 4: Temperature Checker

temperature = 35

if temperature >= 40:
    print("It is extremely hot.")

elif temperature >= 30:
    print("It is hot.")

elif temperature >= 20:
    print("The weather is warm.")

elif temperature >= 10:
    print("The weather is cool.")

else:
    print("The weather is cold.")


# Example 5: Login System

username = "Saif"
password = "python123"

if username == "Saif" and password == "python123":
    print("Login successful.")

elif username != "Saif":
    print("Incorrect username.")

else:
    print("Incorrect password.")


# Example 6: Simple Traffic Light

traffic_light = "yellow"

if traffic_light == "red":
    print("Stop.")

elif traffic_light == "yellow":
    print("Prepare to stop.")

elif traffic_light == "green":
    print("Go.")

else:
    print("Invalid traffic light color.")


# Example 7: Compare Two Numbers

first_number = 10
second_number = 20

if first_number > second_number:
    print("The first number is greater.")

elif first_number < second_number:
    print("The second number is greater.")

else:
    print("Both numbers are equal.")


# Example 8: Check Even, Odd, or Zero

number = 7

if number == 0:
    print("The number is zero.")

elif number % 2 == 0:
    print("The number is even.")

else:
    print("The number is odd.")


# Example 9: Discount Calculator

purchase_amount = 6000

if purchase_amount >= 10000:
    print("You get a 20% discount.")

elif purchase_amount >= 5000:
    print("You get a 10% discount.")

elif purchase_amount >= 2000:
    print("You get a 5% discount.")

else:
    print("No discount available.")


# Example 10: Xenoriq Labs Course Eligibility

course = "Python"
age = 16

if course == "Python" and age >= 15:
    print("You are eligible for the Python course.")

elif course == "Python" and age < 15:
    print("You need to meet the minimum age requirement.")

else:
    print("Course not found.")