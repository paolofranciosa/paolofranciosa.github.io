def mat_count_large(m, t):
    if not isinstance(m,list):
        raise TypeError
    for i in m:
        if not isinstance(i,list):
            raise TypeError
    conta=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > t:
                conta+=1
    return conta
print(mat_count_large([[1,2,3],[4,6,7]],3))