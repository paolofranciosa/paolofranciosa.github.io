def sommavalorigrandi(D, soglia):
    tot = 0
    for i in D:
        if D[i] > soglia:
            tot += D[i]
    return tot
diz = {'xx': 44, 'yy': 33, 'zz': 22, 'qw': 22, 'das': 11}
print(sommavalorigrandi(diz,20))