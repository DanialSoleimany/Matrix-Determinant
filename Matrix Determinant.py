# Code works on square matrices (matrices that have the same number of rows and columns)

import numpy as np

def determinant(matrix):
    determinant = np.linalg.det(matrix)
    return determinant

matrix = np.array([[5, 6],
                   [3, 5]])

print("Determinant of matrix 2x2:\n{0}".format(determinant(matrix)))
