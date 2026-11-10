def sommavalorigrandi(D,soglia):
    '''calcoli
la somma di tutti i valori corrispondenti ad una chiave del
dizionario, che siano strettamente maggiori della soglia indicata
da secondo valore.'''
    tot=0
    for i in D:
        if D[i]>soglia:
            tot+=D[i]
    return tot