def frequenze_relative(diz):
    '''Funzione che a partire da un dizionario che contiene
frequenze assolute delle chiavi, restituisce il dizionario
contenente le frequenze relative delle chiavi'''
    somma = 0
    for k in diz:
        somma += diz[k]
    
    rel = {}
    for k in diz:
        rel[k] = diz[k]/somma
    
    return rel