def bordo_zero_mat(M) :
    for elemento in M[0] :
        if elemento != 0 :
            return False
    for elemento in M[len(M)-1] :
        if elemento != 0 :
            return False
        
    for i in range(1, len(M) - 1) :
        if M[i][0] or M[i][len(M[0])-1] != 0 :
            return False
            

        
    return True
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
matrice = [[0,0,0,0],
           [0,1,1,0],
           [0,1,1,0],
           [0,0,0,0]]
print(bordo_zero_mat(matrice))