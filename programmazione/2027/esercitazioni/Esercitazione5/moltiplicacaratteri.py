def moltiplicacaratteri(stringa, c, x):
    stringa_nuova = ''
    for carattere in stringa:
        if carattere == c:
            stringa_nuova = stringa_nuova + carattere*x
        else:
            stringa_nuova = stringa_nuova + carattere
            
    return stringa_nuova
