def crear_maquina(bits_exponente, bits_mantisa):
    
    if bits_exponente + bits_mantisa != 30:
        return False
    else:    
        return {
            "bits_exponente": bits_exponente,
            "bits_mantisa": bits_mantisa,
            "signoMant": 1,
            "signoExp": 1,
            "exponente": 1,
            "mantisa": 1
        }

def entero_aux(num): 

    while num > 1: 
        num /= 10

    if num == 0: num = 0.0
    elif num == 1: num = 0.1

    return num  

def base10_base2(number, places): 
  
    whole, dec = str(number).split(".") 
    whole = int(whole) 
    dec = int (dec) 
    res = bin(whole).lstrip("0b") + "."
  
    for x in range(places): 
  
        whole, dec = str((entero_aux(dec)) * 2).split(".") 
        dec = int(dec) 
        res += whole 
  
    return res 

def normalizar_bin(bits_exponente, binario):

    binarioPartido = binario.split('.')
    if '1' in binarioPartido[0]:

        signo = 1
        index = len(binarioPartido[0])
        binario = '0.'+binarioPartido[0]+binarioPartido[1]

    else:
        signo = 0
        index = -1

        for i in binario:
            if i == '1': break
            binario = binario[1:]
            index += 1

        binario = '0.'+binario

    exponenteBinario = base10_base2(float(index), 0).split('.')[0]
    ceros_faltantes = bits_exponente-len(exponenteBinario)
    ceros_exponente = ''

    for i in range(ceros_faltantes): ceros_exponente = ceros_exponente + '0'
    exponenteBinario = ceros_exponente + exponenteBinario

    return {
        'binarioNormalizado': binario,
        'exponente': exponenteBinario,
        'signo': signo
        }

    if numero < 0: 

        numero *= -1
        maquina['signoMant'] = 0

    binario = base10_base2(float(numero), maquina['bits_mantisa'])
    normalzado = normalizar_bin(maquina['bits_exponente'], binario)
    maquina['mantisa'] = normalzado['binarioNormalizado'][3:maquina['bits_mantisa']+3]
    maquina['exponente'] = normalzado['exponente'][0:maquina['bits_exponente']]
    maquina['signoExp'] = normalzado['signo']

    return maquina

def binary_to_integer(number_binary):
    
    aux1 = 0
    aux2 = 0   

    if '.' in number_binary:

        integer,decimal = number_binary.split('.')
        integer = integer[::-1]
        decimal = decimal[::-1]
        long_integer = len(integer) -1
        long_decimal = (len(decimal) * -1)-1

        for i in range(long_integer,-1,-1):
            if integer[i] == '1': aux1 += 2**i    

        for j in range(-1,long_decimal,-1):
            if decimal[j] == '1': aux2 += 2**j    

        return str(aux1 + aux2)

    else:

        integer = number_binary
        integer = integer[::-1]
        long_integer = len(integer) -1
        
        for i in range(long_integer,-1,-1):
            if integer[i] == '1': 
                aux1 += 2**i
                
        return str(aux1)

def maquina_to_cadena(maquina):

    bit_significativo = maquina['mantisa']
    exponente = int(binary_to_integer(maquina['exponente'])) - 1
    sign_exponente = maquina['signoExp']
    sign_mantiza = maquina['signoMant']
    index = 0
    cadena = []

    if sign_exponente == 0:

        for i in bit_significativo:

            if index == exponente:
                break
            cadena.append('0')
            index += 1
            
        cadena = str("".join(cadena))
        cadena = cadena + '.' + bit_significativo[exponente:]

    else:
        for i in bit_significativo:

            cadena.append(i)
            index += 1

            if index == exponente:

                cadena.append(i)
                cadena = str("".join(cadena))
                index += 1
                decimal = bit_significativo[index:]
                cadena ='1' + cadena[1:] + '.' + decimal
                break
    
    
    cadena = binary_to_integer(cadena)

    if sign_mantiza == 0:
        cadena = '-' + cadena
    else:
        cadena = '+' + cadena
    return cadena

        
def almacenar_en_maquina(maquina, numero):
    numero= float(numero)
    if numero < 0: 
        numero *= -1
        maquina['signoMant'] = 0
    binario = base10_base2(numero,maquina['bits_mantisa'])
    normalzado = normalizar_bin(maquina['bits_exponente'], binario)
    maquina['mantisa'] = normalzado['binarioNormalizado'][3:maquina['bits_mantisa']+3]
    maquina['exponente'] = normalzado['exponente'][0:maquina['bits_exponente']]
    maquina['signoExp'] = normalzado['signo']
    return maquina

def sum_or_rest_or_mult(maquina,operation):

    sum1 = 0
    sum2 = 0
    operation = operation
    res1 = 0 
    res2 = 0
    mul1 = 0
    mul2 = 0
    result = 0
    
    
    if '+' in operation:

        sum1,sum2 = operation.split("+")
        sum1 = float(sum1.replace(" ",""))
        sum2 = float(sum2.replace(" ",""))

        almacenar_sum1 = almacenar_en_maquina(maquina,sum1)
        almacenar_sum1 = maquina_to_cadena(almacenar_sum1)

        almacenar_sum2 = almacenar_en_maquina(maquina,sum2)
        almacenar_sum2 = maquina_to_cadena(almacenar_sum2)
        return int(almacenar_sum1) + int(almacenar_sum2)

    if '-' in operation:

        res1,res2 = operation.split("-")
        res1 = float(res1.replace(" ",""))
        res2 = float(res2.replace(" ",""))

        almacenar_res1 = almacenar_en_maquina(maquina,res1)
        almacenar_res1 = maquina_to_cadena(almacenar_res1)

        almacenar_res2 = almacenar_en_maquina(maquina,res2)
        almacenar_res2 = maquina_to_cadena(almacenar_res2)
        return int(almacenar_res1) - int(almacenar_res2)

    if '*' in operation:

        mul1,mul2 = operation.split("*")
        mul2 = float(mul2.replace(" ",""))
        mul1 = float(mul1.replace(" ",""))

        almacenar_mul1 = almacenar_en_maquina(maquina,mul1)
        almacenar_mul1 = maquina_to_cadena(almacenar_mul1)

        almacenar_mul2 = almacenar_en_maquina(maquina,mul2)
        almacenar_mul2 = maquina_to_cadena(almacenar_mul2)
        return int(almacenar_mul1) * int(almacenar_mul2)

