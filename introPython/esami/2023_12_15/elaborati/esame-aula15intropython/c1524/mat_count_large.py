def mat_count_large(m, threshold):
    cnt = 0
    for i in m:
        for j in i:
            if j > threshold:
                cnt += 1
    return cnt 