def somma_lista_nidificata(l):
    '''dato un numero o una lista l, i cui elementi possono essere numeri o liste ricorsivamente,
restituisce la somma dei numeri presenti.
Ad esempio, se l = [[3, 6], [[1, 2], 5, [8]]]
restituisce 25'''
    if isinstance(l, (int, float)): # passo base: è un numero
        return l
    if isinstance(l, list): # passo ricorsivo: somma (ricorsiva) degli elementi
        tot = 0
        for e in l:
            tot += somma_lista_nidificata(e)
        return tot
    else:
        raise TypeError

if __name__ == "__main__":
    print(somma_lista_nidificata([[3, 6], [[1, 2], 5, [8]]]))
    print(somma_lista_nidificata([1, 2, 3, 4, 5]))
    print(somma_lista_nidificata(55))
    print(somma_lista_nidificata([]))
