def scalar_product(a,b):
    if len(a)==0:
        raise ValueError
    if len(b)==0:
        raise ValueError
    if len(a)!=len(b):
        raise TypeError
    ps=0
    for i in range(len(a)):
        ps=ps+(a[i]*b[i])
    return ps

