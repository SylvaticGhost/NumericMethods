from LabWork4.Helpers import Helpers

class Operations:
    @staticmethod
    def inverse_matrix(matrix):
        determinant = Operations.calculate_determinant(matrix)
        cont = []

        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix)):
                row.append(Operations.calculate_minor(matrix, i, j))
            cont.append(row)

        transposed = Operations.transpose_matrix(cont)
        result = Operations.multiply_on_number(transposed, 1/determinant)
        return result


    @staticmethod
    def calculate_minor(matrix, row, column):
        sub_matrix = []

        for i in range(len(matrix)):
            if i != row:
                sub_matrix.append(matrix[i][:column] + matrix[i][column+1:])

        return sub_matrix


    @staticmethod
    def calculate_determinant(matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        determinant = 0
        for i in range(len(matrix)):
            determinant += ((-1) ** i) * matrix[0][i] * Operations.calculate_determinant(Operations.calculate_minor(matrix, 0, i))
        return determinant


    @staticmethod
    def transpose_matrix(matrix):
        transposed = []
        for j in range(len(matrix)):
            row = []
            for i in range(len(matrix)):
                row.append(matrix[i][j])
            transposed.append(row)

        return transposed


    @staticmethod
    def multiply_on_number(matrix, number):
        result = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[i][j] * number)
            result.append(row)

        return result


    @staticmethod
    def multiply_matrix(matrix1, matrix2):
        result = []

        for row1 in matrix1:
            row = []
            for i in range(len(matrix2[0])):
                sum = 0
                for j in range(len(row1)):
                    sum += row1[j] * matrix2[j][i]
                row.append(sum)
            result.append(row)

        return result


    @staticmethod
    def multiply_vector(vector, n):
        result = []
        for i in range(len(vector)):
            result.append(vector[i] * n)
        return result


    @staticmethod
    def matrix_subtraction(matrix1, matrix2):
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1)):
                row.append(matrix1[i][j] - matrix2[i][j])
            result.append(row)
        return result
