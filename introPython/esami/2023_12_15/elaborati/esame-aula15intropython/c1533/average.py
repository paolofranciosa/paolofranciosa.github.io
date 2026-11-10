def average(L):
    if not isinstance(L,list):
        raise TypeError
    somma=0
    for i in L:
        somma+=i
    media=somma/len(L)
    return media
    