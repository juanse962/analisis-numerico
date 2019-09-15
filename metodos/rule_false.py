from sympy import *
import math

x = symbols('x')
function = (math.e**(3*x-12)) + x*cos(3*x)-x**2+4

xa= input("interval start: ") 
xb = input("interval end: ")
tolerance = input("number of tolerance: ")
niter = input("number of iterations: ")

xa = float(xa)
xb = float(xb)
tolerance = float(tolerance)
niter = int(niter)
xm = 0

fxa = function.subs(x, xa)
fxb = function.subs(x, xb)
xm = xa -(function.subs(x, xa)*(xb-xa))/(function.subs(x, xb)-function.subs(x, xa))  
fxm = function.subs(x,xm)

if fxa == 0:
  print("{0} It's a root".format(xa))
elif fxb == 0:
  print("{0} It's a root".format(xb))
elif fxa * fxb < 0:
    xm = xa -(function.subs(x, xa)*(xb-xa))/(function.subs(x, xb)-function.subs(x, xa))
    fxm = function.subs(x,xm)
    count = 1
    error = tolerance + 1
    while (error > tolerance) and (fxm !=0) and (count < niter):
        if fxa * fxm < 0:
            xb = xm
        else:
            xa = xm
        aux = xm
        xm = xa -(function.subs(x, xa)*(xb-xa))/(function.subs(x, xb)-function.subs(x, xa))  
        fxm = function.subs(x,xm)
        error = abs(xm-aux)
        count += 1
    if fxm == 0:
        print("{0} It's a root".format(xm))
    elif error < tolerance:
        print("{0} approximately and a tolerance = {1}".format(xm,tolerance))
    else:
        print("Failure of the number of iterations") 
else:
  print("The interval is inadequate")