def sommavalorigrandi(D, soglia):
    somma=0
    for i in D.values():
        if soglia<i:
            somma+=i
    return somma
diz = {'xx': 44, 'yy': 33, 'zz': 22, 'qw': 22, 'das': 11}
print(sommavalorigrandi(diz,20))
print(sommavalorigrandi(diz,25))
print(sommavalorigrandi(diz,120))
    