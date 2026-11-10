def coppia_differenza_minima(L):
    minima = None
    indice1  = None
    indice2 = None
    for i in range(0, len(L)-1):
        for j in range(i+1,len(L)-1):
            if minima == None:
                minima = abs(L[j] - L[i])
                indice1 = i
                indice2 = j
            if abs(L[i] - L[j]):
                minima = abs(L[j] - L[i])
                indice1 = i
                indice2 = j
    return [indice1, indice2]
                
        
seq = [-5,4,8,-3,1,3,10]
print(coppia_differenza_minima(seq))                