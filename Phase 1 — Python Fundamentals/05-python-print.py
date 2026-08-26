# The print() function is used to display output on the screen.
# It is one of the most commonly used functions in Python.


# --> 1. print()

print("Hello, Xenoriq Labs!")   # Basic syntax

print(100)                      # You can print numbers
print(20 + 30)


name = "Saif"
age = 23

print(name)                     # You can also print variables
print(age)


print("Hello")
print()                         # Calling print() without an argument prints a blank line
print("Python")


# --> 2. Multiple Values

name = "Saif"
age = 22

print(name, age)                # print() can accept multiple values separated by commas


name = "Saif"
age = 22
salary = 50000

print(name, age, salary)        # You can print different types of values together

print("Hello", "Python", "World")   # By default, Python places a space between values


# --> 3. sep

print("Hello", "Python", "World", sep="-")
print("2026", "8", "22", sep="-")
print("Python", "Programming", sep="")
print("HTML", "CSS", "Python", sep=" | ")

print("Hello", sep="-")         # sep has no effect with a single value


# --> 4. end

print("Hello")
print("World")

print("Hello", end=" ")         # Instead of moving to a new line, print() ends with a space
print("World")

print("Loading", end="...")
print("Done")


# --> 5. Escape Characters

print("Hello\nWorld")           # \n — New Line
print("Name: Saif\nAge: 22")

print("Hello\tWorld")           # \t — Tab
print("Name\tAge")
print("Saif\t22")

print("C:\\Users\\devsa")       # \\ — Backslash

print("He said, \"Hello!\"")    # \" — Double Quote

print("It's Python!")           # Single quote inside double quotes

print('It\'s Python!')          # \' — Single Quote

print("Hello\rPython")          # \r — Moves the cursor to the beginning of the current line

print("Helloo\b!")              # \b — Moves the cursor one position backward


# --> sep + end Together

print("2026", "08", "22", sep="-", end="\n")
print("Hello", "Python", sep=" | ", end="!")