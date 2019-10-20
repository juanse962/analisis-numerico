print("------- POLYNOMIAL INTERPOLATION (Lagrange) -------")
import numpy as np
import sympy as sym

xp = 2.5
xi = np.array([1, 3, 4, 5, 7])
fi = np.array([4.31, 1.5, 3.2, 2.6,1.8])

n = len(xi)
x = sym.Symbol('x')

polynomial = 0
for i in range(0,n,1):
    term = 1
    for j  in range(0,n,1):
        if (j!=i):
            term = term*(x-xi[j])/(xi[i]-xi[j])
    polynomial = polynomial + term*fi[i]

px = polynomial.expand()
pxn = sym.lambdify(x,polynomial)

print('\nLagrange polynomial: ')
print(px,'\n')
print('Evaluate: ')
print(px.subs(x,xp))