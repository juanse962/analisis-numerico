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
    print("Bits-Exponente: ", exponente)
    print("Bits-Mantisa: ", mantisa)
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
        print("6. Sumar numeros")
        print("7. Restar numeros")
        print("8. Multiplicar numeros")
        print("9. Cambiar maquina")
        print("10. Salir")
        opcion = input("")
        if len(opcion) is not 0 and opcion.isdigit(): return (int(opcion))


print("\033[1mBienvenido maquina de 32 bits\033[0m")
operation = ''
maquina = solicitarMaquina()

while True :

    opcion = seleccionarOpcion()
    if opcion == 1:
        
        print('El numero mas grande de la maquina es: ',maquina32.mayor(maquina) ) 
        
    elif opcion == 2:
   
        
        print('El numero mas pequenio es: ',maquina32.menor(maquina) )

    elif opcion == 3:
    
      epsilon = 2**(maquina['bits_mantisa']*-1)
      print("El epsilon de la maquina es: ",epsilon)

    elif opcion == 4:

        print("\n4. Convertir base 10 a numero de maquina")
        print("Puedes pulsar B para regresar al menu anterior \n")
        numero = input("Introduce el numero en base 10: ")
        if numero == 'B': continue

        elif len(numero) is not 0:
            numero = float(numero)
            maquina = maquina32.almacenar_en_maquina(maquina, numero)
            print('signo exponente: ',maquina['signoExp'])
            print('signo mantisa: ',maquina['signoMant'])
            print('exponente: ',maquina['exponente'])
            print('mantisa: ',maquina['mantisa'])
            print('El numero que guarda la maquina es: ',maquina32.machine_to_string(maquina))

        else:
            print ("Input invalido")
        
    elif opcion == 5:

        print("\n5. Convertir numero de maquina a base 10")
        print("Puedes pulsar B para regresar al menu anterior \n")
        print('Nota: utilize el punto decimal (.) en vez de la coma (,)')

        cadena = input("Introduce el numero en base 2: ")
        if cadena == 'B': continue

        elif len(cadena) is not 0:
            print("El resultado es: ", maquina32.binary_to_integer(cadena))
        else:
            print ("Input invalido")

    elif opcion == 6:

        print("\n6. Sumar numeros")
        print("Puedes pulsar B para regresar al menu anterior \n")
        print("Solo escribe los numeros sin necesidad de (+)")
        numero1 = input("Numero 1: ")
        if numero1 == 'B': continue
        numero2 = input("Numero 2: ")
        if numero2 == 'B': continue

        if len(numero1) is not 0 and len(numero2) is not 0:
            print('El resultado es: ',maquina32.sum_or_rest_or_mult(float(numero1), float(numero2), '+', maquina))
        else:
            print ("Input invalido")
        
    elif opcion == 7:

        print("\n7. Restar numeros")
        print("Puedes pulsar B para regresar al menu anterior \n")
        print("Solo escribe los numeros sin necesidad de (-)")

        numero1 = input("Numero 1: ")
        if numero1 == 'B': continue
        numero2 = input("Numero 2: ")
        if numero2 == 'B': continue

        if len(numero1) is not 0 and len(numero2) is not 0:
            print('El resultado es: ',maquina32.sum_or_rest_or_mult(float(numero1), float(numero2), '-', maquina))
        else:
            print ("Input invalido")

    elif opcion == 8:
        
        print("\n8. Multiplicar numeros")
        print("Puedes pulsar B para regresar al menu anterior \n")
        print("Solo escribe los numeros sin necesidad de (*)")

        numero1 = input("Numero 1: ")
        if numero1 == 'B': continue
        numero2 = input("Numero 2: ")
        if numero2 == 'B': continue

        if len(numero1) is not 0 and len(numero2) is not 0:
            print('El resultado es: ',maquina32.sum_or_rest_or_mult(float(numero1), float(numero2), '*', maquina))
        else:
            print ("Input invalido")

    elif opcion == 9:

        print("\n9. Cambiar maquina")
        print("Puedes pulsar B para regresar al menu anterior \n")
        crear_maquina = input("Presiona la tecla ENTER para continuar, recuerda la maquina actual se borrara: ")
        if crear_maquina == 'B': continue
        elif crear_maquina == '': 
            maquina = solicitarMaquina()
        else:
            print ("Input invalido")   
            
    elif opcion == 10:
          break
    else:

        print("Opcion invalida")

a = maquina32.crear_maquina(3,3)