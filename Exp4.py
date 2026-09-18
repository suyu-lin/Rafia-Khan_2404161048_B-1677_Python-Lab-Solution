"""Write simple Python program to demonstrate use of conditional statements:
   (a) ‘if’ statement, 
   (b) ‘if ... else’ statement and 
   (c) if – elif – else statement"""
# 'if' statement
print("Conditional Statements:\n")
print("‘if’ statement:\n")
x = 10
if x > 5:
    print(f"{x} is greater than 5")
# 'if ... else' statement
print("\n‘if ... else’ statement:\n")
y = 3
if y % 2 == 0:
    print(f"{y} is even")
else:
    print(f"{y} is odd")
# 'if – elif – else' statement
print("\n‘if – elif – else’ statement:\n")
z = 15
if z < 10:
    print(f"{z} is less than 10")
elif z < 20:
    print(f"{z} is between 10 and 20")
else:
    print(f"{z} is greater than or equal to 20")
