def seq_compresi(L,low,high):
    risultato=0
    for i in L:
        if low<=L[i]<=high:
            risultato+=1
    return risultato
seq = [3,5,1,8,4,2,5,7,6,3,4,1,9,8,4]
n = seq_compresi(seq,3,5)
print(n)
        