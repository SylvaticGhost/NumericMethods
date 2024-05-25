from LabWork8.AdamsMethod import AdamsMethod
from LabWork8.RungeKuttMethod import RungeKuttMethod
from scipy.integrate import solve_ivp

from LabWork8.helpers import check_error

epsilon = 0.00001
a = 0
b = 0.5
h = 0.1

x0 = 0
y0 = -1

def f(x, y):
    return 0.25*y**2 + x**2

print("\n\033[1m" + "Метод Рунге-Кутта\n" + "\033[0m")
x_values, ys, h = RungeKuttMethod(f, y0, h, a, b)

print("Результат:")
print('x: ', x_values)
print('y: ', ys)

print('Перевірка за допомогою мат. пакету:')
y_first = [y0]
span = [a, b]
sol = solve_ivp(f, span, y_first, method='RK45', t_eval=x_values)
print(f'x: {sol.t}')
print(f'y: {sol.y[0]}')

print('Висновок:')
if check_error(ys, sol.y[0], epsilon):
    print('Відхилення не перевищує задану точність')
else:
    print('Відхилення перевищує задану точність')

print("\n\033[1m" + "Метод Адамса\n" + "\033[0m")
x_a, y_a = AdamsMethod(f, x_values, ys, h, a, b)
print("Результат:")
print('x: ', x_a)
print('y: ', y_a)
print('Перевірка за допомогою мат. пакету:')
if check_error(y_a, sol.y[0], epsilon):
    print('Відхилення не перевищує задану точність')
else:
    print('Відхилення перевищує задану точність')
