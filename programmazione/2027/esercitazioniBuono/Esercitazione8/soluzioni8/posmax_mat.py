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


def posmax_mat(m):

    if not good_mat(m):
        raise TypeError

    R = len(m)
    C = len(m[0])
    massimo = m[0][0]
    massimo += 0  # to get TypeError if not num
    pos_r = 0
    pos_c = 0

    for i in range(R):
        for j in range(C):
            if massimo < m[i][j]:
                massimo = m[i][j]
                pos_r = i
                pos_c = j
    return pos_r, pos_c

