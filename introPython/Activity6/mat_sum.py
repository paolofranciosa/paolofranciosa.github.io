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


def mat_sum(m):

    res = 0

    for row in m:
        for val in row:
            res += val
    return res

