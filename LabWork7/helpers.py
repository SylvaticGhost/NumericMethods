import numpy as np

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def build_graphic(f, a, b, max_value, title = 'Графік функції'):
    import matplotlib.pyplot as plt

    x = np.linspace(a, b, 1000)
    y = f(x)

    plt.plot(x, y)
    plt.title(title)
    plt.axhline(y=max_value, color='r', linestyle='--')
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