import numpy as np

n = 4

xm = np.array([-3.57227369, -5.3375872,   8.51914908,  0.66231135])

xByJacobi = np.array([-3.572273569424768, -5.337587095563936, 8.519149053352177, 0.6623112593169777])

xBySeidel = np.array([-3.5722736747747135, -5.337587196702536, 8.519149077744046, 0.6623113483679325])

def calculate_mistake(xm, x):
    sum = 0

    for i in range(n):
        sum += pow(x[i] - xm[i], 2)

    return np.sqrt(sum/n)

print("Похибка для методу Якобі: ", calculate_mistake(xm, xByJacobi))

print("Похибка для методу Зейделя: ", calculate_mistake(xm, xBySeidel))