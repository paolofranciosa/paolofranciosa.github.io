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


def somme_per_colonna_mat(m):

    if not good_mat(m):
        raise TypeError

    R = len(m)
    C = len(m[0])

    sums = [0] * C

    for i in range(R):
        for j in range(C):
            sums[j] += m[i][j]

    return sums

