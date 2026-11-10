def mat_count_large(m, threshold):
    L = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > threshold:
                L.append(m[i][j])
    return len(L)