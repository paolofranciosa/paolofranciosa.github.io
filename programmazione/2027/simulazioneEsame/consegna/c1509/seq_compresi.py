def seq_compresi(L,low,high):
    """restituisca il
numero di valori nella lista L che sono compresi tra low e high
(estremi inclusi)."""
    num_val = 0
    for i in L:
        if L[i] >= low and L[i] <= high:
            num_val += 1
        else:
            num_val = num_val
    return num_val

seq = [3,5,1,8,4,2,5,7,6,3,4,1,9,8,4]
n = seq_compresi(seq,3,5)
print(n)