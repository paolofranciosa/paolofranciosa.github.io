def average(L):
    somma = 0
    for i in range(len(L)):
        somma += L[i]
    avg = somma/len(L)
    return avg

H = [2,4,6,8]
print(average(H))