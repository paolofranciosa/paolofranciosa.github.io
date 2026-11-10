def mat_count_large(m, threshold):
    count = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > threshold:
                count = count + 1
    return print(count)

a = [1,2,3,4,5]
b = [3,5,6,7,8,9]
c = [4,4,2]
matrice = [a,b,c]
limite = 5

mat_count_large(matrice,limite)
