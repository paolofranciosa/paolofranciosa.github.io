# labEserc8.6.py

def somme_per_colonna_mat(m):
    if not isinstance(m, list):
        raise TypeError
    for r in m:
        if not isinstance(r, list):
            raise TypeError
    if len(m) > 0:
        n_col = len(m[0])
        for r in m:
            if len(r) != n_col:
                raise ValueError
    for r in m:
        for x in r:
            if not isinstance(x, (int, float)):
                raise TypeError
    if len(m) == 0:
        return []
    lista_somme = []
    for ic in range(len(m[0])):
        somma = 0
        for ir in range(len(m)):
            somma += m[ir][ic]
        lista_somme.append(somma)
    return lista_somme