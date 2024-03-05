
import numpy as np
from sympy import symbols, solve, Eq, linsolve

def check_if_matrix_symetric(matrix) -> bool:
    return (np.array_equal(matrix.transpose(), matrix))

#Init part

n_var = 25

k1 = abs(n_var - 25)

a : float = k1/4

k2 = abs(n_var - 21)

beta = 0.35*k2

A = np.array([[5.18 + a, 1.12, 0.95,  1.32, 0.83],
             [1.12, 4.28-a, 2.12, 0.57, 0.91],
             [0.95, 2.12, 6.13 + a, 1.29, 1.57],
             [1.32, 0.57, 1.29, 4.57 - a, 1.25],
                [0.83, 0.91, 1.57, 1.25, 5.21 + a]])

B = np.array([7.59, 3.21, 2.88, 6.25, 6.35])

size = 5

print("Вихідна матриця A = ")
print(A)

print("Вихідний вектор B = ")
print(B)

print(f'Чи є матриця симетричною: {check_if_matrix_symetric(A)}\n')

u = [[0, 0 ,0, 0, 0],
                [0, 0 ,0, 0, 0],
                [0, 0 ,0, 0, 0],
                [0, 0 ,0, 0, 0],
                [0, 0 ,0, 0, 0]]

u[0][0] = np.sqrt(A[0][0])
u[0][1] = A[0][1] / u[0][0]
u[0][2] = A[0][2] / u[0][0]
u[0][3] = A[0][3] / u[0][0]
u[0][4] = A[0][4] / u[0][0]

u[1][1] = np.sqrt(A[1][1] - u[0][1]**2)
u[1][2] = (A[1][2] - u[0][1]*u[0][2]) / u[1][1]
u[1][3] = (A[1][3] - u[0][1]*u[0][3]) / u[1][1]
u[1][4] = (A[1][4] - u[0][1]*u[0][4]) / u[1][1]

u[2][2] = np.sqrt(A[2][2] - u[0][2]**2 - u[1][2]**2)
u[2][3] = (A[2][3] - u[0][2]*u[0][3] - u[1][2]*u[1][3]) / u[2][2]
u[2][4] = (A[2][4] - u[0][2]*u[0][4] - u[1][2]*u[1][4]) / u[2][2]

u[3][3] = np.sqrt(A[3][3] - u[0][3]**2 - u[1][3]**2 - u[2][3]**2)
u[3][4] = (A[3][4] - u[0][3]*u[0][4] - u[1][3]*u[1][4] - u[2][3]*u[2][4]) / u[3][3]

u[4][4] = np.sqrt(A[4][4] - u[0][4]**2 - u[1][4]**2 - u[2][4]**2 - u[3][4]**2)

U = np.array(u)
print("U = ")
print(U)

UT = U.transpose()


Y = np.linalg.solve(UT, B)
print("Y = ")
print(Y)

X = np.linalg.solve(U, Y)
print("шуканий вектор X = ")
print(X)

vectorNeViazky = B - A@X
print("Вектор нев'язки= ")
print(vectorNeViazky)



