import numpy as np

A = np.array([
    [10.39, 2.45, 3.35, 2.28],
    [0, 6.027883, -0.732079, -0.125],
    [0, 0.789, 4.854, -0.0037],
    [0, -0.648, 0.051, 0.913]
])

A1 = np.array([
    [3.81, 0.25, 1.28, 1.75],
    [2.25, 1.32, 5.58, 0.49],
    [5.31, 7.28, 0.98, 1.04],
    [10.39, 2.45, 3.35, 2.28]
])

b1 = np.array([4.21, 7.47, 2.38, 11.48])
b = np.array([11.48, -3.487, 4.983, 0.000298])

x = np.linalg.solve(A, b)

d = np.array([1.1049085659287776, -0.578478381216092, 1.026576019777503, 0.00032639649507119385 ])
np.set_printoptions(suppress=True)
print("результат по не зведеній:")
print(np.linalg.solve(A1, b1))

print("результат по зведеній:")
print(x)

print("b + d")
print(b + d)

