from sympy import *
import math

x = symbols('x')
function = log(x**2+1) +x*cos(6*x+3)-3*x-10

x0= input("Write the initial value: ") 
delta = input("interval length (delta): ")
niter = input("number of iterations: ")

x0 = float(x0)
delta = float(delta)
niter = int(niter)

fx0 = function.subs(x, x0)

if fx0 == 0:
    print("{0} It's a root.".format(x0))
else:
    x1 = x0 + delta
    count = 1
    fx1 = function.subs(x,x1)

    while (fx0 * fx1 > 0) and count < niter:
        x0 = x1
        fx0 = fx1
        x1 = x0 + delta 
        fx1 = function.subs(x,x1)
        count += 1
    if fx1 == 0:
        print("There's a root: ",x1)

    elif fx0 * fx1 < 0:
        print('There is a root between %.4f and %.4f ' % (x0,x1))
    else:
        print("The maximum number of iterations was reached")

