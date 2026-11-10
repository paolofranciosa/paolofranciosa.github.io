def mat_count_large(m, threshold):
    counter = 0
    for r in range(len(m)):
        for c in range(len(m[r])):
            if m[r][c] > threshold:
                counter += 1
    return counter
    print(counter)
    