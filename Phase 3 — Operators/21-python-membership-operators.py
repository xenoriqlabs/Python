# ==========================================
# 1. 'in' Operator with List
# ==========================================

# 'in' checks whether a value exists
# inside a collection.

fruits = ['apple', 'banana', 'mango', 'orange']

print("IN Operator:")
print("apple" in fruits)
print("banana" in fruits)
print("grapes" in fruits)

# ==========================================
# 2. 'not in' Operator with List
# ==========================================

print('\nNOT IN Operator:')

print('grapes' not in fruits)
print('apple' not in fruits)

# ==========================================
# 3. 'in' Operator with String
# ==========================================

company = 'Xenoriq Labs'

print("\nString Membership:")

print('Xenoriq' in company)
print('Labs' in company)
print('Pyhton' in company)

# ==========================================
# 4. 'not in' Operator with String
# ==========================================

print("\nString NOT IN:")

print("Python" not in company)
print("Xenoriq" not in company)

# ==========================================
# 5. Character Membership
# ==========================================

name = "Saif"

print("\nCharacter Membership:")

print("S" in name)
print("a" in name)
print("z" in name)

# ==========================================
# 6. Tuple Membership
# ==========================================

languages = (
    "python",
    "C++",
    "JavaScript",
    "Java"
)

print("\nTuple Membership:")

print("Python" in languages)
print("C++" in languages)
print("PHP" in languages)

print("PHP" not in languages)
print("Python" not in languages)

# ==========================================
# 7. Set Membership
# ==========================================

skills = {
    "Python",
    "C++",
    "JavaScript",
    "React",
    "Node.js"
}

print("\nSet Membership:")

print("Python" in skills)
print("React" in skills)
print("Flutter" in skills)

print("Flutter" not in skills)

# ==========================================
# 8. Dictionary Membership
# ==========================================

student = {
    "name": "Saif",
    "age": 20,
    "city": "Sahiwal"
}

print("\nDictionary Membership:")

# 'in' checks dictionary keys.

print("name" in student)
print("age" in student)
print("email" in student)


# ==========================================
# 9. Checking Dictionary Values
# ==========================================

print("\nDictionary Values:")

print("Saif" in student.values())
print("Lahore" in student.values())

print("Lahore" not in student.values())

# ==========================================
# 10. Practical Course Example
# ==========================================

courses = [
    "Python",
    "C++",
    "CSS3",
    "JavaScript",
    "AI/ML"
]

course = 'Pyhton'

print("\nCourse Availability:")

if course in courses:
    print("Course is available")
else:
    print("Course is not available")

# ==========================================
# 11. Course Not Available Example
# ==========================================

course = "Flutter"

if course not in courses:
    print("Flutter course is not available")
else:
    print("Flutter course is available")

# ==========================================
# 12. Username Check
# ==========================================

usernames = [
    "Saif",
    "Ali",
    "Ahmed",
    "Usman"
]

username = "Saif"

print("\nUsername Check:")

if username in usernames:
    print("Username already exists")
else:
    print("Username is available")


# ==========================================
# 13. Email Domain Check
# ==========================================

email = "saif@xenoriqlabs.com"

print("\nEmail Check:")

if "@xenoriqlabs.com" in email:
    print("This is a Xenoriq Labs email")
else:
    print("This is not a Xenoriq Labs email")

# ==========================================
# 14. Search Example
# ==========================================

description = "Xenoriq Labs builds modern software and AI solutions."

search_word = 'AI'

print("\nSearch Example:")

if search_word in description:
    print("Search word found")
else:
    print("Search word not found")

# ==========================================
# 15. Combining Membership Operators
# ==========================================

programming_languages = [
    "Pyhton",
    "C++",
    "JavaScript"
]

language = "Pyhton"

print("\nLanguage Check:")

if language in programming_languages:
    print(language, "is supported")
    
if "Java" not in programming_languages:
    print("Java is not in the list")
