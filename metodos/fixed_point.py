from sympy import *
import math


def fixed_point(tolerance,xa,niter):
  x = symbols('x')

  fx = x*(math.e**x)-(x**2)-5*x-3
  gx = (x*(math.e**x)-(x**2)-3)/5

  fxa = fx.subs(x,xa)
  count = 0
  error = tolerance +1
  while (fxa != 0) and (error >tolerance) and (count < niter):
    xn = gx.subs(x,xa)
    fxa = fx.subs(x,xn)
    error = abs(xn-xa)
    xa = xn
    count += 1
  if fxa == 0:
    print("{xa} is a root")
  elif error < tolerance:
    print("{0} It is a root with tolerance = {1}".format(xa,tolerance))
  else:
    print("fail the number of iterations {0}".format(niter))

fixed_point(0.0005,-0.5,11)
