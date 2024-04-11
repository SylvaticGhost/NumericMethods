import numpy as np

ai = [3, 0, 0, -1, -3, 2]
#ai = [1, -5, -6]
a = 2
k = 4
ai[0] += a
ai[len(ai) - 1] += k
print('ai = ', ai)

print('m=', ai[1:])
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

def find_root_bounds(coefficients):
  """
  Finds the bounds for all roots of a polynomial equation.

  Args:
      coefficients: A list of coefficients of the polynomial in decreasing order.

  Returns:
      tuple: A tuple containing the lower and upper bounds of the roots.
  """

  n = len(coefficients)
  a_max = np.max(np.abs(coefficients[:-1]))
  b_max = np.max(np.abs(coefficients[1:]))
  lower_bound = -np.sqrt(float(float(b_max) / coefficients[0]))
  upper_bound = np.sqrt(a_max / coefficients[0])

  return lower_bound, upper_bound

print(print_equation(ai))


def calculate_polynom_value(polynom, x):
    result = 0
    for i in range(len(polynom)):
        try:
            #np.seterr(all='raise')
            result += polynom[i] * (x ** (len(polynom) - i - 1))
        except FloatingPointError:
            continue
    return result


def sturm_theorem(f, a, b):
    f1 = np.polyder(f)

    fi = [f, f1]

    # Generate the rest of the sequence
    for i in range(1, len(f) - 1):
        if np.any(fi[i] != 0):  # Check that fi[i] is not a zero polynomial
            quotient, remainder = np.polydiv(fi[i - 1], fi[i])
            fi.append(-remainder)

    print(fi)

    return abs(count_sign_changes(fi, a, b))


def count_sign_changes_in_array(array):
    count = 0
    for i in range(len(array) - 1):
        if array[i] * array[i + 1] < 0:
            count += 1
    return count


def count_sign_changes(sequence, a, b):
    val_for_a = []
    val_for_b = []

    for i in range(len(sequence)):
        val_for_a.append(calculate_polynom_value(sequence[i], a))
        val_for_b.append(calculate_polynom_value(sequence[i], b))

    return count_sign_changes_in_array(val_for_a) - count_sign_changes_in_array(val_for_b)

a , b = find_root_bounds(ai)
a -= 0.006
print('a = ', a, 'b = ', b)

n = sturm_theorem(ai, a, b)
print('number of roots =' ,n)

print('roots = ', np.roots(ai))

epsilone = 0.0001
def bisection_method(polynom, a, b):
    if calculate_polynom_value(polynom, a) * calculate_polynom_value(polynom, b) > 0:
        return None

    while abs(b - a) > epsilone:
        c = (a + b) / 2
        if calculate_polynom_value(polynom, c) == 0:
            return c
        elif calculate_polynom_value(polynom, c) * calculate_polynom_value(polynom, a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

print('bisection roots = ', bisection_method(ai, a, b))

def chord_method(polynom, a, b):
    derivative = np.polyder(polynom) #перша похідна
    derivative2 = np.polyder(derivative) #друга похідна

    x0 = (a + b) / 2
    x = [0, 0]

    value = calculate_polynom_value(polynom, x0) * calculate_polynom_value(derivative2, x0)
    if value > 0:
        #Нерухома права границя
        x[0] = b
        x[1] = a
    else:
        #Нерухома ліва границя
        x[0] = a
        x[1] = b

    while True:
        x_prev = x[len(x) - 1]
        x_new = x_prev - calculate_polynom_value(polynom, x_prev) * (x_prev - x[0]) / (calculate_polynom_value(polynom, x_prev) - calculate_polynom_value(polynom, x[0]))
        x.append(x_new)
        if abs(x_new - x_prev) < epsilone:
            break

    return x[len(x)- 1]

print('chord roots = ', chord_method(ai, a, b))

def newton_method(polynom, a, b):
    derivative = np.polyder(polynom) #перша похідна
    derivative2 = np.polyder(derivative) #друга похідна

    x0 = (a + b) / 2

    while True:
        x_prev = x0
        x0 = x0 - calculate_polynom_value(polynom, x0) / calculate_polynom_value(derivative, x0)
        if abs(x0 - x_prev) < epsilone:
            break

    return x0

print('newton roots = ', newton_method(ai, a, b))