def seq_compresi(L,low,high):
    totale = 0
    for i in range(0, len(L)):
        if L[i]>= low and L[i]<= high:
            totale += 1
        else:
            totale = totale
    return totale




seq = [3,5,1,8,4,2,5,7,6,3,4,1,9,8,4]
n = seq_compresi(seq,3,5)
print(n)