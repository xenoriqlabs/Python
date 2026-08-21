# 1. Python Syntax
'''
Python syntax refers to the rules that define how Python code must be written.

Python syntax is designed to be simple and readable.

For example:
```python
print("Hello, Python!")
```

Here:
    `print()` is a built-in Python function.
    `"Hello, Python!"` is a string.
     Python executes the statement and displays the text.

Another example:
```python
name = "Saif"
age = 25
print(name)
print(age)
```
Python uses indentation instead of curly braces `{}` to define blocks of code.
'''

# 2. Statements
'''
A statement is an instruction that Python can execute.

Example:
```python
name = "Saif"
age = 25
print(name)
print(age)
```

Each line represents a statement.

Python also allows multiple statements on separate lines:
```python
x = 10
y = 20
z = x + y
print(z)
```

### Multiple statements on one line

Python technically allows multiple statements on one line using `;`:
```python
x = 10; y = 20; print(x + y)
```
However, this is generally not recommended because separate lines are easier to read.

Prefer:
```python
x = 10
y = 20
print(x + y)
```
'''

# 3. Indentation
'''
Indentation means adding spaces at the beginning of a line.

Python uses indentation to define which statements belong to a particular code block.

Example:
```python
age = 20
if age >= 18:
    print("You are an adult.")
```
The indented line belongs to the `if` block.

Python commonly uses 4 spaces for indentation:

```python
if True:
    print("This is inside the block.")
```

### Incorrect indentation
```python
if True:
print("Hello")
```
This produces an `IndentationError`.

### Important

Do not randomly mix tabs and spaces. The standard practice is:
```text
4 spaces = 1 indentation level
```
'''

# 4. Comments
'''
Comments are notes written inside code for developers. Python ignores comments during execution.

A single-line comment starts with `#`:
```python
# This is a comment
print("Hello")
```

You can also write a comment after code:
```python
name = "Saif"  # Store the user's name
```

Comments are useful for explaining code:
```python
# Calculate the total price
price = 100
quantity = 3
total = price * quantity

print(total)
```

### Multi-line comments

Python does not have a dedicated multi-line comment syntax like some other languages.
You can use multiple `#` lines:

```python
# This program calculates
# the total price of
# multiple products.

price = 100
quantity = 3
```

Triple-quoted strings can also span multiple lines:

```python
"""
This is a multi-line string.
It is not technically a comment.
"""
```
So, for actual comments, prefer `#`.
'''

# 5. Case Sensitivity
'''
Python is case-sensitive.
This means uppercase and lowercase letters are treated as different characters.

For example:
```python
name = "Saif"
Name = "Ali"

print(name)
print(Name)
```
Output:
```text
Saif
Ali
```

Here:
```text
name
Name
```
are two different variables.

Python also distinguishes between:
```python
print()
```

and:

```python
Print()
```

`print()` is correct because Python's built-in function is written in lowercase.
```python
print("Hello")
```

But:

```python
Print("Hello")
```

will produce an error because `Print` is not the same as `print`.
'''

# 6. Code Blocks
'''
A code block is a group of statements that belong together.

Python uses indentation to define code blocks.

For example:
```python
age = 20

if age >= 18:
    print("You are an adult.")
    print("You can vote.")
```

Both `print()` statements belong to the `if` block because they are indented.

### Multiple code blocks

```python
age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

Here there are two code blocks:

```text
if block
    ↓
    print("You are an adult.")

else block
    ↓
    print("You are a minor.")
```

### Nested code blocks

A code block can exist inside another code block:

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Access granted.")
```

The indentation shows the relationship:

```text
if age >= 18:
    └── if has_id:
            └── print()
```

### Key Rule

In Python:

```text
Colon (:) + indentation
        ↓
     Code Block
```

For example:

```python
if condition:
    statement
```

This concept is extremely important because Python uses indentation instead of `{}` to structure programs.
'''