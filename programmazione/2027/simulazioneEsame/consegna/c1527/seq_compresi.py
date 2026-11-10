def seq_compresi(L, low, high):
    a=[]
    for i in L:
        if i <=high and i>=low:
            a.append(i)
    return len(a)
seq = [3,5,1,8,4,2,5,7,6,3,4,1,9,8,4]
n = seq_compresi(seq,3,5)
print(n)