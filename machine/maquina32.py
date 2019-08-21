def crear_maquina(bits_exponente, bits_mantisa):
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

    exponenteBinario = num(float(index), 0).split('.')[0]
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

    binario = num(float(numero), maquina['bits_mantisa'])
    normalzado = normalizar_bin(maquina['bits_exponente'], binario)
    maquina['mantisa'] = normalzado['binarioNormalizado'][3:maquina['bits_mantisa']+3]
    maquina['exponente'] = normalzado['exponente'][0:maquina['bits_exponente']]
    maquina['signoExp'] = normalzado['signo']

    return maquina

def binary_to_integer(number_binary):
    
    acum1 = 0

    if '.' in number_binary:
        acum2 = 0   
        integer,decimal = number_binary.split('.')
        integer = integer[::-1]
        decimal = decimal[::-1]
        long_decimal = (len(decimal) * -1)

        for i in range((len(integer) -1),-1,-1):
            if integer[i] == '1': acum1 += 2**i    

        for j in range(-1,long_decimal -1,-1):
            if decimal[j] == '1': acum2 += 2**j    
        
        return acum1 + acum2

    else:
        number_binary = number_binary[::-1]    
        for i in range(len(number_binary) -1,-1,-1):
            if number_binary[i] == '1': acum1 += 2**i    
        return acum1

def almacenar_en_maquina(maquina, numero):

    if numero < 0: 
        numero *= -1
        maquina['signoMant'] = 0
    binario = num(numero,maquina['bits_mantisa'])
    print(binario)
    normalzado = normalizar_bin(maquina['bits_exponente'], binario)
    maquina['mantisa'] = normalzado['binarioNormalizado'][3:maquina['bits_mantisa']+3]
    maquina['exponente'] = normalzado['exponente'][0:maquina['bits_exponente']]
    maquina['signoExp'] = normalzado['signo']
    return maquina

def sum_or_rest_or_mult(numero1, numero2, operacion, maquina):

    maquina = almacenar_en_maquina(maquina, numero1)
    numero1 = maquina_to_binario(maquina)

    maquina = almacenar_en_maquina(maquina, numero2)
    numero2 = maquina_to_binario(maquina) 
    
    if operacion == '+': return numero1 + numero2
    elif operacion == '-': return numero1 - numero2
    else: return numero1 * numero2
    
def maquina_to_binario(maquina):

    numero = '1'+maquina['mantisa']
    exponente = binary_to_integer(maquina['exponente'])

    if maquina['signoExp'] == 1 and exponente < len(numero):
        numero = numero[:exponente] + '.' + numero[exponente:]

    elif maquina['signoExp'] == 1 and exponente >= len(numero):
        exponente = exponente - len(numero)
        ceros = ''
        for i in range(exponente): 
            ceros = '0'+ceros 
        numero = numero + ceros + '.0'

    else:
        ceros = ''
        for i in range(exponente): 
            ceros = '0'+ceros 
        numero = '0.' + ceros + numero

    numero = binary_to_integer(numero)
    if maquina['signoMant'] == 0: numero = numero * -1

    return numero

def calcularMayor(maquina):

    exponente = maquina['bits_exponente']
    mantisa = maquina['bits_mantisa']

    maquinaTemp = {
        "bits_exponente": exponente,
        "bits_mantisa": mantisa,
        "signoMant": 1,
        "signoExp": 1,
        "exponente": '1'*exponente,
        "mantisa": '1'*mantisa
    }

    return maquina_to_binario(maquinaTemp)

def calcularMenor(maquina):

    exponente = maquina['bits_exponente']
    mantisa = maquina['bits_mantisa']

    maquinaTemp = {
        "bits_exponente": exponente,
        "bits_mantisa": mantisa,
        "signoMant": 1,
        "signoExp": 0,
        "exponente": '1'*exponente,
        "mantisa": '0'*mantisa
    }

    return maquina_to_binario(maquinaTemp)


def num(numero,parar):
    numero = str(numero)
    index = numero.find('.')
    numero = "".join(numero)
    entera = numero[:index]
    entera = entera.lstrip('0')
    decimal = numero[index+1:]
    lista = []
    if entera == '': entera = '0'
    entera = bin(int(entera))[2:]
    decimal ='0.' + decimal
    for i in range(0,parar):
        decimal = str(float(decimal) * 2)
        if decimal[0] == '0':
            lista.append('0')
            decimal = str(decimal)
        else:
            lista.append('1')
            decimal = str(float(decimal)-1)
    lista = "".join(lista)
    return entera +'.' +lista