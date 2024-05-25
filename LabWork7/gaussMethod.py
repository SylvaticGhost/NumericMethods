import sympy as sp
import scipy.optimize as opt

from LabWork7.helpers import factorial, build_graphic, find_max_value


def solve_gauss(f, a, b, epsilon):
    m = 2
    d_analytical = 0

    while True:
        print(f'Починаємо розрахунок для m = {m}')
        got_accuracy, d_analytical = _calculate_at_i_derivative(f, a, b, m, 2*m, epsilon)
        if got_accuracy:
            break
        else:
            m += 1


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
