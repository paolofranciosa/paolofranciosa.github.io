def average(L):
    if not isinstance(L,list):
        raise TypeError
    for i in range(len(L)):
        if not isinstance(L[i],(float,int)):
            raise TypeError
    somma=0
    n=len(L)
    for i in range(n):
        somma+=L[i]
    media=somma/n
    return media

