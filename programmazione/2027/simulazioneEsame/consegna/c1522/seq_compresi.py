def seq_compresi(L, low, high):
    if not isinstance(L, list):
        raise ValueError
    comp = 0 
    for i in L:
        if L[i]>=low and L[i]<=high:
            comp += 1
    return comp
seq = [3,5,1,8,4,2,5,7,6,3,4,1,9,8,4]
n = seq_compresi(seq,3,5)
print(n)
        
        