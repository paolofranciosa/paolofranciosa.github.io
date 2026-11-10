def mat_count_large(m,threshold):
    count=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]>threshold:
                count+=1
    return count
s=mat_count_large([[1,5,3],[4,7,9],[1,2,9]],6)
print(s)