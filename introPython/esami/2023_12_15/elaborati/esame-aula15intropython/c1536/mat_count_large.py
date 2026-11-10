def mat_count_large(m, threshold):
    res = 0
    for row in m:
        for ele in row:
            if ele > threshold:
                res += 1
    return res