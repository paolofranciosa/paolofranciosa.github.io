def binario(n):
    '''restituisce una stringa di 0-1 che rappresenta la codifica binaria di n
n si assume intero non negativo'''
    if n == 0:
        return "0"
    res = ""
    while n > 0:
        resto = n%2
        res = str(resto)+res
        n = n//2
    return res

print(binario(1920))
print(binario(1114112))
