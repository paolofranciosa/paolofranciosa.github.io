def sommavalorigrandi(D,soglia):
    '''calcola la somma di tutti i valori corrispondenti
ad una chiave del dizionario, che siano strettamente
maggiori della soglia indicata dal secondo valore'''
    lista=[]
    valori= D.values()
    for i in valori:
        if i > soglia:
            lista.append(i)
    return sum(lista)

diz= {'a': 44, 'b': 5, 'c': 20}
print(sommavalorigrandi(diz,10))
    