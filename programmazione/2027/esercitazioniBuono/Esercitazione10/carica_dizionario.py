def carica_dizionario(nomefile):
    if not isinstance(nomefile, str):
        raise TypeError
    diz = {}
    with open(nomefile) as f:
        for riga in f:
            riga = riga.strip()
            k, v = riga.split()
            diz[k] = int(v)
    return diz
