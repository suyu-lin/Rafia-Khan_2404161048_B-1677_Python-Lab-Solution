"""Write a Python program to demonstrate various ways ofaccessing the string.
(a) By using Indexing (Both Positive and Negative)
(b) By using Slice Operator"""
# Accessing string using Indexing
print("Accessing string using Indexing:")
str1 = "Hello, World!"
print(f"String: {str1}")
# Positive Indexing
print(f"Character at index 0: {str1[0]}")
print(f"Character at index 7: {str1[7]}")
# Negative Indexing
print(f"Character at index -1: {str1[-1]}")
print(f"Character at index -5: {str1[-5]}")
# Accessing string using Slice Operator
print("Accessing string using Slice Operator:")
print(f"Substring from index 0 to 4: {str1[0:5]}")
print(f"Substring from index 7 to end: {str1[7:]}")
print(f"Substring from index 2 to 7: {str1[2:8]}")
