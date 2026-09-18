# Create a sample tuple
t = (2,1,3,5,4)
print("Original Tuple:", t)

# (a) len()
print("\nLength of tuple:", len(t))

# (b) count()
print("Count of 3:", t.count(3))

# (c) index()
print("Index of 4:", t.index(4))

# (d) sorted()
sorted_list = sorted(t)
print("Sorted tuple (returns a list):", sorted_list)

# (e) min()
print("Minimum value:", min(t))

# (f) max()
print("Maximum value:", max(t))

# (g) reversed()
reversed_tuple = tuple(reversed(t))
print("Reversed tuple:", reversed_tuple)