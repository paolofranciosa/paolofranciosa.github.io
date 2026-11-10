def verifica_diagonale(mat):
    '''restituisce True se e solo se mat e' una matrice diagonale
Se mat non e' quadrata o non è diagonale restituisce False'''
    if len(mat) == 0: # matrice vuota
        return True
    # verifichiamo che tutte le righe abbiano la stessa lunghezza
    n = len(mat)
    m = len(mat[0])
    if n != m:
        return False
    for r in range(1, n):
        if len(mat[r]) != m:
            return False
    # mat e' quadrata, non vuota
    trovato_non_zero_fuori_diagonale = False
    for i in range(n):
        for j in range(n):
            if i != j and mat[i][j] != 0:
                trovato_non_zero_fuori_diagonale = True
    if trovato_non_zero_fuori_diagonale:
        return False
    else:
        return True
            