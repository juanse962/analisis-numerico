from sympy import *
import math

x = symbols('x')
function = (math.e**(3*x-12)) + x*cos(3*x)-x**2+4

xi= input("interval start: ") 
xs = input("interval end: ")
tolerance = input("number of tolerance: ")
niter = input("number of iterations: ")

xi = float(xi)
xs = float(xs)
tolerance = float(tolerance)
niter = int(niter)
xm = 0

fxi = function.subs(x, xi)
fxs = function.subs(x, xs)

if fxi == 0:
  print("{0} It's a root".format(xi))
elif fxs == 0:
  print("{0} It's a root".format(xs))
elif fxi * fxs < 0:
  xm = (xi+xs)/2
  fxm = function.subs(x, xm)
  count = 1
  error = tolerance + 1
  while (error > tolerance) and (fxm !=0) and (count < niter):
    if fxi * fxm <0:
      xs = xm
      fxs = function.subs(x, xm)
    else:
      xi = xm 
      fxi = function.subs(x, xm)
    xaux = xm
    xm = (xi+xs)/2
    fxm = function.subs(x, xm)
    error = abs(xm-xaux)
    count += 1
  if fxm == 0:
    print("{0} It's a root".format(xm))
  elif error < tolerance:
    print("{0} approximately and a tolerance = {1}".format(xm,tolerance))
  else:
    print("Failure of the number of iterations") 
else:
  print("The interval is inadequate")