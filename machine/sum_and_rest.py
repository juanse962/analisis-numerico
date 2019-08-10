operation = str(input('Operacion: '))

def sum_or_rest_or_mult(operation):
    sum1 = 0
    sum2 = 0
    
    res1 = 0 
    res2 = 0
    
    if '+' in operation:
        is_sum = 's'
        sum1,sum2 = operation.split("+")
        sum1 = float(sum1.replace(" ",""))
        sum2 = float(sum2.replace(" ",""))
        return sum1,sum2,is_sum  #Aca debemos almacenar los numeros en la maquina para despues 
   
    if '-' in operation:
        is_sum = 'r'
        res1,res2 = operation.split("-")
        res1 = float(res1.replace(" ",""))
        res2 = float(res2.replace(" ",""))
        return res1,res2,is_sum

    if '*' in operation:
        is_sum = 'm'
        mul1,mul2 = operation.split("*")
        mul1 = float(mul1.replace(" ",""))
        mul2 = float(mul2.replace(" ",""))
        return mul1,mul2,is_sum

l=sum_or_rest_or_mult(operation)
print(l[2])
