import numpy as np

v1 = np.array([1, 2, 7])
v2 = np.array([9, 8, 3])

print("v1 + v2:")
print(v1 + v2)

print("v1 - v2:")
print(v1 - v2)

print("v1 * v2:")
print(v1*v2)

print("v1 x v2:")
print(np.outer(v1, v2))

print('\n')
#matrix

A = np.array([[1, 2], [3, 4]])

B = np.array([[4, 5], [11, 4]])

print("A + B:")
print(A + B)

print("A * B:")
print(np.dot(A, B))


print("A транспонована:")
print(A.T)

print("детермінант матриці А")
print(np.linalg.det(A))


