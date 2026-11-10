def seq_compresi(L,low,high):
    """restituisce il numero di valori nella lista L che sono compresi tra low e high
(estremi inclusi)"""
    tot=0
    for i in L:
        if i>=low and i <=high:
            tot+=1
    return tot
    
    
seq = [3,5,1,8,4,2,5,7,6,3,4,1,9,8,4]
n = seq_compresi(seq,3,5)
print(n)