class Helpers:
    @staticmethod
    def get_e_matrix(size):
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

    @staticmethod
    def print_matrix(matrix):
        for row in matrix:
            print(row)
        print("\n")

    @staticmethod
    def convert_row_to_column(row):
        return [[row[i]] for i in range(len(row))]

    @staticmethod
    def print_equation(v):
        v1 = v.copy()
        v1.reverse()
        print("Характеристичне рівняння:")
        print("P(λ) = ")
        for i in range(len(v1)):
            print(f"{v1[i]}*λ^{len(v1) - i - 1}", end=" ")
        print("= 0\n")