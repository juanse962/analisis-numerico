import numpy as np
import sympy as sp
from sympy import *

x = symbols('x')
#Esto lo que mas importa
def trazalineal(xi,fi):
    n = len(xi)
    x = sp.Symbol('x')
    polinomio = []
    tramo=1
    while not(tramo>=n):
        m =(fi[tramo]-fi[tramo-1])/(xi[tramo]-xi[tramo-1])
        inicio = fi[tramo-1]-m*xi[tramo-1]
        ptramo = inicio + m*x
        polinomio.append(ptramo)
        tramo = tramo + 1
    return(polinomio)

xi = [-1 , 2, 3, 4]
fi = [2, -2, 2, 14]
polinomios = []
resolucion = 10 # entre cada par de puntos

n = len(xi)
polinomio = trazalineal(xi,fi)

# SALIDA
print('Polinomios por tramos: ')
for tramo in range(1,n,1):
    print(' x = ['+str(xi[tramo-1])
          +','+str(xi[tramo])+']')
    poli = str(polinomio[tramo-1])
    polinomios.append(poli)
    print(poli)
print(polinomios)

point_evaluated = float(input("Ingrese el punto a evaluar: "))
xi.sort()
negativo = xi[0]

if negativo < 0:
    aux= []
    for i in range(0,len(xi)):
        aux.append(abs(point_evaluated - xi[i]))
    menor = min(aux)
    index = int(aux.index(menor))
    evaluated = sympify(polinomios[index]).subs(x,point_evaluated)
    print(evaluated)
else:
    aux= []
    for i in range(0,len(xi)):
        aux.append(point_evaluated - xi[i])
    temp1 = 0
    temp2 = 0
    for i in range(0,len(xi)):
        if aux[i] > 0 and i == 0:
            temp = aux[i]
        elif aux[i] < temp and aux[i] > 0:
            temp = aux[i]

    index = int(aux.index(temp))
    evaluated = sympify(polinomios[index]).subs(x,point_evaluated)
    print(evaluated)