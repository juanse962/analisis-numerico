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
    7
    res = bin(whole).lstrip("0b") + "."
  
    for x in range(places): 
  
        whole, dec = str((entero_aux(dec)) * 2).split(".") 
  
        dec = int(dec) 
        
        res += whole 
  
    return res 

def normalizar_bin(bits_exponente, binario):
    index = -1
    for i in binario:
        index += 1
        if i == '1': break
        if i == '.': index -= 1
        binario = binario[1:]
    binarioPartido = binario.split('.')[0]
    if len(binario.split('.')) == 2:
        binarioPartido = binario.split('.')[0] + binario.split('.')[1]

    binarioPartido = '0.'+ binarioPartido
    exponenteBinario = base10_base2(float(index), 0).split('.')[0]
    ceros_faltantes = bits_exponente-len(exponenteBinario)
    ceros_exponente = ''
    for i in range(ceros_faltantes): ceros_exponente = ceros_exponente + '0'
    exponenteBinario = ceros_exponente + exponenteBinario

    return {
        'binarioNormalizado': binarioPartido,
        'exponente': exponenteBinario
        }

def almacenar_en_maquina(maquina, numero):
    binario = base10_base2(float(numero), maquina['bits_mantisa'])
    print(binario)
    normalzado = normalizar_bin(maquina['bits_exponente'], binario)
    print(normalzado)
    maquina['mantisa'] = normalzado['binarioNormalizado'][3:maquina['bits_mantisa']+3]
    maquina['exponente'] = normalzado['exponente'][0:maquina['bits_exponente']]
    print(maquina)
    return maquina

# FIXME: Corregir exponente negativo
almacenar_en_maquina(crear_maquina(7,23), 8.2)

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

        
        
