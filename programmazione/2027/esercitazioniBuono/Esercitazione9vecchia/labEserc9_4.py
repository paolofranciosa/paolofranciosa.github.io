def crea_mat(nrighe, ncol, val=0):
    if not isinstance(nrighe, int) or not isinstance(ncol, int):
        raise TypeError
    if nrighe <= 0 or ncol <= 0:
        raise ValueError
    m = []
    for i in range(nrighe):
        m.append([])
        for j in range(ncol):
            m[i].append(val)
    return m
