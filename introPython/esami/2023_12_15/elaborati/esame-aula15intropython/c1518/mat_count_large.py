def mat_count_large(m,threshold):
    k=0
    for i in range(0,len(m)):
        for j in range(0,len(m[i])):
            if m[i][j]>threshold:
                k+=1
    return(k)
