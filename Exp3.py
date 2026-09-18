"""Write simple Python program using following operators:
   (a) Arithmetic Operators 
   (b) Relational Operators
   (c) Assignment Operator 
   (d) Logical Operators 
   (e) Bit wise Operators 
   (f) Ternary Operator 
   (g) Membership Operators and 
   (h) Identity Operators"""
# Arithmetic Operators
a = 10
b = 5
print("Arithmetic Operators:\n")
print(f"a = {a}, b = {b}")
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ** b}")
print(f"Floor Division: {a // b}")
print("---------------------------------------------------------------------")
# Relational Operators
print("Relational Operators:\n")
print(f"a = {a}, b = {b}")
print(f"Equal: {a == b}")
print(f"Not Equal: {a != b}")
print(f"Greater Than: {a > b}")
print(f"Less Than: {a < b}")
print(f"Greater Than or Equal To: {a >= b}")
print(f"Less Than or Equal To: {a <= b}")
print("---------------------------------------------------------------------")
# Assignment Operator
print("Assignment Operator:\n")
c = 10
print(f"Initial value of c: {c}")
c += 5
print(f"Assignment (c += 5): {c}")
print("---------------------------------------------------------------------")
# Logical Operators
print("Logical Operators:\n")
d = True
e = False
print(f"d = {d}, e = {e}")
print(f"Logical AND: {d and e}")
print(f"Logical OR: {d or e}")
print(f"Logical NOT: {not d}")
print("---------------------------------------------------------------------")
# Bitwise Operators
print("Bitwise Operators:\n")
f = 10  # 1010 in binary
g = 4   # 0100 in binary
print(f"f = {f}, g = {g}")
print(f"Bitwise AND: {f & g}")
print(f"Bitwise OR: {f | g}")
print(f"Bitwise XOR: {f ^ g}")
print(f"Bitwise NOT: {~f}")
print("---------------------------------------------------------------------")
# Ternary Operator
print("Ternary Operator:\n ")
h = 20
i = 30
print(f"h = {h}, i = {i}")
print(f"Ternary Operator: {'h is greater' if h > i else 'i is greater'}")
print("---------------------------------------------------------------------")
# Membership Operators
print("Membership Operators:\n")
j = [1, 2, 3, 4, 5]
print(f"j = {j}")
print(f"Membership (3 in j): {3 in j}")
print(f"Membership (6 not in j): {6 not in j}")
print("---------------------------------------------------------------------")
# Identity Operators
print("Identity Operators:\n")
k = 10
l = 10
print(f"k = {k}, l = {l}")
print(f"Identity (k is l): {k is l}")
print("---------------------------------------------------------------------")