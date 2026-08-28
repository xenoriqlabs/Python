# Python data types define what kind of value a variable stores. 
# Different data types have different properties and are used for different purposes.

# 1. Numeric

# Integer
age = 22
print(age)
print(type(age))

# Float
price = 99.99
print(price)
print(type(price))

# Complex
number = 3 + 4j
print(number)
print(type(number))

# Practical example

product_price = 1500
quantity = 3

total = product_price * quantity

print("Total Price:", total)

# 2. String

name = 'Saif'
city = "Sahiwal"

print(name)
print(city)

# Practical example

first_name = "Saif Ur"
last_name = """Rahman"""

full_name = first_name + " " + last_name

print(full_name)

# You can also access individual characters:

language = "Python"

print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[-1])     # last character

# 3. Boolean

is_logged_in = True
is_admin = False

print(is_logged_in)
print(is_admin)

print(type(is_logged_in))

# Practical example

age = 22

is_adult = age >= 18

print(is_adult)

# Another example

password = "12345"

is_correct = password == "12345"

print(is_correct)

# 4. List (mutable - Ordered - Allow duplicate values - Written using [ ])

# A list stores multiple values in a single variable.

mixed = ["Banana", "Mango", "Orange", 23, 34.8, ]

print(mixed)
print(type(mixed))

# You can access items using indexes:

print(mixed[0])
print(mixed[-1])

# Lists can be modified:

mixed[-1] = "Saif"

print(mixed)

# Practical example

students = ["Saif", "Ali", "Ahmad", "Awais"]
print("Students:", students)

students.append("Wajid")

print("Updated Students:", students)

# 5. Tuple (Immutable - Ordered - Allow duplicate values - Usually written using ( ))

# A tuple is similar to a list, but it cannot be changed after creation.

mixed = ("Saif", "Sahiwal", 22, 178.8, "Anwar Tahir")

print(mixed)
print(type(mixed))

# You can access tuple items using indexes:

print(mixed[2])
print(mixed[-2])

# Practical example

# Use a tuple when the data should remain fixed:

coordinates = (31.4504, 73.1350)

print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])

# 6. Set (Unordered - Mutable - Do not allow duplicate values - Written using { })

# A set is a collection of unique values.

numbers = {10, 20, 30, 40}

print(numbers)
print(type(numbers))

# Duplicate values are automatically removed

numbers = {10, 20, 20, 30, 30, 30}

print(numbers)

# Practical example (Suppose you have duplicate usernames)

usernames = {"ali", "saif", "ali", "ahmad", "saif"}

print(usernames)

# You can add values

skills = {"Python", "JavaScript", "MongoDB"}

skills.add("React.js")
print(skills)

# 7. Dictionary

# A dictionary stores data in key-value pairs.

student = {
    "Name" : "Saif",
    "Age" : 22,
    "City" : "Sahiwal"
}

print(student)
print(type(student))

# You access values using their keys:

print(student["Name"])
print(student["Age"])
print(student["City"])

# You can modify values:

student["Age"] = 24
print(student)

# You can also add a new key:

student["Email"] = "drsaiftahir560@gmailcom"
print(student)

# Practical example

# Dictionaries are very useful for representing real-world objects:

product = {
    "name" : "Laptop",
    "price" : 150000,
    "brand" : "Dell",
    "in_stock" : True
}

print("Product:", product["name"])
print("Price:", product["price"])
print("Brand:", product["brand"])
print("Available:", product["in_stock"])

# 8. None

# None represents no value or absence of a value.

result = None

print(result)
print(type(result))

# Practical example

# Suppose a user has not provided an email yet:

name = 'Saif'
email = None

print("Name:", name)
print("Email:", email)

# Later, you can assign a value:

email = "drsaiftahir560@gmail.com"

print(email)

# Checking for None

# Use is None:

email = None

if email is None:
    print("Email has not been provided.")