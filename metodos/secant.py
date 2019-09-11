from sympy import *
import math

x = symbols('x')

tolerance = input("Write tolerance: ")
x0 = input("Zero point: ")
x1 = input("One point: ")
niter = input("Number iteration: ")

tolerance = float(tolerance) 
x0 = float(x0)
x1 = float(x1)
niter = int(niter)

fx = math.e**(-x**2+1)-4*x**3 + 25
fx0 = fx.subs(x,x0)

if fx0 == 0:
    print("{0} is a root".format(x0))
else:
    fx1 = fx.subs(x,x1)
    count = 0
    error = tolerance + 1
    den = fx1 - fx0
    while error > tolerance and fx1 != 0 and den != 0 and count < niter:
        x2 = x1 - fx1 *(x1 - x0)/den
        error = abs(x2 - x1)
        x0 = x1 
        fx0 = fx1
        x1 = x2
        fx1 = fx.subs(x,x1)
        den = fx1 - fx0
        count += 1
    if fx1 == 0:
        print("{0} is a root".format(x1)) 
    elif error < tolerance:
        print("{0} It is a root with tolerance = {1}".format(x1,tolerance))
    elif den == 0:
        print("there is a possible multiple root")
    else:
        print("fail the number of iterations {0}".format(niter))