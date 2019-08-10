#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unicodedata
import maquina32
 
def solicitarMaquina():

    digitosValidos = False

    while not digitosValidos:
        mantisa = input("Numero de la mantisa: ")
        exponente = input("Numero del exponente: ")
    
        if len(mantisa) is not 0 and len(exponente) is not 0 and mantisa.isdigit() and exponente.isdigit():
            maquina = maquina32.crear_maquina(int(exponente), int(mantisa))
            if not maquina:
                print ('Bits de mantisa y exponente invalidos para maquina de 32-bits.')
            else:
                digitosValidos = True
        else:
            print('Digitos invalidos \n')
    return maquina

def seleccionarOpcion():

    salir = False
    while not salir:
        print("\n Seleccione una opcion")
        print("1. Calcular numero mas grande de la maquina")
        print("2. Calcular numero mas pequenio de la maquina")
        print("3. Calcular epsilon de la maquina")
        print("4. Convertir base 10 a numero de maquina")
        print("5. Convertir numero de maquina a base 10")
        print("6. Sumar numeros de maquina")
        print("7. Restar numeros de maquina")
        print("8. Multiplicar numeros de maquina")
        print("9. Cambiar maquina")
        print("10. Salir")
        opcion = input("")
        if len(opcion) is not 0 and opcion.isdigit(): return (int(opcion))


print ("Bienvenido maquina de 32 bits")
operation = ''
maquina = solicitarMaquina()

while True :

    opcion = seleccionarOpcion()
    if opcion == 1:
        1
    elif opcion == 2:
        2
    elif opcion == 3:
        3
    elif opcion == 4:

        numero = input("Introduce el numero en base 10: ")
        if len(numero) is not 0:
            maquina = maquina32.almacenar_en_maquina(maquina, numero)
            maquina = maquina32.maquina_to_cadena(maquina)
            print('El numero que guarda la maquina es: ',maquina)

        else:
            print ("Input invalido")
        
    elif opcion == 5:

        cadena = input("Introduce el numero en base 10: ")
        if len(cadena) is not 0:
            print("El resultado es: ", maquina32.binary_to_integer(cadena))
        else:
            print ("Input invalido")

    elif opcion == 6:

        operation = str(input('Operacion: '))
        if '+' in operation:
            result = maquina32.sum_or_rest_or_mult(maquina,operation)
            print('El resultado es: ',result)
        else:
            print ("Input invalido")
        
    elif opcion == 7:

        operation = str(input('Operacion: '))

        if '-' in operation:
            result = maquina32.sum_or_rest_or_mult(maquina,operation)
            print('El resultado es: ',result)
        else:
            print ("Input invalido")

    elif opcion == 8:
        
        operation = str(input('Operacion: '))

        if '*' in operation:
            result = maquina32.sum_or_rest_or_mult(maquina,operation)
            print('El resultado es: ',result)
        else:
            print ("Input invalido")

    elif opcion == 9:
        9
    elif opcion == 10:
          break
    else:
        print("Opcion invalida")


a = maquina32.crear_maquina(3,3)

 

 