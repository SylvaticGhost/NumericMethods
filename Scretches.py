from sympy import symbols, CRootOf

# Define the variable
x = symbols('x')

# Define the polynomial equation
equation = 5*x**5 - x**2 - 3*x + 6

# Get the roots
roots = [CRootOf(equation, i) for i in range(5)]

# Print the numerical values of the roots
for root in roots:
    print(root.evalf())