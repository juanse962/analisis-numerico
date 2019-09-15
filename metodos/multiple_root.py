from sympy import *
import math

x = symbols('x')
function = x**3 - 5*x**2 +7*x -3
first_derivative = 3*x**2 - 10*x + 7
second_derivative = 6*x - 10

xi = input("Start point: ") 
tolerance = input("number of tolerance: ")
niter = input("number of iterations: ")

xi = float(xi)
tolerance = float(tolerance)
niter = int(niter)

fx = function.subs(x,xi)
fpx = first_derivative.subs(x,xi)
fppx = second_derivative.subs(x,xi)

denominator = fpx**2 - fx*fppx
count = 1
error = tolerance + 1

while (error > tolerance) and (fx !=0) and (count < niter) and (denominator != 0):
    xn = xi - (fx*fpx)/denominator
    fx = function.subs(x,xn)
    fpx = first_derivative.subs(x,xn)
    fppx = second_derivative.subs(x,xn)
    denominator = fpx**2 - fx*fppx
    error = abs(xn-xi)
    xi = xn
    count += 1

if fx == 0:
    print("{0} It's a root".format(xi))
elif error < tolerance:
    print("{0} approximately and a tolerance = {1}".format(xi,tolerance))
else:
        print("Failure of the number of iterations") 