def coppia_differenza_minima(L):
    minima=3000000000000
    m1=0
    m2=0
    lista=[]
    for i in range(len(L)):
        f=L[i]
        for m in range(len(L)):
            if i!=m:
                diff=abs(f-L[m])
                if diff<minima:
                    m1=i
                    m2=m
                    minima=diff
    if m1<=m2:
        lista.append(m1)
        lista.append(m2)
    else:
        lista.append(m2)
        lista.append(m1)
    return lista
seq = [-5,4,8,-3,1,3,10]
print(coppia_differenza_minima(seq))