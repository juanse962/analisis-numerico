def crear_maquina(bits_exponente, bits_mantisa):
    return {
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
    binarioNormalizado = '0.' + binarioPartido[0] + binarioPartido[1]
    exponente = float(len(binarioPartido[0]))
    exponenteBinario = base10_base2(exponente, 0).split('.')[0]
    ceros_faltantes = bits_exponente-len(exponenteBinario)
    ceros_exponente = ''
    for i in range(ceros_faltantes): ceros_exponente = ceros_exponente + '0'
    exponenteBinario = ceros_exponente + exponenteBinario

    return {
        'binarioNormalizado': binarioNormalizado,
        'exponente': exponenteBinario
        }

def almacenar_en_maquina(bits_exponente, bits_mantisa, numero):
    maquina = crear_maquina(bits_exponente, bits_mantisa)
    binario = base10_base2(float(numero), bits_mantisa)
    print(binario)
    # TODO: Normalizacion cuando el entero es 0 
    normalzado = normalizar_bin(bits_exponente, binario)
    print(normalzado)
    maquina['mantisa'] = normalzado['binarioNormalizado'][3:bits_mantisa+3]
    maquina['exponente'] = normalzado['exponente'][0:bits_exponente]
    print(maquina)
    return maquina

almacenar_en_maquina(7, 23, 8.2)