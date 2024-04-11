import numpy as np

from LabWork5.Helpers import Helpers


class SolveEquation:
    def __init__(self, polinom, a, b):
        self.polinom = polinom
        self.a = a
        self.b = b

    def bisection_method(self, epsilon):
        a = self.a
        b = self.b
        polynom = self.polinom

        if Helpers.calculate_polynom_value(polynom, a) * Helpers.calculate_polynom_value(polynom, b) > 0:
            return None

        while abs(b - a) > epsilon:
            c = (a + b) / 2
            if Helpers.calculate_polynom_value(polynom, c) == 0:
                return c
            elif Helpers.calculate_polynom_value(polynom, c) * Helpers.calculate_polynom_value(polynom, a) < 0:
                b = c
            else:
                a = c

        return (a + b) / 2