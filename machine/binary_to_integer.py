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

print(binary_to_integer('1100'))
print(binary_to_integer('11000.0001'))
