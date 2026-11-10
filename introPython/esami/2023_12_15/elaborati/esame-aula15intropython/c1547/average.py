def average(L):
    if not isinstance(L,list):
        raise TypeError
    for i in L:
        if not isinstance(i,(int,float)):
            raise TypeError
    if len(L)==0:
        return 0
    return sum(L)/len(L)

