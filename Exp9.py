"""Python program to perform following operations on Tuples: 
   a) Create Tuple, b) Access Tuple, c) Update Tuple and 
   d) Delete Tuple"""
# a) Create Tuple
Ttuple = (10, 20, 30, 40, 50)
print("Created Tuple:",Ttuple)

# b) Access Tuple
print("Element at index 1:", Ttuple[1])
print("Last element (negative indexing):", Ttuple[-1])

# c) Update Tuple 
# Tuples are immutable, so we convert to a list first
print("\nUpdate tuple")
list = list(Ttuple)
list[2] = 99  # Changing the 3rd element
Ttuple = tuple(list)
print("Updated Tuple:", Ttuple)

# d) Delete Tuple
del Ttuple
print("Tuple has been deleted successfully.")
# print(my_tuple) # Uncommenting this line would cause a NameError