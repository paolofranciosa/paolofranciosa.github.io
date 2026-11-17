def dict_rimuovi(d, lista_chiavi):
    if not isinstance(d, dict):
        raise TypeError
    new_d = {}
    for k in d:
        if k not in lista_chiavi:
            new_d[k] = d[k]
    return new_d
 

