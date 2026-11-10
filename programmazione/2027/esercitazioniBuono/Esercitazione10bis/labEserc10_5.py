def elimina_duplicati(lista_parole):
    if not isinstance(lista_parole, list):
        raise TypeError
    risultato = []
    prec = None
    for x in lista_parole:
        if x != prec:
            risultato.append(x)
        prec = x
    return risultato

