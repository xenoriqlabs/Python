'''
Comments are text written in Python code to explain the code. Python ignores comments during program execution.

Comments are useful for making code easier to understand, maintain, and debug.
'''

# 1. Single-line Comments
'''
A single-line comment starts with the `#` symbol.

Everything after `#` on that line is treated as a comment.

```python
# This is a comment
print("Hello, Python!")
```

Python ignores the comment and executes:

```python
print("Hello, Python!")
```

### Comment after code

You can also place a comment after a statement:

```python
name = "Saif"  # Store the user's name
age = 25        # Store the user's age
```

### Commenting out code

Comments can temporarily disable a line of code:

```python
print("Hello")

# print("This line will not execute")

print("Python is easy!")
```

Output:

```text
Hello
Python is easy!
```
'''

# 2. Multi-line Comments
'''
Python does not have a dedicated multi-line comment syntax.

The recommended approach is to use `#` on each line:

```python
# This program calculates
# the total price of a product
# based on price and quantity.

price = 100
quantity = 3
total = price * quantity

print(total)
```

Each line beginning with `#` is a separate comment.

### Triple-quoted strings

You may also see triple-quoted strings used for multiple lines:

```python
"""
This is a multi-line string.
It can contain multiple lines.
"""
```

However, this is technically not a comment.

It is a string literal that is not assigned to a variable. Triple-quoted strings are primarily used for docstrings.

For example:

```python
def greet():
    """Display a greeting message."""
    print("Hello, Python!")
```

The string inside the function is a docstring, which can be used to document what the function does.

Therefore, for actual comments, prefer:

```python
# First comment
# Second comment
# Third comment
```
'''

# 3. Comments Best Practices
'''
Good comments should make your code easier to understand, not make it more complicated.

### 1. Write meaningful comments

Good:

```python
# Calculate the total cost
total = price * quantity
```

Less useful:

```python
# Multiply price by quantity
total = price * quantity
```

The second comment simply describes what the code obviously does.

### 2. Explain why, not just what

Prefer explaining the reason behind unusual code.

Good:

```python
# Add a small delay to prevent excessive API requests
time.sleep(1)
```

This explains why the delay exists.

### 3. Keep comments concise

Avoid unnecessarily long comments.

Good:

```python
# Convert temperature from Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32
```
'''

# 4. Keep comments up to date
'''
If you change your code, update related comments as well.

Bad:

```python
# Calculate the discount for premium users
discount = 10
```

If the code later changes to calculate a tax, the old comment becomes misleading.
'''

# 5. Use comments to explain complex logic
'''
Comments are especially useful when the logic isn't immediately obvious:

```python
# Apply the discount only when the order exceeds $100
if total > 100:
    total *= 0.90
```
'''

# 6. Don't over-comment obvious code
'''
Avoid:

```python
# Create a variable called name
name = "Saif"

# Print the name
print(name)
```

Better:

```python
name = "Saif"
print(name)
```

The code is already easy to understand.
'''

# 7. Use consistent formatting
'''
A common style is to place a space after `#`:

```python
# Good comment
```

Instead of:

```python
#Bad comment
```

For inline comments, leave enough spacing:

```python
age = 25  # User's age
```
'''