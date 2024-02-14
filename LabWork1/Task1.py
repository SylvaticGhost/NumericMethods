from sympy import Symbol, sin, pi, cos, tan

alpha = Symbol('\u03B1')
beta = Symbol('\u03B2')
n = Symbol('n')
f = sin(alpha) + cos(alpha/2) + tan(beta) + 2*pi*n

print(f)

