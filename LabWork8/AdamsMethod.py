def AdamsMethod(f, x_values, y_values, h, a, b, epsilon=0.00001):

    if len(x_values) < 4 or len(y_values) < 4:
        raise ValueError('необхідно мати принаймні 3 точки для методу Адамса')

    x_values = x_values[:4]
    y_values = y_values[:4]

    n = int((b - a) / h)

    print('Значення отримані методом Рунге-Кутта')
    print(f'x1 = {x_values[-3]}')
    print(f'x2 = {x_values[-2]}')
    print(f'x3 = {x_values[-1]}')
    print(f'y1 = {y_values[-3]}')
    print(f'y2 = {y_values[-2]}')
    print(f'y3 = {y_values[-1]}')

    for k in range(3, n):
        print('крок ', k + 1)
        y_next_progn = y_values[-1] + h / 24 * (55 * f(x_values[-1], y_values[-1]) - 59 * f(x_values[-2], y_values[-2]) + 37 * f(x_values[-3], y_values[-3]) - 9 * f(x_values[-4], y_values[-4]))
        print('y_next_progn = ', y_next_progn)
        y_values.append(y_next_progn)
        x_values.append(x_values[-1] + h)
        y_next_kor = y_values[-2] + h / 24 * (9 * f(x_values[-1], y_values[-1]) + 19 * f(x_values[-2], y_values[-2]) - 5 * f(x_values[-3], y_values[-3]) + f(x_values[-4], y_values[-4]))
        print('y_next_kor = ', y_next_kor)


        d_analytical = abs(y_next_kor - y_next_progn)
        print('Δ_analytical = ', d_analytical, ' на кроці ', k + 1)
        if d_analytical < epsilon:
            print('Похибка менша за задану точність')
        else:
            print('Похибка більша за задану точність')

    return x_values, y_values