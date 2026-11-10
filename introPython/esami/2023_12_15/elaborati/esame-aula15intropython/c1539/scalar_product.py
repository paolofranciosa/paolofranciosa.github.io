def scalar_product(a,b):
    prodotto=0
    for i in range(len(a)):
        somma=a[i]*b[i]
        prodotto+=somma
    return prodotto
s=scalar_product([1,4,3],[5,5,1])
print(s)