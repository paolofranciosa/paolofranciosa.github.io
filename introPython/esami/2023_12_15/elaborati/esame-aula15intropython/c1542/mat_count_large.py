def mat_count_large(m, threshold):
    count = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > threshold:
                count += 1
            
    return count

print(mat_count_large(((2,3), (4,8), (2,7), (9,8)), 6))