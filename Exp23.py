import numpy as np
a = np.array([[10, 20, 30],[40, 50, 60]])
print("Created NumPy Array:\n",a)
# (a) Type of array
print(f"\nType of array: {type(a)}")
# (b) Axes of array (Number of dimensions)
print(f"Axes of array: {a.ndim}")
# (c) Shape of array (rows, columns)
print(f"Shape of array: {a.shape}")
# (d) Type of elements in array
print(f"Type of elements in array: {a.dtype}")