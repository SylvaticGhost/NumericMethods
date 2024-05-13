import math

import numpy as np
import sympy as sp
from scipy.integrate import quad
from LabWork7.simpsonMethod import solve_simpson
from LabWork7.gaussMethod import solve_gauss
from LabWork7.helpers import show_error

def f(x):
    return (sp.log(x**2 + 1))/x

a = 1
b = 3

epsilon = 0.0001

print("\033[1m" + "Програмний розв'язок\n" + "\033[0m")


print("\033[1m" + "\nМетод Сімпсона" + "\033[0m")
integral_simpson, d_analytical_simpson = solve_simpson(f, a, b, epsilon)
print('Значення інтегралу: ', integral_simpson)


print("\033[1m" + "\nРозв'язок квадратною формулою Гауса" + "\033[0m")
integral_gauss, d_analytical_gauss = solve_gauss(f, a, b, epsilon)
print('Значення інтегралу: ', integral_gauss)


print("\033[1m" + "\nТочний розв'язок" + "\033[0m")
Integral_ethalon = quad(f, a, b)
print('Значення інтегралу: ', Integral_ethalon[0])


print("\033[1m" + "\nПохибки" + "\033[0m")

print("Аналіз методу Сімпсона")
show_error(integral_simpson, Integral_ethalon[0], d_analytical_simpson, epsilon)

print("\nАналіз методу Гауса")
show_error(integral_gauss, Integral_ethalon[0], d_analytical_gauss, epsilon)

