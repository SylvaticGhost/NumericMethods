import numpy as np

def calculate_sum(x, xm, n):
    sum = 0
    for i in range(n):
        sum += (x[i] - xm[i]) ** 2
    return sum

x = [0, 8.881784197001252e-16, 4.440892098500626e-16, 0, 8.881784197001252e-16]

xm = [8.8817842e-16, 8.8817842e-16, 4.4408921e-16, 0.0000000e+00, 8.8817842e-16]

n = 5
mistake = np.sqrt((1/n)*calculate_sum(x, xm, n))

print("Похибка = ", mistake)

