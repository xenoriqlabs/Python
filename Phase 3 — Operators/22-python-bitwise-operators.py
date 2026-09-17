# ==========================================
# Binary Representation
# ==========================================

# bin() converts a decimal number
# into its binary representation.

number1 = 5
number2 = 3

print("Binary Representation:")
print("5 in binary:", bin(number1))
print("3 in binary:", bin(number2))

# ==========================================
# 1. Bitwise AND (&)
# ==========================================

# AND:
# 1 & 1 = 1
# 1 & 0 = 0
# 0 & 1 = 0
# 0 & 0 = 0

a = 5
b = 3

result = a & b

print("\nBitwise AND (&):")
print("5 & 3 =", result)
print("Binary:", bin(result))

# Manual representation:
#
#     0101   = 5
#     0011   = 3
#     ----
#     0001   = 1

# ==========================================
# 2. Bitwise OR (|)
# ==========================================

# OR:
# 1 | 1 = 1
# 1 | 0 = 1
# 0 | 1 = 1
# 0 | 0 = 0

a = 5
b = 3

result = a | b

print("\nBitwise OR (|):")
print("5 | 3 =", result)
print("Binary:", bin(result))

# Manual representation:
#
#     0101   = 5
#     0011   = 3
#     ----
#     0111   = 7

# ==========================================
# 3. Bitwise XOR (^)
# ==========================================

# XOR:
# Same bits  -> 0
# Different  -> 1

a = 5
b = 3

result = a ^ b

print("\nBitwise XOR (^):")
print("5 ^ 3 =", result)
print("Binary:", bin(result))


# Manual representation:
#
#     0101   = 5
#     0011   = 3
#     ----
#     0110   = 6

# ==========================================
# 4. Bitwise NOT (~)
# ==========================================

# NOT reverses bits.
#
# Python uses signed integers,
# so ~n = -(n + 1)

number = 5

result = ~number

print("\nBitwise NOT (~):")
print("~5 =", result)

number = 10

print("~10 =", ~number)

# ==========================================
# 5. Left Shift (<<)
# ==========================================

# Left shift moves bits to the left.
#
# For positive integers:
#
# n << 1 ≈ n * 2
# n << 2 ≈ n * 4

number = 5

result1 = number << 1
result2 = number << 2

print("\nLeft Shift (<<):")
print("5 << 1 =", result1)
print("5 << 2 =", result2)

print("Binary of 5:", bin(5))
print("Binary of 5 << 1:", bin(result1))
print("Binary of 5 << 2:", bin(result2))

# ==========================================
# 6. Right Shift (>>)
# ==========================================

# Right shift moves bits to the right.
#
# For positive integers:
#
# n >> 1 ≈ n / 2
# n >> 2 ≈ n / 4

number = 20

result1 = number >> 1
result2 = number >> 2

print("\nRight Shift (>>):")
print("20 >> 1 =", result1)
print("20 >> 2 =", result2)

print("Binary of 20:", bin(20))
print("Binary of 20 >> 1:", bin(result1))
print("Binary of 20 >> 2:", bin(result2))

# ==========================================
# 7. Practical AND Example
# ==========================================

# Check whether specific bits are enabled.

permissions = 5
required_permission = 1

if permissions & required_permission:
    print("\nAND Practical Example:")
    print("Permission is enabled")
else:
    print("\nAND Practical Example:")
    print("Permission is not enabled")

# ==========================================
# 8. Practical OR Example
# ==========================================

a = 4
b = 2

result = a | b

print("\nOR Practical Example:")
print("4 | 2 =", result)
print("Binary:", bin(result))

# ==========================================
# 9. Practical XOR Example
# ==========================================

a = 10
b = 6

result = a ^ b

print("\nXOR Practical Example:")
print("10 ^ 6 =", result)
print("Binary:", bin(result))

# ==========================================
# 10. Shift Example
# ==========================================

number = 8

double = number << 1
half = number >> 1

print("\nShift Practical Example:")
print("Original:", number)
print("Double using <<:", double)
print("Half using >>:", half)

# ==========================================
# 11. All Operators Together
# ==========================================

a = 12
b = 5

print("\nAll Bitwise Operators:")

print("a =", a)
print("b =", b)

print("a & b  =", a & b)
print("a | b  =", a | b)
print("a ^ b  =", a ^ b)
print("~a     =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)


# ==========================================
# 12. Binary Results
# ==========================================

print("\nBinary Results:")

print("a:", bin(a))
print("b:", bin(b))

print("a & b:", bin(a & b))
print("a | b:", bin(a | b))
print("a ^ b:", bin(a ^ b))
print("a << 1:", bin(a << 1))
print("a >> 1:", bin(a >> 1))
