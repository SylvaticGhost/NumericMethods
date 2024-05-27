import numpy as np
import scipy.integrate as scinteg

k = 25

def system(x, y):
    return [y[1], (-y[0] + (k - 10) / 10 * y[1])]
    #function from example solving
    #return [y[1], -y[0]+0.1*y[1]]

a = 0
b = 10
N = 200
x = np.linspace(a, b, N)

solution = scinteg.solve_ivp(system, [x[0], x[-1]], [0.1, 0], t_eval=x)

print(solution)

import matplotlib.pyplot as plt

plt.title('y0 and y1')
plt.plot(x, solution.y[0], c='red', label='f0', linewidth=1)
plt.plot(x, solution.y[1], c='blue', label='f1', linewidth=1)
plt.legend()
plt.grid(True)
plt.show()

plt.title('Phase portrait')
plt.plot(solution.y[0], solution.y[1])
plt.axvline(0, color='black', lw=0.5)
plt.axhline(0, color='black', lw=0.5)
plt.grid(True)
plt.show()