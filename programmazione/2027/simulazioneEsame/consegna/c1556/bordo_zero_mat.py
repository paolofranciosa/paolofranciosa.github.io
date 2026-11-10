def bordo_zero_mat(M):
    g = True
    for j in M:
        if j in M[0] != 0:
            return False
        if j in M[len(M) - 1] != 0:
            return False
        
        
    for i in M[0]:
        if i != 0:
            return False
    for k in M[len(M) - 1]:
        if k != 0:
            return False
    return g

M1 = [[0]]
M2 = [[0,0,0,0], [0,7,8,0] , [0,0,0,0]]
M3 = [[1,0,0], [0,8,0] , [0,2,-1], [0,0,0]]
print(bordo_zero_mat(M1))
print(bordo_zero_mat(M2))
print(bordo_zero_mat(M3))