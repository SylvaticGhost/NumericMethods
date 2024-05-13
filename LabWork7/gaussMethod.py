import sympy as sp
import scipy.optimize as opt

from LabWork7.helpers import factorial, build_graphic, find_max_value


def solve_gauss(f, a, b, epsilon):
    m = 2
    i = 2
    d_analytical = 0

    while True:
        print(f'Починаємо розрахунок для m = {m}')
        got_accuracy, d_analytical = _calculate_at_i_derivative(f, a, b, m, i, epsilon)
        if got_accuracy:
            break
        else:
            m += 1
            i += 2

    t = sp.symbols('t')
    x = (b - a) / 2 * t + (a + b) / 2
    f = f(x)

    roots, weights = _get_roots_and_weights(m)

    integral = 0
    for i in range(m):
        print(f'Значення ваги {i + 1}-го кореня: {weights[i]}', f'Значення кореня {i + 1}: {roots[i]}')
        integral += weights[i] * f.subs('t', roots[i])

    integral = sp.simplify(integral)

    return integral.evalf(), d_analytical


def _calculate_at_i_derivative(f, a, b, m, i, epsilon):
    x = sp.symbols('x')
    f = f(x)
    i = 2*m
    f_i = sp.diff(f, x, i)
    f_i = sp.lambdify(x, f_i)

    mx = opt.minimize_scalar(lambda x: f_i(x), bounds=(a, b), method='bounded').fun
    max_value = find_max_value(f_i, a, b, epsilon)
    print(f'максимальне значення {i}-ої похідної за модулем : ', max_value)


    build_graphic(f_i, a, b,f'Графік {i}-ої похідної функції')

    d_analytical = _d_analytical(a, b, m, max_value)
    result = d_analytical < epsilon
    print('Аналітична похибка: ', d_analytical)
    print('Чи є аналітична похибка менше заданої: ', result)

    return result, d_analytical


def _d_analytical(a, b, m, max_value):
    return ((factorial(m)**4 * (b - a)**(m - 1))/((2*m + 1)*factorial(2*m)**3))*max_value

def _get_roots_and_weights(m):
    x = sp.symbols('x')
    roots = sp.solve(sp.legendre(m, x), x)
    weights = []
    for i in range(m):
        weights.append(2/((1 - roots[i]**2) * sp.diff(sp.legendre(m, x), x).subs('x', roots[i])**2))
    return roots, weights
    # roots = [
    #     [-0.577350, 0.577350],
    #     [-0.774597, 0.0, 0.774597],
    #     [-0.861136, -0.339981, 0.339981, 0.861136],
    #     [-0.906180, -0.538470, 0.0, 0.538470, 0.906180],
    #     [-0.932470, -0.661210, -0.238619, 0.238620, 0.661210, 0.932470],
    #     [-0.949108, -0.741531, -0.405845, 0.0, 0.405845, 0.741531, 0.949108],
    #     [-0.960290, -0.796666, -0.525532, -0.183434, 0.183434, 0.525532, 0.796666, 0.960289],
    # ]
    # weights = [
    #     [1.0, 1.0],
    #     [0.555555, 0.888889, 0.555555],
    #     [0.347855, 0.652145, 0.652145, 0.347855],
    #     [0.236927, 0.478629, 0.568889, 0.478629, 0.236927],
    #     [0.171324, 0.360761, 0.467914, 0.467914, 0.360761, 0.171324],
    #     [0.129485, 0.279705, 0.381830, 0.417960, 0.381830, 0.279705, 0.129485],
    #     [0.101228, 0.222381, 0.313707, 0.362684, 0.362684, 0.313707, 0.222381, 0.101228],
    # ]
    # return roots[m - 2], weights[m - 2]