def coppia_differenza_minima(L):
    if not isinstance(L, list):
        raise TypeError
    r = []
    val = 0
    ris = 0
    el = 0
    diff = 0 
    for i in range(len(L)-1):
        for j in range(1,len(L)):
            if abs(L[i] - L[j]) < diff:
                diff += (L[i] - L[j])
                el = L[i]
                el2 = L[j]
    r.append(L[i])
    r.append(L[j])
            
            
            
                
                
    return r
seq = [-5,4,8,-3,1,3,10]
print(coppia_differenza_minima(seq))
        
        
        
            
            