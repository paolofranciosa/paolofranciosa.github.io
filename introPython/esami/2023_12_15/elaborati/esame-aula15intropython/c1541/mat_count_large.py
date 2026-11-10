def mat_count_large(m,threshold):
    counter=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]>threshold:
                counter+=1
    return counter

m=[[1,2,3],[3,5,2],[9,12,5]]
print(mat_count_large(m,5))
print(mat_count_large(m,4))
            