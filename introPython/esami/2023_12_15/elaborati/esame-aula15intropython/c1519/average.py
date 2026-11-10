def average(L):
    if not isinstance (L,list):
        type ('Error')
    somma=sum(L)
    average=somma/len(L)
    return (average)
print(average([1,2,3,4,5,9]))