import math

def scalar_product(a,b):
    if not isinstance (a,list) and (b,list):
        raise TypeError
    scal_prod=0
    for x in range(len(a)):
        scal_prod+=a[x]*b[x]
    
    return scal_prod
