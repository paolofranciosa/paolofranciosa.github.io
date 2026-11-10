def lista_somme_da_file(nomefile):
    if not isinstance(nomefile, str):
        raise TypeError
    lista = []
    with open(nomefile) as f:
        for riga in f:
            campi = riga.split(";")
            somma = 0
            for c in campi:
                somma += int(c)
            lista.append(somma)
    return lista
