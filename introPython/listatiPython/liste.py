def azzera(lista):
    for i in range(len(lista)):
        lista[i] = 0


def crea_lista_lunga_1(valore):
    '''creare una lista contenente un solo valore
e restituirla'''
    risultato = [valore]
    return risultato

pippo = crea_lista_lunga_1(44)
print(pippo)