def mat_count_large(m, threshold):
    r = len(m)
    c = len(m[0])
    conta = 0
    for i in range(r):
        for j in range(c):
            if m[i][j] > threshold:
                conta = conta+1
    return conta
