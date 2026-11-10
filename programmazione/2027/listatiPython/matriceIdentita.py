def mat_zero(r, c):
    m = []
    for i in range(r):
        riga = []
        for j in range(c):
            riga.append(0)
        m.append(riga)
    return m

def mat_identita(n):
    '''crea e restituisce la matrice identità n x n'''
    if not isinstance(n, int):
        raise TypeError
    if n < 0:
        raise ValueError
    risultato = mat_zero(n, n) # matrice quadrata di zeri n x n
    # modificare gli elementi sulla diagonale assegnando 1
    for i in range(n):
        risultato[i][i] = 1
    return risultato

if __name__ == "__main__":
    print(mat_identita(3))