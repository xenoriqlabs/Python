# --> 1. type()

name = "Saif"
age = 25
height = 5.9
is_student = True

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>

# --> 2. type() with different data types

print(type(10))          # int
print(type(10.5))        # float
print(type("Hello"))     # str
print(type(True))        # bool
print(type(None))        # NoneType

# --> 3. isinstance()

# isinstance() checks whether a value is of a specific data type or not.

age = 25

print(isinstance(age, int))    # True
print(isinstance(age, str))    # False
print(isinstance(age, float))  # False

# isinstance() with Variables

name = "Saif"
age = 25
price = 99.99
is_active = True

print(isinstance(name, str))       # True
print(isinstance(age, int))        # True
print(isinstance(price, float))    # True
print(isinstance(is_active, bool)) # True

# --> 4. Check Multiple Types

# You can use a tuple in `isinstance()` to check multiple data types

value = 10

print(isinstance(value, (int, str)))

value = "10"

print(isinstance(value, (int, float)))  # False

# 1. `type()` → tells you the exact type.
# 2. `isinstance()` → checks whether an object is an instance of a given type.
# 3. For general type checking, `isinstance()` is more useful.