def bordo_zero_mat(M):
    n_rig = len(M)
    n_col = len(M[0])
    
    for e in M[0]:
        if e != 0:
            return False
    for e in M[n_rig - 1]:
        if e != 0:
            return False
    for i in range(1, n_rig - 1):
        if M[i][0] != 0:
            return False
        if M[i][n_col - 1] != 0:
            return False
    return True
    
    