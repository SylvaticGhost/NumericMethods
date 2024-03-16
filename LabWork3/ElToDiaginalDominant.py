import numpy as np

matrix = np.array([
    [8.3, 3.22, 4.1, 1.9, -10.65],
    [3.92, 8.45, 8.18, 2.46, 12.21],
    [3.77, 7.81, 8.04, 2.28, 14.85],
    [2.21, 3.65, 1.69, 6.99, -8.35] ])

print("Ділимо перший рядок на 8.3:")
matrix[0] /= 8.3
print(matrix)

print("Віднімаємо від друго перший рядок домножений на 3.92\n Від третього віднвмаємо перший домножений на 3.77 \n Від четвертого - перший на 2.91")

matrix[1] -= matrix[0] * 3.92
matrix[2] -= matrix[0] * 3.77
matrix[3] -= matrix[0] * 2.21

print(matrix)

print("Віднімаємо від друго третій рядок")
matrix[1] -= matrix[2]
print(matrix)

print("Від першого віднімаємо другий рядок\n Від третього перший домножений на 10")

matrix[0] -= matrix[1]
matrix[2] -= matrix[1] * 10
np.set_printoptions(suppress=True)
print(matrix)
