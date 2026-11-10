def average(L):
    summ=0
    l=len(L)
    for i in range(len(L)):
        summ+=L[i]
    avg=summ/l
    return(avg)
    
