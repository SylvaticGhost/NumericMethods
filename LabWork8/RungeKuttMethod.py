def RungeKuttMethod(f,y0, h, a, b):
    """
    :param f: похідна функції
    :param y0: значення в x = 0
    :param h: крок розбиття
    :param a: початок проміжку
    :param b: кінець проміжку
    :return: два масиви значень x та y та кінцевовикористаний крок
    """

    n = calculate_n(a, b, h)

    x_values = [a + i * h for i in range(n + 1)]

    ys = [y0]

    i = 0
    while i < n:
        print('крок ', i)
        k1 = h * f(x_values[i], ys[i])
        k2 = h * f(x_values[i] + h / 2, ys[i] + k1 / 2)
        k3 = h * f(x_values[i] + h / 2, ys[i] + k2 / 2)
        k4 = h * f(x_values[i] + h, ys[i] + k3)

        teta = abs((k2 - k3) / (k1 - k2))
        print('θ = ', teta, ' на кроці ', i)

        if teta > 0.01:
            h /= 2
            print('Зменшуємо крок та розрочинаємо обрахунок з початку')
            #Необхідно розпочати обрахунок з початку
            i = 0
            ys = [y0]
            n = calculate_n(a, b, h)
            x_values = [a + i * h for i in range(n + 1)]
            continue

        delta_y = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        print(f'Δy_{i} = ', delta_y)

        y_next = round(ys[i] + delta_y, 8)
        ys.append(y_next)

        print(f'y_{i + 1} = ', y_next)
        i += 1

    return x_values, ys, h


def calculate_n(a, b, h):
    n = int((b - a) / h)
    print('Розбиваємо відрізок на ', n, ' частин')
    return n