"""
In Python, None is a special value that means:

    -> “There is no value” / “Nothing is currently assigned.”

    -> It is not 0, False, or an empty string.
"""

# 1. None
# You can assign None to a variable when you don't have a value yet.

name = None

print(name)

# Example:
username = None
username = 'Saif'   # Later, we get the username

print("Username is:", username)

# 2. Checking None with is None
# when you want to check whether a variable contains exactly None.

username = None

if username is None:
    print("Username is not available...")

# Another example:
result = None

if result is None:
    print("No result found...")
else:
    print("Result found")

# 3. is not None
# This checks whether a variable has some value other than None.

username = 'Saif'

if username is not None:
    print("Username is availabe")

# Another practical example:
email = None

if email is not None:
    print("Email:", email)
else:
    print("Email is missing...")