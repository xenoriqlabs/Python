# Python Conditional Expressions

# Example 1: Check Age

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)


# Example 2: Check Positive or Non-Positive

number = -5

result = "Positive" if number > 0 else "Zero or Negative"

print(result)


# Example 3: Check Even or Odd

number = 7

result = "Even" if number % 2 == 0 else "Odd"

print(result)


# Example 4: Check Exam Result

marks = 75

result = "Passed" if marks >= 40 else "Failed"

print(result)


# Example 5: Find the Greater Number

first_number = 25
second_number = 15

result = (
    "First number is greater"
    if first_number > second_number
    else "Second number is greater or equal"
)

print(result)


# Example 6: Check Password

password = "python123"

result = "Login successful" if password == "python123" else "Incorrect password"

print(result)


# Example 7: Apply a Simple Discount

purchase_amount = 6000

discount = 10 if purchase_amount >= 5000 else 0

print("Discount:", discount, "%")


# Example 8: Company Name Check

company_name = "Xenoriq Labs"

message = (
    "Welcome to Xenoriq Labs!"
    if company_name == "Xenoriq Labs"
    else "Unknown company"
)

print(message)


# Example 9: Check Temperature

temperature = 35

message = "Hot weather" if temperature > 30 else "Pleasant or cold weather"

print(message)


# Example 10: Select a Greeting

hour = 10

greeting = "Good morning" if hour < 12 else "Good afternoon"

print(greeting)


# Example 11: Nested Conditional Expression

marks = 85

grade = (
    "A" if marks >= 80
    else "B" if marks >= 70
    else "C" if marks >= 60
    else "D" if marks >= 40
    else "F"
)

print("Grade:", grade)


# Example 12: Choose a Username

is_admin = True

username = "Saif (Admin)" if is_admin else "Saif (User)"

print(username)