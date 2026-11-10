def somma_lista(seq):
    '''restituisce la somma degli elementi
della lista'''
    if len(seq) == 0:
        return 0
    else:
        return seq[0] + somma_lista(seq[1:])
    
print(somma_lista([22,33,11,5]))