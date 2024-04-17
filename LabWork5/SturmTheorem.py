import numpy as np

class SturmTheorem:

    def __init__(self, polynom):
        self.f = polynom

    def theorem(self, a, b):
        """
        :param a: left border of the interval
        :param b: right border of the interval
        :return: number of roots in the interval [a, b]
        """
        f1 = np.polyder(self.f)

        fi = [self.f, f1]

        # Generate the rest of the sequence
        for i in range(1, len(self.f) - 1):
            if np.any(fi[i] != 0):  # Check that fi[i] is not a zero polynomial
                quotient, remainder = np.polydiv(fi[i - 1], fi[i])
                fi.append(-remainder)

        return abs(self.count_sign_changes(fi, a, b))

    @staticmethod
    def count_sign_changes_in_array(array):
        count = 0
        for i in range(len(array) - 1):
            if array[i] * array[i + 1] < 0:
                count += 1
        return count

    def count_sign_changes(self, sequence, a, b):
        val_for_a = []
        val_for_b = []

        for i in range(len(sequence)):
            from LabWork5.Helpers import Helpers
            val_for_a.append(Helpers.calculate_polynom_value(sequence[i], a))
            val_for_b.append(Helpers.calculate_polynom_value(sequence[i], b))

        return self.count_sign_changes_in_array(val_for_a) - self.count_sign_changes_in_array(val_for_b)