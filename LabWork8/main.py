from tabulate import tabulate
import numpy as np
from LabWork8.AdamsMethod import AdamsMethod
from LabWork8.RungeKuttMethod import RungeKuttMethod
from scipy.integrate import solve_ivp

from LabWork8.helpers import check_error, build_graphic_for_values, error_function, build_graphic_for_errors, \
    build_graphic_for_errors_interpolated

epsilon = 10**-5
print('epsilon = ', epsilon)
h = 0.1

n_var = 25
k = n_var - 20

a_k = 1 + 0.4*k

x0 = 0
y0 = 0

#interval
a = x0
b = 1

def f(x, y):
    #return 0.25*y**2 + x**2
    return np.cos(y)/(a_k + x) + y**2

print("\n\033[1m" + "Метод Рунге-Кутта\n" + "\033[0m")
x_values, ys, h = RungeKuttMethod(f, y0, h, a, b)

x_values_copy = np.array(x_values)
ys_copy = np.array(ys)

print("Результат методу Рунге-Кутта:")

y_first = [y0]
span = [x0, 1]
sol = solve_ivp(f, span, y_first, method='RK45', t_eval=x_values)
error_on_runge = error_function(ys, sol.y[0])

table_runge = list(zip(x_values, ys, sol.y[0], error_on_runge))
print(tabulate(table_runge, headers=['x', 'y (обчислений)', 'y (еталоний)', 'похибка'], tablefmt='grid'))

# print('Висновок:')
# if check_error(ys, sol.y[0], epsilon):
#     print('Відхилення не перевищує задану точність')
# else:
#     print('Відхилення перевищує задану точність')


print("\n\033[1m" + "Метод Адамса\n" + "\033[0m")
x_a, y_a = AdamsMethod(f, x_values, ys, h, a, b)

x_a_copy = np.array(x_a)
y_a_copy = np.array(y_a)

print("Результат методу Адамса:")

error_on_adams = error_function(y_a, sol.y[0])

table_adams = list(zip(x_a, y_a, sol.y[0], error_on_adams))
print(tabulate(table_adams, headers=['x', 'y (обчислений)', 'у (еталоний)', 'Похибка'], tablefmt='grid'))

# if check_error(y_a, sol.y[0], epsilon):
#     print('Відхилення не перевищує задану точність')
# else:
#     print('Відхилення перевищує задану точність')


build_graphic_for_values(x_values, ys, y_a, sol.y[0])

build_graphic_for_errors(x_values, error_on_runge, error_on_adams)

build_graphic_for_errors_interpolated(x_values, error_on_runge, error_on_adams)
