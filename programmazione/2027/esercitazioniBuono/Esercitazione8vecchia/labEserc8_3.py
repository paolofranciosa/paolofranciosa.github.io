# labEserc8.3.py

def pos_max_mat(m):
    if not isinstance(m, list):
        raise TypeError
    if len(m) == 0 or len(m[0]) == 0:
        raise ValueError
    for r in m:
        if not isinstance(r, list):
            raise TypeError
    for r in m:
        for x in r:
            if not isinstance(x, (int, float)):
                raise TypeError
    r_max, c_max = 0, 0
    massimo = m[r_max][c_max]
    for ir in range(len(m)):
        for ic in range(len(m[ir])):
            if m[ir][ic] > massimo:
                r_max, c_max = ir, ic
                massimo = m[ir][ic]
    return r_max, c_max