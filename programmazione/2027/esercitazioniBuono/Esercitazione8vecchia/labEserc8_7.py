# labEserc8.7.py

def pos_riga_massima_mat(m):
    if not isinstance(m, list):
        raise TypeError
    for r in m:
        if not isinstance(r, list):
            raise TypeError
    for r in m:
        for x in r:
            if not isinstance(x, (int, float)):
                raise TypeError
    if len(m) == 0:
        return -1
    lista_somme = []
    for r in m:
        somma = 0
        for x in r:
            somma += x
        lista_somme.append(somma)
    pos_max = 0
    for i in range(len(lista_somme)):
        if lista_somme[i] > lista_somme[pos_max]:
            pos_max = i
    return pos_max