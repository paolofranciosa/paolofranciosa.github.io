def mat_count_large(m, threshold):
    counter = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > threshold:
                counter = counter+1
    return counter

    