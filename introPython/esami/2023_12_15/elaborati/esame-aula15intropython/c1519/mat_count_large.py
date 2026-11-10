def mat_count_large(m, treshold):
    conta=0
    for i in range (0,len(m)):
        for j in range (0,len(m[i])):
            if m[i][j]>treshold:
                conta+=1
    return (conta)
print(mat_count_large([[2,3,1,4],[5,4,3,2]],1))
