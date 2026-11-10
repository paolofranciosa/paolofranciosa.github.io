def seq_compresi(L, low, high):
    '''restituisce il numero di valori nella lista L
che sono compresi tra low e high'''
    conta=0
    for i in L:
        if i>=low and i<=high:
            conta+=1
    return conta

print(seq_compresi([3,5,6,2,8], 3, 6))


    