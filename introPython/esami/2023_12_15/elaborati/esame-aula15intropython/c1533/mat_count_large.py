def mat_count_large(m, threshold):
    conta=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]>threshold:
                conta+=1
    return conta