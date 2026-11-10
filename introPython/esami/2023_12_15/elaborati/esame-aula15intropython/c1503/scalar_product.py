def scalar_product(a,b) :
    prodotto = 0
    for i in range (len(a)) :
        prodotto += a[i]*b[i]
    return(prodotto)

a = [2,3,4]
b=[3,4,5]
c = scalar_product(a,b)
print(c)

        