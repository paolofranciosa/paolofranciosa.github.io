def bordo_zero_mat(M):
    if not isinstance(M, list):
        raise TypeError
    n = len(M)
    m = len(M[0])
    zeri = 0
    zeri2 = 0 
    for i in range(0, n):
        if M[i][0] == 0:
            zeri += 1
    for i2 in range(0, n):
        if M[i2][n] == 0:
            zeri2 += 1
    for i3 in range(0,n):
        if M[0][i3] == 0:
            zeri3 += 1
    for i4 in range(0,n):
        if M[m][i4] == 0:
            zeri4 += 1
    if zeri == zeri2  and zeri3 == zeri4 and zeri4==zeri:
    #sum(M[0])==0 and sum(M[n])==0:
        return True
    else:
        return False
M1 = [[0]]
M2 = [[0,0,0,0], [0,7,8,0] , [0,0,0,0]]
M3 = [[1,0,0], [0,8,0] , [0,2,-1], [0,0,0]]
print(bordo_zero_mat(M1))
print(bordo_zero_mat(M2))
print(bordo_zero_mat(M3))
                
                
        
    