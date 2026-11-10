def average(L):
    sum=0
    for x in L:
        if not isinstance(x,(int,float)):
            raise ValueError
        sum+=x
    avg=sum/len(L)
    return avg
    

    