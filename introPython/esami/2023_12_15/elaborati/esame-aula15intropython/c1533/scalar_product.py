def scalar_product(a,b):
    somma=0
    for i in range(len(a)):
        prodotto=0
        prodotto=a[i]*b[i]
        somma+=prodotto
    return somma
        