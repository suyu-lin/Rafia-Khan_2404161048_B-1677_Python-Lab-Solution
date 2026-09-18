import numpy as np

# (a) Empty and Full NumPy array
empty = np.empty((2, 2))
full = np.full((2, 2), 3)
print("Empty Array:\n", empty)
print("Full Array:\n", full)

# (b) Array filled with all zeros and all ones

print(f"Zeros Array:\n {np.zeros((2, 2))}")
print(f"Ones Array:\n  {np.ones((2, 2))}")

# (c) Maximum and minimum value from a matrix
m= np.array([[10, 5], [3, 8]])
print("Matrix:\n", m)
print("Maximum value:", m.max())
print("Minimum value:", m.min())

# (d) Eigen values of a matrix
print(f"Eigenvalues of matrix: {np.linalg.eigvals(m)}")

# (e) NumPy array with random values
random = np.random.rand(2, 2) # 2x2 array of random floats between 0 and 1
print("Random Array:\n", random)

# (f) Floor, ceiling, and truncated values
float = np.array([1.5, -2.8, 3.1, -4.9])
print("Original Float Array:", float)
print("Floor values:", np.floor(float))
print("Ceiling values:", np.ceil(float))
print("Truncated values:", np.trunc(float))

# (g) Subtract one polynomial from another
# p1 = x^2 + 2x + 3, p2 = x + 1
p1 = np.array([1, 2, 3])
p2 = np.array([1, 1]) 
print(f"Subtraction Result: {np.polynomial.polynomial.polysub(p1, p2)}")

# (h) Roots of a polynomial
# Polynomial: x^2 - 3x + 2 = 0
print(f"Roots of polynomial x^2 - 3x + 2 = 0: {np.roots([1, -3, 2] )}")

# (i) Convert list and tuple into NumPy arrays
print(f"List to Array: {np.array([1, 2, 3])}")
print(f"Tuple to Array: {np.array((4, 5, 6))}")