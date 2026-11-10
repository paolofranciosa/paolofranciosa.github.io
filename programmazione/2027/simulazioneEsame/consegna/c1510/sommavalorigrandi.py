def sommavalorigrandi(D,soglia):
    if not isinstance(D,dict):
        raise TypeError
    risultato=0
    for i in D:
        if soglia<D[i]:
            risultato+=D[i]
    return risultato
diz = {'xx': 44, 'yy': 33, 'zz': 22, 'qw': 22, 'das': 11}
print(sommavalorigrandi(diz,20))
print(sommavalorigrandi(diz,25))
print(sommavalorigrandi(diz,120))