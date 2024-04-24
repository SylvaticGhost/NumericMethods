import numpy as np

from LabWork6.CubeSplainInterpolation import cube_splain_interpolation

a = 4
n_var = 25 # не кратний двом, отже, інтерполяція методом Лагранжа
k = (n_var - 21)*2

def y(x):
    return x**2/15 + np.cos(x + a)

xi = [-6 + k, -4 + k, -2 + k, 0+k, 2+ k]

yi = [y(i) for i in xi]

S = cube_splain_interpolation(xi, yi)
print("Кубічні сплайни: ")
print(S)