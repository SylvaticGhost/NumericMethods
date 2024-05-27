def check_error(arr1, arr2, epsilon):
    if len(arr1) != len(arr2):
        raise ValueError('Довжини масивів не співпадають')

    result = True

    for i in range(len(arr1)):
        if abs(arr1[i] - arr2[i]) > epsilon:
            print(f'Похибка не виконана на точці {i} з похибкою {abs(arr1[i] - arr2[i])}')
            result = False

    return result

def error_function(values, ethalon_values):
    if len(values) != len(ethalon_values):
        raise ValueError('Довжини масивів не співпадають')

    e = []

    for i in range(len(values)):
        e.append(abs(values[i] - ethalon_values[i]))

    return e

def build_graphic_for_values(x, y_runge, y_adams, y_ethalon):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12, 10))
    plt.plot(x, y_runge, label='Runge-Kutta')
    plt.plot(x, y_adams, label='Adams')
    plt.plot(x, y_ethalon, label='Ethalon')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Runge-Kutta vs Adams vs Ethalon')
    plt.legend()
    plt.grid(True)
    plt.show()

def build_graphic_for_errors(x, e_runge, e_adams):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12, 10))
    plt.plot(x, e_runge, label='помилка методу Рунге-Кутта')
    plt.plot(x, e_adams, label='помилка методу Адамса')
    plt.xlabel('x')
    plt.ylabel('error')
    plt.title('Похибки методу Рунге-Кутта та Адамса')
    plt.legend()
    plt.grid(True)
    plt.show()


def build_graphic_for_errors_interpolated(x, e_runge, e_adams):
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.interpolate import interp1d
    x = np.array(x)
    xnew = np.linspace(x.min(), x.max(), 300)
    f_runge = interp1d(x, e_runge, kind='cubic')
    f_adams = interp1d(x, e_adams, kind='cubic')

    plt.figure(figsize=(12, 10))
    plt.plot(xnew, f_runge(xnew), label='помилка методу Рунге-Кутта')
    plt.plot(xnew, f_adams(xnew), label='помилка методу Адамса')
    plt.xlabel('x')
    plt.ylabel('error')
    plt.title('Похибки методу Рунге-Кутта та Адамса (інтерпольований графік)')
    plt.legend()
    plt.grid(True)
    plt.show()
