def seq_compresi(L,low,high):
    totale = []
    for i in L:
        if low <= L[i] <= high:
            totale.append(L[i])
    return (len(totale))

seq = [3,5,1,8,4,2,5,7,6,3,4,1,9,8,4]
n = seq_compresi(seq,3,5)
print(n)
            
    