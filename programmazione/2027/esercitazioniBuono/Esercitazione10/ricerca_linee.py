def ricerca_linee(nomefile, stringa):
    if not isinstance(nomefile, str):
        raise TypeError
    if not isinstance(stringa, str):
        raise TypeError
    lista = []
    num = 0
    with open(nomefile) as f:
        for riga in f:
            num += 1
            if stringa in riga:
                lista.append(num)
    return lista
