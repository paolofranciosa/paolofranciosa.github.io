def scalar_product(a,b):
    conto = 0
    for i in range(len(a)):
        conto = conto + a[i]*b[i]
    return conto

lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
print(scalar_product(lista1,lista2))