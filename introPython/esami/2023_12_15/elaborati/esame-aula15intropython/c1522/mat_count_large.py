def mat_count_large(m, threshold):
    larger = 0
    for el in m:
        for i in el:
            if i > threshold:
                larger += 1
    return larger

mat = [(1,2,3), (5,6,7), (9,10,11)]

print(mat_count_large(mat, 3))

