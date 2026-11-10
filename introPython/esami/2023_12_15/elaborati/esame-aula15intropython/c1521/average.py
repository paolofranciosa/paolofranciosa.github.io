def average(L):
    if not isinstance(L,list):
        raise TypeError
    for i in L:
        if not isinstance(i,(int,float)):
            raise TypeError
    total = 0
    for i in L:
        total = total + i
    average = total/len(L)
    return average