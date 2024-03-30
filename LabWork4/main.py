import numpy as np
import scipy as sp

from LabWork4.Helpers import Helpers
from LabWork4.Operations import Operations
from copy import copy

class Program:
     t = 5
     k = 3 * (4 - 3) + 2

     a = 0.11 * t
     b = 0.02 * k
     g = 0.02 * k
     d = 0.015 * t

     A = [[6.26 + a, 1.10 - b, 0.97 + g, 1.24 - d],
          [1.10 - b, 4.16 - a, 1.30, 0.16],
          [0.97 + g, 1.30, 5.44 + a, 2.10],
          [1.24 - d, 0.16, 2.10, 6.10 - a]]


     def Solve(self):
          print("Вихідна матриця A = ")
          Helpers.print_matrix(self.A)
          Aw = copy(self.A)

          Ms = []
          size = len(self.A)

          i = size - 1
          j = size - 2

          index = size - 1

          while i >= 1 and j >= 0:
               if self.A[i][j] == 0:
                    break
               M = Helpers.get_e_matrix(size)
               M_inverse = Helpers.get_e_matrix(size)
               for k in range(size):
                    if k == j:
                         M[j][k] = 1 / Aw[i][j]
                    else:
                         M[j][k] = - Aw[i][k] / Aw[i][j]
                    M_inverse[j][k] = Aw[i][k]

               print(f"матриця M{i} = ")
               Helpers.print_matrix(M)
               print(f"Обернена матриця M{i} = ")
               Helpers.print_matrix(M_inverse)
               Ms.append(M)

               Aw = Operations.multiply_matrix(M_inverse, Aw)
               Aw = Operations.multiply_matrix(Aw, M)

               i -= 1
               j -= 1
               print(f'A{i + 1}=')
               Helpers.print_matrix(Aw)
               index -= 1

          print("Матриця після перетворень у нормальній формі Фробеніуса= ")
          Helpers.print_matrix(Aw)

          print('Знаходження власних чисел матриці A = ')

          v = Aw[0]
          v.reverse()
          v = Operations.multiply_vector(v, -1)
          v.append(1)

          Helpers.print_equation(v)

          print("Вектор v = ")
          print(v)

          λ = np.polynomial.polynomial.polyroots(v)

          print("Власні значення =")
          print(λ)

          lambdas = []
          for i in range(size):
               lambda_i = λ[i]
               y = []
               for j in range(size - 1, -1, -1):
                    y.append(lambda_i ** j)
               print(f"Вектор y{i + 1} = ")
               print(y)
               lambdas.append(y)

          Ms.reverse()
          S = Operations.multiply_matrix(Ms[size - 2], Ms[size - 3])
          for i in range(size - 4, -1, -1):
               S = Operations.multiply_matrix(S, Ms[i])

          print("Матриця S = ")
          Helpers.print_matrix(S)

          xs = []

          for i in range(size):
               yi = lambdas[i]

               xi = np.dot(S, yi)
               print(f"Вектор x{i + 1} = ")
               print(xi)
               xs.append(xi)

               p1 = np.dot(self.A, xi)
               p2 = np.dot(λ[i], xi)
               p = p1 - p2
               print(f"Перевірка #{i + 1}= ")
               print(p)

          return λ, xs


if __name__ == '__main__':
     np.set_printoptions(suppress=True)
     program = Program()
     program.Solve()
