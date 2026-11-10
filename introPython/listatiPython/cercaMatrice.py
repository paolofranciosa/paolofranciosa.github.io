def cerca_matrice_in_matrice(mat_grande, mat_piccola): # due matrici
    '''restituisce la prima coppia di posizioni di mat_grande in cui compare mat_piccola,
restituisce -1, -1 se non compare mai'''
    n1 = len(mat_grande)
    m1 = len(mat_grande[0])
    n2 = len(mat_piccola)
    m2 = len(mat_piccola[0])
    for pos_riga_iniziale in range(n1 - n2 + 1):
        for pos_colonna_iniziale in range(m1 - m2 +1)
            if esiste_copia_matrice(mat_grande, pos_riga_iniziale, pos_colonna_iniziale, mat_piccola):
                return pos_riga_iniziale, pos_colonna_iniziale
    return -1, -1

if __name__ == "__main__":
    r, c = cerca_matrice_in_matrice(..........)