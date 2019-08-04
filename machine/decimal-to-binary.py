def decimalToBinary(number):

    num = number
    l = []

    while num >= 1:
        l.insert(0,num%2)
        num = num // 2

    result = "".join(str(i) for i in l)

    return result

print(decimalToBinary(8))
