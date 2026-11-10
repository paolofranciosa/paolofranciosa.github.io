def seq_compresi(L,low,high):
    '''Restituisce il
numero di valori nella lista L che sono compresi tra low e high
(estremi inclusi).'''
    numero=0
    for i in L:
        if L[i]>=low and L[i]<=high:
            numero+=1
    return numero