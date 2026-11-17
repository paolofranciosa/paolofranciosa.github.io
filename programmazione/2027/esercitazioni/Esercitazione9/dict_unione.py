def dict_unione(d1, d2):
    unione = {}
    for k in d1:
        unione[k] = d1[k]
    for k in d2:
        if k in d1:
            unione[k] = unione[k] + d2[k]
        else:
            unione[k] = d2[k]
    return unione

