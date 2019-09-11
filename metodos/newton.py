from sympy import *
import math

x = symbols('x')

tolerance = input("Write tolerance: ")
x0 = input("Start point: ")
niter = input("Number iteration: ")

tolerance = float(tolerance) 
x0 = float(x0)
niter = int(niter)

fx = sin(x)
dfx = cos(x)

fx_evaluated = fx.subs(x,x0)
dfx_evaluated = dfx.subs(x,x0)

count = 0
error =  tolerance + 1

while error > tolerance and fx != 0 and dfx != 0 and count < niter:
    x1 = x0 - (fx_evaluated / dfx_evaluated)
    fx_evaluated = fx.subs(x,x1)
    dfx_evaluated = dfx.subs(x,x1)
    error = abs((x1 - x0)/x1)
    x0 = x1
    count += 1
if fx == 0:
    print("{0} is a root".format(x0))
elif error < tolerance:
    print("{0} It is a root with tolerance = {1}".format(x1,tolerance))
elif dfx == 0:
    print("{0} is a multiple root".format(x1))
else:
    print("fail the number of iterations {0}".format(niter))