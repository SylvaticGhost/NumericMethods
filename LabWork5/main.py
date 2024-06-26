import numpy as np

from LabWork5.Helpers import Helpers
from LabWork5.SolveEquation import SolveEquation
from LabWork5.SturmTheorem import SturmTheorem

ai = [3, 0, 0, -1, -3, 2]

a = 2
k = 4
ai[0] += a
ai[len(ai) - 1] += k
epsilon = 0.000001

print('вихідний набір коефіцієнтів = ', ai)

print("Рівняння:")
print(Helpers.print_equation(ai))

a, b = Helpers.find_root_bounds(ai)
a -= 0.01

print(f"Ліва границя: {a}, Права границя: {b}")

shturmTheorem =  SturmTheorem(ai)
number_of_roots =  shturmTheorem.theorem(a, b)
print(f"Кількість коренів на відрізку [{a}, {b}] = {number_of_roots}\n")

if number_of_roots == 0:
    print("Оскільки кількість коренів на відрізку [a, b] = 0, то коренів немає")
    exit(0)

solveEquation = SolveEquation(ai, a, b)

print("Програмний розв'язок:")
solution_bisection, i = solveEquation.bisection_method(epsilon)
print(f"Розв'язок методом бісекції: {solution_bisection}, Кількість ітерацій: {i}")

solution_chord, i = solveEquation.chord_method(epsilon)
print(f"Розв'язок методом хорд: {solution_chord}, Кількість ітерацій: {i}")

solution_newton, i = solveEquation.newton_method(epsilon)
print(f"Розв'язок методом Ньютона: {solution_newton}, Кількість ітерацій: {i}\n")

print("\nРозв'язок з використанням мат. пакету:")
roots = np.roots(ai)
print(roots)
roots_real = roots[np.isreal(roots)]
roots_real = np.real(roots_real)
print("Дійсні корені: ", roots_real)



