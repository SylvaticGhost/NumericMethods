import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x):
    return np.sin(x)*2 + 2

x = np.linspace(-10, 10, 400)

y = f(x)

plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('y')

plt.show()

#3D

def g(x, y):
    return np.cos(x) + np.sin(y)

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = g(x, y)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

plt.show()

