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

def dominates(a, b):
    for i in range(len(a)):
        if a[i] <= b[i]:
            return False
    return True

def mat_dominant_rows(m):

    if not good_mat(m):
        raise TypeError
    res = []
    for i in range(len(m)):
        domin = False
        for j in range(len(m)):
            if dominates(m[i], m[j]):
                domin = True
        if domin:
            res.append(i)
    return res

