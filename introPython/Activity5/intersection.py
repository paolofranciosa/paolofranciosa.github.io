def intersection(a, b):
    res = []

    for x in a:
        if x in b:
            res.append(x)
    return sorted(res)

