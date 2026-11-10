def sommavalorigrandi(D,soglia):
    '''accetta come argomento un
dizionario e un valore numerico,
e che calcola la somma di tutti i valori
corrispondenti ad una chiave del
dizionario, che siano strettamente
maggiori della soglia indicata
da secondo valore.'''
    tot=0
    for key in D:
        if D[key] > soglia:
            tot += D[key]
    return tot