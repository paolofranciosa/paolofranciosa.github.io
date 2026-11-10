def unione(a, b):

    res = a[:]

    for x in b:
        if x not in res:
            res.append(x)

    return sorted(res)

