def bordo_zero_mat(M):
    for i in M[0]:
        if i != 0:
            return False
    for i in M[len(M)]:
        if sum(M[len(M)]) != 0:
            return False
    for i in M:
        if i[0] or i[len(i)] != 0:
            return False  
    return True


bordo_zero_mat(M)

M1 = [[0]]
print(bordo_zero_mat(M))
M2 = [[0,0,0,0], [0,7,8,0] , [0,0,0,0]]
print(bordo_zero_mat(M))
M3 = [[1,0,0], [0,8,0] , [0,2,-1], [0,0,0]]
print(bordo_zero_mat(M))