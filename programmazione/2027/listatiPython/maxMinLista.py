def max_min_lista(lista):
    '''data una lista, restituisce il massimo e minimo elemento della lista'''
    if len(lista) == 0:
        return None, None
    max = lista[0]
    min = lista[0]
    for elem in lista[1:]:
        if elem > max:
            max = elem
        if elem < min:
            min = elem
    return max, min