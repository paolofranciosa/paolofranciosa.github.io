# labEserc8.2.py

def min_mat(m):
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
    min = m[0][0]
    for r in m:
        for x in r:
            if x < min:
                min = x
    return min