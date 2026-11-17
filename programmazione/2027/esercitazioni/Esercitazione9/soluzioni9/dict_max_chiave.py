def dict_max_chiave(d):
    if not isinstance(d, dict):
        raise TypeError
    max_k = max(d.keys())
    return d[max_k]
 

