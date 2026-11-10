def average(L):
    if not isinstance(L,list):
        raise TypeError
    for i in L:
        if not isinstance(i,int) and not isinstance(i,float):
            raise TypeError
        n=len(L)
        av=sum(L)/n
        return av
print(average([1,2,3,4,5]))