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
    binario = base10_base2(numero,maquina['bits_mantisa'])
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

    if maquina['signoExp'] == 1:
        numero = numero[:exponente] + '.' + numero[exponente:]
    else:
        ceros = ''
        for i in range(exponente): 
            ceros = '0'+ceros 
        numero = '0.'+ceros+numero

    numero = binary_to_integer(numero)
    if maquina['signoMant'] == 0: numero = numero * -1

    return numero
        
def exponentef (exponente):
    
        nExponente = 0;
        for i in range (0,exponente) :
            nExponente = nExponente + 2**i;
        return nExponente        
    
def mayor (maquina ):
    
        parteDecimal = 0;
        mEntera = 0;
        nExponente = exponentef (maquina['bits_exponente']);
    
        if maquina['bits_mantisa'] + 1 >= nExponente :
             
               for i in range (0,nExponente) :
                   mEntera = mEntera + 2**i; 
               
               for j in range (1,maquina['bits_mantisa'] + 1 - nExponente + 1):
                   parteDecimal = parteDecimal + 2**-j;
    
        if maquina['bits_mantisa'] + 1 < nExponente :
            
               for i in range (nExponente - maquina['bits_mantisa'] - 1, nExponente):
                   mEntera = mEntera + 2**i
    
        return (mEntera + parteDecimal)  
        
def menor (maquina):

        nExponente = exponentef (maquina['bits_exponente'])
        exponenteNeg = (nExponente * -1) -1
        numeroM = (2**exponenteNeg) 
        return numeroM
