import numpy as np

from LabWork5.Helpers import Helpers


class SolveEquation:
    def __init__(self, polynom, a, b):
        self.polynom = polynom
        self.a = a
        self.b = b

    def bisection_method(self, epsilon):
        a = self.a
        b = self.b
        polynom = self.polynom

        if Helpers.calculate_polynom_value(polynom, a) * Helpers.calculate_polynom_value(polynom, b) > 0:
            return None

        iterations = 0

        while abs(b - a) > epsilon:
            iterations += 1
            c = (a + b) / 2
            if Helpers.calculate_polynom_value(polynom, c) == 0:
                return c
            elif Helpers.calculate_polynom_value(polynom, c) * Helpers.calculate_polynom_value(polynom, a) < 0:
                b = c
            else:
                a = c

        return (a + b) / 2, iterations

    def chord_method(self, epsilon):
        derivative = np.polyder(self.polynom)  # перша похідна
        derivative2 = np.polyder(derivative)  # друга похідна

        x0 = (self.a + self.b) / 2
        x = [0, 0]

        value = Helpers.calculate_polynom_value(self.polynom, x0) * Helpers.calculate_polynom_value(derivative2, x0)

        if value > 0:
            # Нерухома права границя
            x[0] = self.b
            x[1] = self.a
        else:
            # Нерухома ліва границя
            x[0] = self.a
            x[1] = self.b

        iterations = 0
        while True:
            iterations += 1
            x_prev = x[len(x) - 1]
            x_new = x_prev - Helpers.calculate_polynom_value(self.polynom, x_prev) * (x_prev - x[0]) / (
                        Helpers.calculate_polynom_value(self.polynom, x_prev) - Helpers.calculate_polynom_value(self.polynom, x[0]))
            x.append(x_new)
            if abs(x_new - x_prev) < epsilon:
                break

        return x[len(x) - 1], iterations

    def newton_method(self, epsilon):
        derivative = np.polyder(self.polynom)  # перша похідна
        derivative2 = np.polyder(derivative)  # друга похідна

        x0 = (self.a + self.b) / 2

        iterations = 0
        while True:
            iterations += 1
            x_prev = x0
            x0 = x0 - Helpers.calculate_polynom_value(self.polynom, x0) / Helpers.calculate_polynom_value(derivative, x0)
            if abs(x0 - x_prev) < epsilon:
                break

        return x0, iterations