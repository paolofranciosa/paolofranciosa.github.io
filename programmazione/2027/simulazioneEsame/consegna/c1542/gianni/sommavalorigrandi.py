def sommavalorigrandi(D, soglia):
    somma = 0
    for valore in D.values():
        if valore > soglia:
            somma += valore
    return somma