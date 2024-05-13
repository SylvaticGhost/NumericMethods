import sympy as sp
import numpy as np
import scipy.optimize as opt

def solve_simpson(f, a, b, epsilon):
    n, d_analytical = calculate_n(f, a, b, epsilon)
    print('Мінімальна кількість кроків для отримання заданої точності: ', n)

    if n % 2 != 0:
        n += 1

    h = (b - a) / n
    print('Крок розбиття: ', h)

    Integral = simpson_method(f, a, b, n, h)

    d_analytical = d_analytical.subs('n', n)

    return Integral, d_analytical

def calculate_n(f, a, b, epsilon):
    x = sp.symbols('x')
    f = f(x)

    f_4 = sp.diff(f, x, 4)
    f_4 = sp.lambdify(x, f_4)


    mx = opt.minimize_scalar(lambda x: f_4(x), bounds=(a, b), method='bounded').fun
    max_value = abs(mx)
    print('максимальне значення 4-ої похідної за модулем : ', max_value)

    _build_graphic(f_4, a, b, mx)

    n = sp.symbols('n')
    d_analytical = (b - a)**5/(180 * n**4) * abs( max_value)
    d_analytical = sp.simplify(d_analytical)
    print('аналітична похибка: ', d_analytical)

    return _solve_inequality(d_analytical, epsilon), d_analytical


def _solve_inequality(d_analytical, epsilon):
    n = 1

    while d_analytical.subs('n', n) >= epsilon:
        n += 1

    return n


def simpson_method(f, a, b, n, h):
    x_values = [a + i * h for i in range(0, n + 1)]

    y_values = [f(x) for x in x_values]
    print('значення x: ', x_values)
    print('значення y: ', y_values)

    S1 = sum(y_values[i] for i in range(1, n, 2))
    S2 = sum(y_values[i] for i in range(2, n - 1, 2))

    Integral = h/3 * (y_values[0] + y_values[-1] + 4 * S1 + 2 * S2)

    return Integral


def _build_graphic(f_4, a, b, max_value):
    import matplotlib.pyplot as plt

    x = np.linspace(a, b, 1000)
    y = f_4(x)

    plt.plot(x, y)
    plt.title('Графік четвертої похідної функції')
    plt.axhline(y=max_value, color='r', linestyle='--')
    plt.show()