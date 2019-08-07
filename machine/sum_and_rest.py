operation = str(input('Operacion: '))

def sum_or_rest(operation):
    sum1 = 0
    sum2 = 0
    
    res1 = 0 
    res2 = 0
    
    if '+' in operation:
        sum1,sum2 = operation.split("+")
        sum1 = float(sum1.replace(" ",""))
        sum2 = float(sum2.replace(" ",""))
        return sum1,sum2 #Aca debemos almacenar los numeros en la maquina convertirlos a binarios
    if '-' in operation:
        res1,res2 = operation.split("-")
        res1 = float(res1.replace(" ",""))
        res2 = float(res2.replace(" ",""))
        return res1,res2

print(sum_or_rest(operation))
