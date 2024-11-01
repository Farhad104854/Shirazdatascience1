# s1.py
import numpy as np

# جمع دو ماتریس
def add_matrices(a, b):
    return np.add(a, b)

if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print("Sum of matrices:\n", add_matrices(A, B))
