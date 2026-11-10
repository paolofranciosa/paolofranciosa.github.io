def verifica_mat_rett(m):
    if not isinstance(m, list) or len(m) <= 0:
        return False
    for riga in m:
        if not isinstance(riga, list) or len(riga) <= 0:
            return False
    ncol = len(m[0])
    for riga in m:
        if len(riga) != ncol:
            return False
    return True

def crea_mat(nrighe, ncol, val=0):
    if not isinstance(nrighe, int) or not isinstance(ncol, int):
        raise TypeError
    if nrighe <= 0 or ncol <= 0:
        raise TypeError
    m = []
    for i in range(nrighe):
        m.append([])
        for j in range(ncol):
            m[i].append(val)
    return m

def trasposta(mat):
    if not verifica_mat_rett(mat):
        raise TypeError
    t = crea_mat(len(mat[0]), len(mat))
    for i in range(len(mat)):
        for j in  range(len(mat[0])):
            t[j][i] = mat[i][j]
    return t