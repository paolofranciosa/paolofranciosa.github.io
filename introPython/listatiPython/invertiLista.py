def inverti_lista(l):
    '''inverte la lista parametro.'''
    for i in range(len(l) // 2):
        l[i], l[len(l)-(i+1)] = l[len(l)-(i+1)], l[i]
    return