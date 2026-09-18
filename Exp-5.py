"""Write Python program to demonstrate use of looping statements: 
(a) ‘while’ loop,
(b) ‘for’ loop and 
(c) Nested loops"""
# 'while' loop
print("Looping Statements:")
print("‘while’ loop:")
print("Print numbers from 1 to 5 using while loop:")
i = 1
while i <= 5:
    print(f"{i}")
    i += 1
print("---------------------------------------------------------------------")
# 'for' loop
print("‘for’ loop:")
print("Table of 2 using for loop:")
for j in range(1, 11):
    print(f"2 x {j} = {2 * j}")
print("---------------------------------------------------------------------")
# Nested loops
print("Nested loops:")
print("Matrix of 2 x 3 using nested loops:")
for k in range(1, 3):
    for l in range(1, 4):
        print(f"{1}",end = " ")
    print()  # for new line after each row