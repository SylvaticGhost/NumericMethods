import numpy as np

class Helpers:
    @staticmethod
    def calculate_polynom_value(polynom, x):
        result = 0
        for i in range(len(polynom)):
            try:
                # np.seterr(all='raise')
                result += polynom[i] * (x ** (len(polynom) - i - 1))
            except FloatingPointError:
                continue
        return result

    @staticmethod
    def print_equation(ai):
        string_builder = []
        for i in range(len(ai)):
            if ai[i] != 0:
                if ai[i] > 0:
                    string_builder.append(f"+{ai[i]}*x^{len(ai) - i - 1}")
                else:
                    string_builder.append(f"{ai[i]}*x^{len(ai) - i - 1}")

        string_builder.append(f"={0}")
        return "".join(string_builder)

    @staticmethod
    def find_root_bounds(coefficients):
        """
        Finds the bounds for all roots of a polynomial equation.

        Args:
            coefficients: A list of coefficients of the polynomial in decreasing order.

        Returns:
            tuple: A tuple containing the lower and upper bounds of the roots.
        """

        a_max = np.max(np.abs(coefficients[:-1]))
        b_max = np.max(np.abs(coefficients[1:]))
        lower_bound = -np.sqrt(float(float(b_max) / coefficients[0]))
        upper_bound = np.sqrt(a_max / coefficients[0])

        return lower_bound, upper_bound
