def bordo_zero_mat(M):
    '''restituisca True se il bordo della matrice è costituito
esclusivamente da zeri, e che restituisca False altrimenti.'''
    for righe in M:
        for colonne in righe:
            if righe==0 or righe==(len(M)-1):
                if righe[colonne]!=0:
                    return False
            else:
                if colonne==0 or colonne==(len(righe)-1):
                    if righe[colonne]!=0:
                        return False
    return True                  