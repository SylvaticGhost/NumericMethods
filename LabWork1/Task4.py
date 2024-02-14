import numpy as np
from sympy import Symbol, solve

x = Symbol('x')
equation = x**2 + 3*x - 4
print(solve(equation))

a = np.tan(np.pi/4)
print(a)

def f(x):
    return x**3 - 2*x + 1

print(f(2))