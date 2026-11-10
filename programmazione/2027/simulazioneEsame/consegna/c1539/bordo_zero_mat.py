def bordo_zero_mat(M) :
    if len(M) == 1 and M[0][0] == 0:
        return True
  
    if sum(M[0]) and sum(M[len(M) -1]) != 0 :
        return False
    lista_colonne = []
    n_colonne = len(M[0])
    for riga in M:
        for elemento in range (n_colonne) :
            if elemento == 0 or elemento == n_colonne:
                lista_colonne.append(riga[elemento])
    if sum(lista_colonne) != 0 :
        return False
    return True
