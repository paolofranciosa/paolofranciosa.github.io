def coppia_differenza_minima(L):
    differenza_minima=abs(L[0]-L[1])
    posizione_i=0
    posizione_j=0
    for i in L:
        posizione_i+=
        posizione_j=0
        for j in L:
            if i!=j:
                posizione_j+=1
                if abs(i-j)<differenza_minima:
                    differenza_minima=abs(i-j)
                
    return posizione_i,posizione_j
seq = [-5,4,8,-3,1,3,10]
print(coppia_differenza_minima(seq))
            
             
            