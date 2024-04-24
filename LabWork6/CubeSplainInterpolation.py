from sympy import symbols, simplify, solve

from LabWork6.Helpers import system_of_equations_to_string


def cube_splain_interpolation(xi, yi):
    S = []
    x = symbols('x')
    for i in range(1, len(xi)):
        ai = symbols('a' + str(i))
        bi = symbols('b' + str(i))
        ci = symbols('c' + str(i))
        di = symbols('d' + str(i))

        S.append(ai + bi*(x - xi[i-1]) + ci*(x - xi[i-1])**2 + di*(x - xi[i-1])**3)

    print("Кубічні сплайни: ", S)

    system = []

    for i in range(1, len(xi)):
        bi = symbols('b' + str(i))
        ci = symbols('c' + str(i))
        di = symbols('d' + str(i))

        hi = xi[i] - xi[i-1]
        system.append(bi*hi + ci*hi**2 + di*hi**3 - (yi[i] - yi[i-1]))

    for i in range(1, len(xi)-1):
        hi = xi[i] - xi[i-1]
        bi_next = symbols('b' + str(i+1))
        bi = symbols('b' + str(i))
        ci = symbols('c' + str(i))
        ci_next = symbols('c' + str(i+1))
        di = symbols('d' + str(i))

        system.append(bi_next - bi - 2*ci*hi - 3*di*hi**2)
        system.append(ci_next - ci - 3*di*hi)

        c1 = symbols('c1')
        system.append(c1)

        cn = symbols('c' + str(len(xi)-1))
        dn = symbols('d' + str(len(xi)-1))
        hn = xi[-1] - xi[-2]
        system.append(cn + 3*dn*hn)

    for i in range(1, len(xi)):
        ai = symbols('a' + str(i))
        system.append(ai - yi[i-1])

    print("Система рівнянь: \n", system_of_equations_to_string(system))

    solution = solve_system(system, len(xi))

    S = [spline.subs(solution) for spline in S]
    S = [simplify(spline) for spline in S]

    print("Cubic splines after substitution and simplifying: ", S)

    return S


def solve_system(system, n):
    variables = []

    for i in range(1, n):
        variables.append(symbols('a' + str(i)))
        variables.append(symbols('b' + str(i)))
        variables.append(symbols('c' + str(i)))
        variables.append(symbols('d' + str(i)))

    solution = solve(system, variables)

    print("Розв'язок: ", solution)

    return solution
