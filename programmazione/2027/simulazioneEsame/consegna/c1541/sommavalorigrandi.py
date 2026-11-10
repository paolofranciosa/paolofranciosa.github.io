def sommavalorigrandi(D,soglia):
    """funzione che accetta come argomento un dizionario e un valore numerico, e che calcoli
la somma di tutti i valori corrispondenti ad una chiave del
dizionario, che siano strettamente maggiori della soglia indicata
da secondo valore"""
    tot=0
    for k in D:
        if D[k]>soglia:
            tot+=D[k]
    return tot

diz = {'xx': 44, 'yy': 33, 'zz': 22, 'qw': 22, 'das': 11}
print(sommavalorigrandi(diz,20))
print(sommavalorigrandi(diz,25))
print(sommavalorigrandi(diz,120))