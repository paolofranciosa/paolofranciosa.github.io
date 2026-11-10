diz = {'xx': 44, 'yy': 33, 'zz': 22, 'qw': 22, 'das': 11}

def sommavalorigrandi(diz,x):
    totale = 0
    for i in diz :
        if diz[i] > x :
            totale += diz[i]
    return totale
print(sommavalorigrandi(diz, 34))
print(sommavalorigrandi(diz, 20))
print(sommavalorigrandi(diz, 25))
print(sommavalorigrandi(diz, 120))