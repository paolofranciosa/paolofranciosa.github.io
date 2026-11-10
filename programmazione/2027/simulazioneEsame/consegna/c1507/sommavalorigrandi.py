def sommavalorigrandi(D,soglia):
    '''accetti
come argomento un dizionario e un valore numerico, e che calcoli
la somma di tutti i valori corrispondenti ad una chiave del
dizionario, che siano strettamente maggiori della soglia indicata
da secondo valore.'''
    somma = 0
    for i in D:
        if D[i] > soglia:
            somma += D[i]
    return somma

diz = {'xx': 44, 'yy': 33, 'zz': 22, 'qw': 22, 'das': 11}
print(sommavalorigrandi(diz,20))
print(sommavalorigrandi(diz,25))
print(sommavalorigrandi(diz,120))

