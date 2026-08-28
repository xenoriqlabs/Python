#===========================
# 1. True
#===========================

# True represents a condition or value that is correct / yes / enabled.

is_logged_in = True
is_active = True
has_permission = True

print(is_logged_in)
print(is_active)
print(has_permission)

# The type is bool:

is_logged_in = True

print(type(is_logged_in))

#============================
# 2. False
#============================

# False represents a condition or value that is incorrect / no / disabled.

is_logged_in = False
is_admin = False
has_permission = False

print(is_logged_in)
print(is_admin)
print(has_permission)

# Example:

is_raining = False

if is_raining:
    print("Take an umbrella.")
else:
    print("You don't need an umbrella.")

#===================================
# Practical Example — Login System
#===================================

username = "admin"
password = '12345'

is_logged_in = username == "admin" and password == "12345"

print(is_logged_in)

#==========================
# 3. Truthy
#==========================

# A value is Truthy when Python treats it as True in a condition, 
# even if the value itself isn't literally True.

name = "Saif"

if name:
    print("Name exists.")

print(bool("Saif"))
print(bool(100))
print(bool(-5))
print(bool([1, 2, 3]))
print(bool({"name": "Saif"}))

#==========================
# 4. Falsy
#==========================

# A value is Falsy when Python treats it as False in a condition.

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))

# Practical Example — Checking a Username

username = ""

if username:
    print("Username entered.")
else:
    print("Username is empty.")

# ===================================
# Practical Example — Shopping Cart
# ===================================

cart = ["Laptop", "Mouse"]

if cart:
    print("Cart has products.")
else:
    print("Cart is empty.")

# bool() Function

# The bool() function converts a value into a Boolean.