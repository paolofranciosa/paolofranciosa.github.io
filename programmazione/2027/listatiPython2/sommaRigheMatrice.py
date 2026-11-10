def somma_righe_matrice(m):
    '''restituisce la lista delle somme di ciascuna
riga di una matrice'''
    somme = []
    for riga in m:
        somme.append(somma_lista(riga))
    return somme

def somma_lista(l):
    '''restituisce la somma degli elementi di una lista'''
    risultato = 0
    for x in l:
        risultato += x
    return risultato


if __name__ == "__main__":
    print(somma_righe_matrice([[1,3],[4,0],[5,2]]))
    print(somma_righe_matrice([[0,2,-1],[1,-7,12]]))