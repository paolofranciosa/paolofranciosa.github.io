def sommavalorigrandi(D, soglia):
    somma = 0
    for i in D:
        if D[i] > soglia:
            somma = somma + D[i]
    return somma

