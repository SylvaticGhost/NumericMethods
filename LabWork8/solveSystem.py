import sympy as sp

y0, y1 = sp.symbols('y0 y1')
t = sp.symbols('t')  # Define the independent variable
y0 = sp.Function('y0')(t)  # Define y0 as a function of t
y1 = sp.Function('y1')(t)  # Define y1 as a function of t

k = 25
system = []
system.append(sp.Eq(sp.diff(y0, t), y1))
system.append(sp.Eq(sp.diff(y1, t), -y0 + (k - 10)/10*y1))

# Define the initial conditions
initial_conditions = {y0.subs(t, 0): 0.1, y1.subs(t, 0): 0}

# Solve the system with initial conditions
solution = sp.dsolve(system, ics=initial_conditions)

print(solution)

import matplotlib.pyplot as plt
import numpy as np

# Convert symbolic solutions to numeric functions
y0_numeric = sp.lambdify(t, solution[0].rhs, "numpy")
y1_numeric = sp.lambdify(t, solution[1].rhs, "numpy")

# Generate a range of t values
t_values = np.linspace(0, 10, 1000)

# Calculate the corresponding y0 and y1 values
y0_values = y0_numeric(t_values)
y1_values = y1_numeric(t_values)

# Plot y0 and y1 on the same graph
plt.figure(figsize=(10, 6))
plt.plot(t_values, y0_values, label='y0')
plt.plot(t_values, y1_values, label='y1')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Plot of y0 and y1')
plt.grid(True)
plt.show()


def system(t, y):
    return [y[1], -y[0] + (k - 10) / 10 * y[1]]


# Generate a grid of points
y1 = np.linspace(-2, 2, 20)
y2 = np.linspace(-2, 2, 20)
Y1, Y2 = np.meshgrid(y1, y2)

t = 0

# Calculate the direction at each point
u, v = np.zeros(Y1.shape), np.zeros(Y2.shape)
NI, NJ = Y1.shape

for i in range(NI):
    for j in range(NJ):
        x = Y1[i, j]
        y = Y2[i, j]
        yprime = system(t, [x, y])
        u[i, j] = yprime[0]
        v[i, j] = yprime[1]

# Normalize the arrows
N = np.sqrt(u ** 2 + v ** 2)
u /= N
v /= N

plt.quiver(Y1, Y2, u, v, color='r')

# for i in range(NI):
#     for j in range(NJ):
#         plt.plot([Y1[i, j] - u[i, j], Y1[i, j] + u[i, j]], [Y2[i, j] - v[i, j], Y2[i, j] + v[i, j]], color='r')



plt.xlabel('$y_0$')
plt.ylabel('$y_1$')
plt.title('Phase portrait of the system')
plt.grid()
plt.show()