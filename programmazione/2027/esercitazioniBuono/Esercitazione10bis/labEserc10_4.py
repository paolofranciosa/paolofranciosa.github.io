def parole_ordinate(lista_parole):
    if not isinstance(lista_parole, list):
        raise TypeError
    risultato = []
    for x in lista_parole:
        risultato.append(x)
    risultato.sort()
    return risultato

