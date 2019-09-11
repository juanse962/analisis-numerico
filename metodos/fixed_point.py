from sympy import *
import math


def fixed_point(tolerance,xa,niter):
  x = symbols('x')


  fx = x**2+1-math.e**(x)

  gx = log(x**2+1)
  fx = fx.subs(x,xa)
  count = 0
  error = tolerance +1
  while (fx != 0) and (error >tolerance) and (count < niter):
    xn = gx.subs(x,xa)
    fx = fx.subs(x,xn)
    error = abs(xn-xa)
    xa = xn
    count += 1
  if fx == 0:
    print("{xa} is a root")
  elif error < tolerance:
    print("{0} It is a root with tolerance = {1}".format(xa,tolerance))
  else:
    print("fail the number of iterations {0}".format(niter))

fixed_point(0.000048,-0.5,100)
