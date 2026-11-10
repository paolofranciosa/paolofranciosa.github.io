def list_difference(a, b):

    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError

    res = []
    for x in a:
        if x not in b:
            res.append(x)
    return res

