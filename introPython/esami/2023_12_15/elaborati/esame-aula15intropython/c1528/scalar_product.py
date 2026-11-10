def scalar_product(a,b):
    prodotto = 0
    i = 0
    while i<len(a):
        prodotto = prodotto + a[i]*b[i]
        i=i+1
    return prodotto
