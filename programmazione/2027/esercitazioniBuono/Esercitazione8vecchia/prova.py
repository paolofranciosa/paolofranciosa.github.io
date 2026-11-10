# labEserc8.1.py

def somma_mat(m):
    if not isinstance(m, list):
        raise TypeError
    for r in m:
        if not isinstance(r, list):
            raise TypeError
    for r in m:
        for x in r:
            if not isinstance(x, (int, float)):
                raise TypeError
    somma = 0
    for r in m:
        for x in r:
            somma += x
    return somma