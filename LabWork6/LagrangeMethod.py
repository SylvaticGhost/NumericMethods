from sympy import symbols, simplify

def lagrange_method(y, xi):
    """
    :param y:  Функція, яку потрібно інтерполювати
    :param xi:  вузли інтерполяції
    :return: поліном коефіцієнтів
    """
    yi = [y(i) for i in xi]
    print("Значення функції в вузлах інтерполяції: ", yi)
    l = L(xi, yi)
    return l


def L(xi, yi):
    L = 0
    x = symbols('x')
    for i in range(len(xi)):
        res = 1
        x_current = xi[i]
        x_cut = xi[:i] + xi[i+1:]
        for j in x_cut:
            res *= (x - j)/(x_current - j)
        L += yi[i]*res

    return simplify(L)

