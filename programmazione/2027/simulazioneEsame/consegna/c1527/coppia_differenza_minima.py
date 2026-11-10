def coppia_differenza_minima(L):
    a=0
    b= abs(max(L)-min(L))
    #c=0
    i=0
    j=i+1
    d= []
    for i in L:
        a=abs(i-L[j])
        if b>a:
            b=a
            d=[L[i], L[j]]
        i+=1
    return d
seq = [-5,4,8,-3,1,3,10]
print(coppia_differenza_minima(seq))
                
            