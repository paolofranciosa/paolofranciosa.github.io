def dict_azzera(d, lista_chiavi):
    if not isinstance(d, dict):
        raise TypeError
    for k in d:
        if k in lista_chiavi:
            d[k] = 0
    return
 

