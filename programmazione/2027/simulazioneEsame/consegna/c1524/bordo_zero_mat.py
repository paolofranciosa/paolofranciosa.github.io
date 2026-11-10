def bordo_zero_mat(M):
    bordanza = True
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i == 0 or i == len(M)-1 or j == 0 or j == len(M[0])-1:
                if M[i][j] != 0:
                    bordanza = False
    return bordanza

    
    
