# labEserc8.4.py

def somma_diagonale_mat(m):
    if not isinstance(m, list):
        raise TypeError
    for r in m:
        if not isinstance(r, list):
            raise TypeError
    n = len(m)
    for r in m:
        if len(r) != n:
            raise ValueError
    for r in m:
        for x in r:
            if not isinstance(x, (int, float)):
                raise TypeError
    somma_diag = 0
    for i in range(len(m)):
        somma_diag += m[i][i]
    return somma_diag