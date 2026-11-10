def somma_matrice(m):
    '''restituisce la somma di tutti gli elementi di una
matrice'''
    s = 0
    for riga in m:
        for elemento in riga:
            s += elemento
    return s

if __name__ == "__main__":
    print(somma_matrice([[1,3],[4,0],[5,2]]))
    print(somma_matrice([[0,2],[1,7]]))