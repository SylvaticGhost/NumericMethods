import numpy as np

epsilon = 1e-9

k = 3
a = k / 5

beta = k / 5
A1 = np.array([
            [8.30, 2.62 + a, 4.10, 1.90],
            [3.92, 8.45, 8.78 - a, 2.46],
            [3.77, 7.21 + a, 8.04, 2.28],
            [2.21, 3.65 - a, 1.69, 6.99]
        ])

b1 = np.array([-10.65, 12.21, 15.45 - beta, -8.35])

matrix = np.array([
    [ 1.0, -0.19385542, 0.42807229, 0.08325301, 1.16439759],
    [ 0.0, 0.58180723, 0.06590361, 0.14566265, -2.44753012],
    [ 0.0, 0.5293494, 5.5186747, -0.03963855, 44.16271084],
    [ 0.0, 2.79262651, 0.59831325, 6.48409639, -5.51427711]
])
A = matrix[:, :-1]
b = matrix[:, -1]

print("A =")
print(A)

print("b =")
print(b)

# print(A)
# n = A.shape[0]
# for i in range(n):
#   for j in range(n):
#     if i != j:
#       # Perform scaling: multiply off-diagonal element by a factor
#       factor = abs(A[i, i]) / (abs(A[i, i]) + abs(A[i, j]))
#       A[i, j] *= factor

print(A)


β = []
x = []

#calculate β and x
for i in range(A.shape[0]):
    x.append(b[i]/ A[i, i])
    row = []
    for j in range(A.shape[0]):
        if i != j:
            t = - float(A[i, j]) / float(A[i, i])
            row.append(t)
        else:
            row.append(0)
    β.append(row)


print("β =")
β = np.array(β)
print(β)

print("x =")
x = np.array(x)
print(x)

def solv(β, b, epsilon):
    x = b.copy()
    x_new = β @ x + b
    i = 0
    while np.linalg.norm(x_new - x) > epsilon:
        x = x_new.copy()
        x_new = β @ x + b
        i += 1

    print(f"iterations = {i}, x prev = {x}")
    return x_new

ans = solv(β, x, epsilon)

print("answer by Jacobi method =" )
print(ans)

#Solve by numpy function

ans2 = np.linalg.solve(A, b)

print("ans2 =")
print(ans2)


def Zeydel(A, x, b, epsilon):

    n = A.shape[0]

    x_new = x.copy()
    i = 0
    while np.linalg.norm(x_new - x) > epsilon:
        x = x_new.copy()

        x_new[0] = (b[0] - A[0, 1] * x_new[1] - A[0, 2] * x_new[2] - A[0, 3] * x_new[3]) / A[0, 0]
        x_new[1] = (b[1] - A[1, 0] * x[0] - A[1, 2] * x_new[2] - A[1, 3] * x_new[3]) / A[1, 1]
        x_new[2] = (b[2] - A[2, 0] * x_new[0] - A[2, 1] * x_new[1] - A[2, 3] * x_new[3]) / A[2, 2]
        x_new[3] = (b[3] - A[3, 0] * x_new[0] - A[3, 1] * x_new[1] - A[3, 2] * x_new[2]) / A[3, 3]
        i += 1


    return x_new

ans3 = Zeydel(A, np.array([0, 0, 0]),b, 0.000000001)

print("ans3 =")
print(ans3)








