def verifica_mat_rett(m):
    if not isinstance(m, list) or len(m) <= 0:
        raise TypeError
    for riga in m:
        if not isinstance(riga, list) or len(riga) <= 0:
            print("errore, "+str(riga)+" non lista")
            raise TypeError
    ncol = len(m[0])
    for riga in m:
        if len(riga) != ncol:
            return False
    return True
