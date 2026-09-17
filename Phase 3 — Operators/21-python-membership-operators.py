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