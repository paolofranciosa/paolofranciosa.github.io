def mat_count_large(m,threshold):
    conta=0
    for row in range(len(m)):
        for col in range(len(m[0])):
            if m[row][col]>threshold:
                conta+=1
    return conta

