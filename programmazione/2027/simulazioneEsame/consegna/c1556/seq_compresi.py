def seq_compresi(L, low, high):
    numerovalori = 0
    for i in L:
        if i >= low and i <= high:
            numerovalori += 1
    return numerovalori
seq = [3,5,1,8,4,2,5,7,6,3,4,1,9,8,4]
n = seq_compresi(seq,3,5)
print(n)
            
            