def pos_max_min_lista(lista):
    '''data una lista, restituisce le posizioni del massimo e
    del minimo elemento della lista'''
    if len(lista) == 0:
        return None, None
    pos_max = 0
    pos_min = 0
    for i in range(1, len(lista)):
        if lista[i] > lista[pos_max]:
            pos_max = i
        if lista[i] < lista[pos_min]:
            pos_min = i
    return pos_max, pos_min