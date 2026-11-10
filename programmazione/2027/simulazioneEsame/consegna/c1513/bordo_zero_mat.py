def bordo_zero_mat(M):
    righe = len(M)
    colonne = len(M[0])
    
    for i in range(colonne):
        if M[0][i] != 0 or M[righe-1][i] != 0:
            return False
        
    for i in range(1, righe-1):
        if M[i][0] != 0 or M[i][colonne-1] != 0:
            return False
        
    return True