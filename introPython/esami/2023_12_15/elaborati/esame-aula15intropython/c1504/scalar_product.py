def scalar_product(a,b):
    if not isinstance(a, list):
        raise TypeError   
    if not isinstance(b, list):  
        raise TypeError
    if len(a) != len(b):
        raise ValueError
        if len(a)>0:
            prod = 0
            for i in range(len(a)):
                prod += a[i] * b[i]
        return prod
