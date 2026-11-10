def sommaliste(a, b):

    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError

    if len(a) != len(b):
        raise ValueError

    res = []
    for i in range(len(a)):
        if not isinstance(a[i], int) or not isinstance(b[i], int):
            raise TypeError

        res.append(a[i] + b[i])

    return res

