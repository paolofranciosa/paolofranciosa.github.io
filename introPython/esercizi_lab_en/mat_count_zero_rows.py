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

def zeroes(r):
    for e in r:
        if e != 0:
            return False
    return True

def mat_count_zero_rows(m):

    if not good_mat(m):
        raise TypeError
    counter = 0
    for row in m:
        if zeroes(row):
            counter += 1
    return counter

