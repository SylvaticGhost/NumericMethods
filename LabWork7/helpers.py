import numpy as np

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def build_graphic(f, a, b, title = 'Графік функції'):
    import matplotlib.pyplot as plt

    x = np.linspace(a, b, 1000)
    y = f(x)

    plt.plot(x, y)
    plt.title(title)
    plt.show()


def show_error(my_value, ethalon_value, d_analytical, epsilon):
    print('Аналітична похибка: ', d_analytical)
    d_real = abs(ethalon_value - my_value)
    print('Реальна похибка: ', d_real)

    if d_real > epsilon:
        print('Реальна похибка більша за задану точність')
    elif d_real > d_analytical:
        print('Реальна похибка більша за аналітичну')
    else:
        print('Точність дотримана')


def find_max_value(func, a, b, epsilon):
    max = 0
    t = a
    while t <= b:
        if abs(func(t)) > max:
            max = abs(func(t))
        t += epsilon*0.01

    return max