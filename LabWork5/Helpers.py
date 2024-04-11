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
