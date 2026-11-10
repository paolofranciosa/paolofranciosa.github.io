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


def min_mat(m):

    if not good_mat(m):
        raise TypeError

    minimo = m[0][0]
    minimo += 0  # to get TypeError if not num

    for row in m:
        for val in row:
            if minimo > val:
                minimo = val
    return minimo

