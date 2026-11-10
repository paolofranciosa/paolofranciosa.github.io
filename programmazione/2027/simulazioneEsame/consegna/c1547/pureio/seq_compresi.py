def seq_compresi (L, low, high):
    n = 0
    for i in L:
        if i >= low and i <= high:
            n += 1
    return n

L = [3,5,1,8,4,2,5,7,6,3,4,1,9,8,4]
print(seq_compresi(L,3,5))
print(seq_compresi(L,3,8))
print(seq_compresi(L,2,7))
