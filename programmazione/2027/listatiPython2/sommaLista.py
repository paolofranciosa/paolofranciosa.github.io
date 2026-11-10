def somma_lista(lista):
    if not isinstance(lista,  list):
        raise TypeError
    s = 0
    for v in lista:
        if not isinstance(v, (int, float)):
            raise TypeError
        s += v
    return s

def conta_valori(l, v):
    ''' restituisce il  numero di elementi di l uguali a v'''
    if not isinstance(l, list):
        raise TypeError
    conta = 0
    for i in range(len(l)):
        if l[i] == v:
            conta += 1
    return conta


