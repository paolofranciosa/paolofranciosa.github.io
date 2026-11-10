def mat_count_large(m,threshold):
    n=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]>threshold:
                n+=1
    return n           