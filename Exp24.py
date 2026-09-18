import numpy as np
A = np.array([[1, 2], [3, 4]])
print("Matrix A:\n",A)
print("Matrix Multiplication (A x A):\n",np.dot(A, A))
print("Transpose of A:\n",A.T)
print(f"Determinant of A: {np.linalg.det(A):.2f}")
print("Inverse of A:\n",np.linalg.inv(A))
print(f"Mean of A: {np.mean(A):.2f}")
print(f"Median of A: {np.median(A):.2f}")
print(f"Standard Deviation of A: {np.std(A):.2f}")
print("Cumulative Sum of A:", np.cumsum(A))

