import numpy as np

matrix = np.array([
    [8.3, 3.22, 4.1, 1.9, -10.65],
    [3.92, 8.45, 8.18, 2.46, 12.21],
    [3.77, 7.81, 8.04, 2.28, 14.85],
    [2.21, 3.65, 1.69, 6.99, -8.35] ])

matrix[0] /= 8.3

print("Matrix after dividing the first row by 8.3:")
print(matrix)

matrix[1] -= matrix[0] * 3.92
matrix[2] -= matrix[0] * 3.77
matrix[3] -= matrix[0] * 2.21

print("Matrix after subtracting the first row from the other rows:")
print(matrix)

matrix[1] -= matrix[2]

print("Matrix after subtracting the second row from the third row:")

print(matrix)

matrix[0] -= matrix[1]
matrix[2] -= matrix[1] * 10

print("Matrix after subtracting the second row from the first row and the third row from the second row:")


np.set_printoptions(suppress=True)
print(matrix)
