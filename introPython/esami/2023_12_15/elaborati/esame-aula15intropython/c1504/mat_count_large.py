def mat_count_large(m, threshold):
    larger=[]
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]> trheshold:
                larger.append(m[i][j])
    return larger