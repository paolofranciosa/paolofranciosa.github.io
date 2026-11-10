def mat_count_large(m,threshold) :
    conta = 0
    for i in range(len(m)) :
        for e in range(len(m[i])):
            if m[i][e] > threshold :
                conta+=1
    return conta
a = [[2,1,4],[5,1,2],[4,1,7]]
c = mat_count_large(a,4)
print(c)
            
        