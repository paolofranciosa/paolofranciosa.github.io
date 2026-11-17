def dict_da_stringa_parole(stringa):
    if not isinstance(stringa, str):
        raise TypeError
        
    lista_parole = stringa.split()
    if len(lista_parole) % 2 != 0:
        raise ValueError
        
    d = dict()
    for i in range(0, len(lista_parole), 2):
        d[lista_parole[i]] = lista_parole[i+1]
    return d
 

