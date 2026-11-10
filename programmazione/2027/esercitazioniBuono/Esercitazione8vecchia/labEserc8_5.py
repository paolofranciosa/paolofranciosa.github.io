# labEserc8.5.py

def somme_per_riga_mat(m):
    if not isinstance(m, list):
        raise TypeError
    for r in m:
        if not isinstance(r, list):
            raise TypeError
    for r in m:
        for x in r:
            if not isinstance(x, (int, float)):
                raise TypeError
    lista_somme = []
    for r in m:
        somma = 0
        for x in r:
            somma += x
        lista_somme.append(somma)
    return lista_somme