def sommavalorigrandi(diz, soglia):
    n = diz.values()
    lista = []
    for i in n:
        if i > soglia:
            lista.append(i)
        tot = sum(lista)
    return tot





diz = {'xx': 44, 'yy': 33, 'zz': 22, 'qw': 22, 'das': 11}
print(sommavalorigrandi(diz,20))
print(sommavalorigrandi(diz,25))
print(sommavalorigrandi(diz,120))