# Escape sequences are special characters written with a backslash \ inside a Python string. 
# They are used to control formatting or represent special characters.

# 1. \n — New Line

print("Name: Saif\nAge: 22\nCity: Sahiwal")

# 2. \t — Tab

print("Name:\tSaif")
print("Age:\t22")
print("City:\tSahiwal")

# Useful for making simple columns:

print("Name\tAge\tCity")
print("Ali\t20\tLahore")
print("Ahmed\t25\tMultan")

# 3. \\ — Backslash

# A single \ has a special meaning in Python strings.
# If you actually want to print a backslash, use \\.

print("C:\\users\\saif\\documents")

# 4. \" — Double Quote

# Used to print a double quote inside a string enclosed by double quotes.

print("He said, \"Hello\".")

# You can also avoid escaping by using single quotes:

print('He said, "Hello".')

# 5. \' — Single Quote

# Used to print a single quote inside a string enclosed by single quotes.

print('It\'s Python.')

# You can also use double quotes:

print("It's Python.")

# 6. \r — Carriage Return

# \r moves the cursor back to the beginning of the current line.

print("Hello\rWorld")

# A more practical example:

print("Loading...\rDone!")

# 7. \b — Backspace

# \b moves the cursor one position backward.
# It does not automatically delete the character.

print("Helloo\b")