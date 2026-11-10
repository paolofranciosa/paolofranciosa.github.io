def scalar_product(a,b):
    if not isinstance (a,list):
        raise TypeError
    if not isinstance (b,list):
        raise TypeError
    if len(a)==0 or len(b)==0:
        return None
    if len(a)!=len(b):
        return None
    for i in range(len(a)):
        if not isinstance(a[i],(int,float)):
            raise TypeError
        if not isinstance(b[i],(int,float)):
            raise TypeError
    somma_prodotto=0
    for i in range(len(a)):
        somma_prodotto+=(a[i]*b[i])
    return somma_prodotto


    