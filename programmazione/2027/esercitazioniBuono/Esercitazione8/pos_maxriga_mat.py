def good_mat(m):
    if not isinstance(m, list):
        return False
    for row in m:
        if not isinstance(row, list):
            return False
    if len(m) == 0:
        return False

    if len(m[0]) == 0:
        return False

    for row in m:
        if len(row) != len(m[0]):
            return False
    return True


def pos_maxriga_mat(m):

    if not good_mat(m):
        raise TypeError

    massimo = sum(m[0])
    posizione = 0

    for i, row in enumerate(m):
        t = sum(row)
        if massimo < t:
            massimo = t
            posizione = i

    return posizione

